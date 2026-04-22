"""Email Sending Routes"""
import random, logging, threading, time
from datetime import datetime
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from services.gmail_sender import send_email, personalize, get_quota_status, SENDER_EMAIL
from services.supabase_client import get_lead, update_lead_status, log_email, get_template, get_all_templates, get_pending_leads

router = APIRouter()
logger = logging.getLogger("td-mailer")

# ---- Batch status (single global state) ----
_batch_status = {
    "running": False, "current": 0, "total": 0,
    "success": 0, "failed": 0,
    "started_at": None, "finished_at": None, "last_error": "",
    "results": [],
}

# ---- Request Models ----
class SendRequest(BaseModel):
    lead_id: str
    template_name: str = "initial_outreach"

class BatchRequest(BaseModel):
    template_name: str = "initial_outreach"
    limit: int = 30
    min_delay: int = 120
    max_delay: int = 300

class TestRequest(BaseModel):
    to_email: str = ""
    template_name: str = "initial_outreach"

class PreviewRequest(BaseModel):
    template_name: str = "initial_outreach"
    contact_name: str = "Tony"
    studio_name: str = "Test Studio"
    job_title: str = "Art Director"

class VerifyRequest(BaseModel):
    email: str
    company_name: Optional[str] = None

class BulkVerifyRequest(BaseModel):
    limit: int = 50

class BounceCheckRequest(BaseModel):
    days_back: int = 7
    max_results: int = 50
    auto_update: bool = True

# ---- Helper: send one lead ----
def _send_one_lead(lead, tpl, template_name):
    contact = {
        'first_name': lead.get('first_name', ''),
        'contact_name': lead.get('contact_name', ''),
        'studio_name': lead.get('studio_name', ''),
        'job_title': lead.get('job_title', ''),
        'company': lead.get('studio_name', ''),
    }
    html_body = personalize(tpl['html_content'], contact)
    subjects = tpl.get('subject_lines', [])
    if not subjects:
        subjects = [f"Art & Animation Outsourcing for {contact['studio_name']}"]
    subject = personalize(random.choice(subjects), contact)
    status_map = {
        'initial_outreach': ('initial_sent', 'initial_sent_at'),
        'followup_1': ('followup1_sent', 'followup1_sent_at'),
        'followup_2': ('followup2_sent', 'followup2_sent_at'),
    }
    new_status, ts_field = status_map.get(template_name, ('initial_sent', 'initial_sent_at'))
    result = {"lead_id": lead['id'], "to": lead['email'], "studio": lead.get('studio_name', ''), "contact": lead.get('contact_name', ''), "tier": lead.get('tier', 99), "subject": subject}
    msg_id, error = send_email(lead['email'], subject, html_body)
    if msg_id:
        update_lead_status(lead['id'], new_status, ts_field)
        log_email(lead['id'], template_name, lead['email'], subject, msg_id, 'sent')
        result["status"] = "sent"
        result["message_id"] = msg_id
        return True, result
    else:
        log_email(lead['id'], template_name, lead['email'], subject, '', 'failed', error)
        result["status"] = "failed"
        result["error"] = error
        return False, result

# ---- Background batch runner (sync, runs in thread) ----
def _run_batch(template_name, lead_ids, min_delay, max_delay):
    global _batch_status
    _batch_status = {
        "running": True, "current": 0, "total": len(lead_ids),
        "success": 0, "failed": 0,
        "started_at": datetime.now().isoformat(), "finished_at": None,
        "last_error": "", "results": [],
    }
    for i, lid in enumerate(lead_ids):
        _batch_status["current"] = i + 1
        quota = get_quota_status()
        if quota["remaining"] <= 0:
            _batch_status["last_error"] = "Quota exhausted"
            break
        try:
            lead = get_lead(lid)
            tpl = get_template(template_name)
            if not tpl:
                _batch_status["failed"] += 1
                continue
            success, result = _send_one_lead(lead, tpl, template_name)
            result["index"] = i + 1
            _batch_status["results"].append(result)
            if success:
                _batch_status["success"] += 1
                logger.info(f"[{i+1}/{len(lead_ids)}] Sent to {lead['email']} ({lead.get('studio_name','')})")
            else:
                _batch_status["failed"] += 1
                logger.warning(f"[{i+1}/{len(lead_ids)}] Failed: {lead['email']}")
        except Exception as e:
            _batch_status["failed"] += 1
            _batch_status["last_error"] = str(e)
            _batch_status["results"].append({"index": i + 1, "lead_id": lid, "status": "error", "error": str(e)})
        if i < len(lead_ids) - 1:
            delay = random.randint(min_delay, max_delay)
            logger.info(f"  Waiting {delay}s before next send...")
            time.sleep(delay)
    _batch_status["running"] = False
    _batch_status["finished_at"] = datetime.now().isoformat()

# ════════════════════════════════════════════════════════════
# ENDPOINTS
# ════════════════════════════════════════════════════════════

@router.post("/send")
async def send(req: SendRequest):
    quota = get_quota_status()
    if quota["remaining"] <= 0:
        raise HTTPException(status_code=429, detail="Daily limit reached")
    try:
        lead = get_lead(req.lead_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Lead not found: {e}")
    try:
        tpl = get_template(req.template_name)
    except Exception:
        raise HTTPException(status_code=404, detail=f"Template '{req.template_name}' not found")
    if not tpl:
        raise HTTPException(status_code=404, detail=f"Template '{req.template_name}' not found")
    success, result = _send_one_lead(lead, tpl, req.template_name)
    if success:
        return {"success": True, **result}
    raise HTTPException(status_code=500, detail=f"Send failed: {result.get('error','unknown')}")

@router.post("/batch")
async def batch_send(req: BatchRequest):
    global _batch_status
    if _batch_status["running"]:
        return {"error": "Batch already running", "status": _batch_status}
    quota = get_quota_status()
    if quota["remaining"] <= 0:
        raise HTTPException(status_code=429, detail="Daily limit reached")
    actual_limit = min(req.limit, quota["remaining"])
    from services.supabase_client import get_client
    client = get_client()
    status_for_template = {'initial_outreach': 'pending', 'followup_1': 'initial_sent', 'followup_2': 'followup1_sent'}
    target_status = status_for_template.get(req.template_name, 'pending')
    result = client.table('crm_outreach_leads').select('id').eq('outreach_status', target_status).limit(actual_limit).execute()
    lead_ids = [r['id'] for r in (result.data or [])]
    if not lead_ids:
        return {"error": "No leads found", "count": 0}
    t = threading.Thread(target=_run_batch, args=(req.template_name, lead_ids, req.min_delay, req.max_delay), daemon=True)
    t.start()
    return {"started": True, "count": len(lead_ids), "delay_range": f"{req.min_delay}-{req.max_delay}s", "estimated_time_min": round(len(lead_ids) * (req.min_delay + req.max_delay) / 2 / 60, 1)}

@router.get("/batch-status")
async def batch_status():
    return _batch_status

@router.post("/test")
async def test_send(req: TestRequest):
    to = req.to_email or SENDER_EMAIL
    try:
        tpl = get_template(req.template_name)
    except Exception:
        tpl = None
    if tpl:
        contact = {'first_name': 'Tony', 'studio_name': 'Test Studio', 'job_title': 'Art Director', 'company': 'Test Studio'}
        html = personalize(tpl['html_content'], contact)
        subject = f"[TEST] {personalize(random.choice(tpl.get('subject_lines', ['Test'])), contact)}"
    else:
        html = "<h1>Test</h1><p>Test from TD Mailer API.</p>"
        subject = "[TEST] TD Mailer API"
    msg_id, error = send_email(to, subject, html)
    if msg_id:
        return {"success": True, "message_id": msg_id, "to": to}
    raise HTTPException(status_code=500, detail=f"Failed: {error}")

@router.post("/preview")
async def preview(req: PreviewRequest):
    try:
        tpl = get_template(req.template_name)
    except Exception:
        tpl = None
    if not tpl:
        raise HTTPException(status_code=404, detail="Template not found")
    contact = {'first_name': req.contact_name, 'contact_name': req.contact_name, 'studio_name': req.studio_name, 'job_title': req.job_title, 'company': req.studio_name}
    html = personalize(tpl['html_content'], contact)
    subject = personalize(random.choice(tpl.get('subject_lines', ['Preview'])), contact)
    return {"html": html, "subject": subject}

@router.get("/status")
async def status():
    return get_quota_status()

# ════════════════════════════════════════════════════════════
# EMAIL VERIFICATION (Enhanced v2)
# ════════════════════════════════════════════════════════════
from services.email_verifier import verify_email as _verify_email

@router.post("/verify")
async def verify_single(req: VerifyRequest):
    result = _verify_email(req.email, req.company_name)
    return {"email": req.email, **result}

@router.post("/verify-pending")
async def verify_pending_leads(req: BulkVerifyRequest):
    from services.supabase_client import get_client
    client = get_client()
    result = client.table('crm_outreach_leads').select('id,email,studio_name').eq('outreach_status', 'pending').limit(req.limit).execute()
    leads = result.data or []
    verified = 0
    invalid = 0
    valid = 0
    high_risk = 0
    results = []
    for lead in leads:
        vr = _verify_email(lead['email'], lead.get('studio_name', ''))
        verified += 1
        if not vr['valid'] or vr.get('deliverable') == 'no':
            client.table('crm_outreach_leads').update({
                'outreach_status': 'invalid_email',
                'notes': f"Invalid: {vr['reason']}. {', '.join(vr.get('warnings', []))}"
            }).eq('id', lead['id']).execute()
            invalid += 1
        elif vr.get('risk_level') == 'high':
            notes = f"HIGH RISK: {', '.join(vr.get('warnings', []))}"
            client.table('crm_outreach_leads').update({'notes': notes}).eq('id', lead['id']).execute()
            high_risk += 1
            valid += 1
        else:
            valid += 1
        results.append({"email": lead['email'], "studio": lead.get('studio_name', ''), **vr})
    return {"verified": verified, "valid": valid, "invalid": invalid, "high_risk": high_risk, "results": results}

# ════════════════════════════════════════════════════════════
# BOUNCE DETECTION
# ════════════════════════════════════════════════════════════
from services.bounce_detector import scan_bounces

@router.post("/check-bounces")
async def check_bounces(req: BounceCheckRequest):
    bounces = scan_bounces(max_results=req.max_results, days_back=req.days_back)
    updated = 0
    already_marked = 0
    not_found = 0
    if req.auto_update and bounces:
        from services.supabase_client import get_client
        client = get_client()
        for bounce in bounces:
            result = client.table('crm_outreach_leads').select('id,outreach_status').eq('email', bounce['email']).execute()
            leads_found = result.data or []
            for lead in leads_found:
                if lead['outreach_status'] == 'bounced':
                    already_marked += 1
                    bounce['db_status'] = 'already_marked'
                else:
                    client.table('crm_outreach_leads').update({
                        'outreach_status': 'bounced',
                        'notes': f"Bounced: {bounce['reason']} ({bounce.get('bounce_date', '')[:20]})"
                    }).eq('id', lead['id']).execute()
                    updated += 1
                    bounce['db_status'] = 'updated'
            if not leads_found:
                not_found += 1
                bounce['db_status'] = 'not_in_db'
    return {
        "bounces_found": len(bounces),
        "leads_updated": updated,
        "already_marked": already_marked,
        "not_in_db": not_found,
        "bounces": bounces,
    }

@router.get("/health-check")
async def email_health_check():
    from services.supabase_client import get_client
    client = get_client()
    sent = client.table('crm_outreach_leads').select('id', count='exact').in_('outreach_status', ['initial_sent', 'followup1_sent', 'followup2_sent']).execute()
    bounced = client.table('crm_outreach_leads').select('id', count='exact').eq('outreach_status', 'bounced').execute()
    invalid = client.table('crm_outreach_leads').select('id', count='exact').eq('outreach_status', 'invalid_email').execute()
    pending = client.table('crm_outreach_leads').select('id', count='exact').eq('outreach_status', 'pending').execute()
    sent_count = sent.count or 0
    bounced_count = bounced.count or 0
    invalid_count = invalid.count or 0
    pending_count = pending.count or 0
    quota = get_quota_status()
    bounce_rate = (bounced_count / sent_count * 100) if sent_count > 0 else 0
    return {
        "pending": pending_count, "sent": sent_count,
        "bounced": bounced_count, "invalid": invalid_count,
        "bounce_rate": round(bounce_rate, 1),
        "quota": quota,
        "health": "good" if bounce_rate < 5 else ("warning" if bounce_rate < 10 else "critical"),
    }
