/**
 * Import SalesQL_Enriched_Leads.csv → Supabase crm_outreach_leads
 * Run: node import_leads.js
 */
const fs = require('fs');
const path = require('path');

const SUPABASE_URL = 'https://fifuhkupaqcfjwyouwpa.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZpZnVoa3VwYXFjZmp3eW91d3BhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEzNDUyMjIsImV4cCI6MjA4NjkyMTIyMn0.tA8a5ElWwsupGZiNEG-1QMgMDJgykP6LNnxuVuZvwBY';

const CSV_PATH = path.resolve('e:/TDC_App/TDGAMES_App/Client_Data/output/SalesQL_Enriched_Leads.csv');

function parseTier(tierStr) {
  if (!tierStr) return 99;
  if (tierStr.includes('Tier 1') || tierStr.includes('⭐')) return 1;
  if (tierStr.includes('Tier 2') || tierStr.includes('★')) return 2;
  if (tierStr.includes('Tier 3') || tierStr.includes('☆')) return 3;
  return 99;
}

function parseCSV(text) {
  const lines = text.trim().split('\n');
  if (lines.length < 2) return [];
  
  // Parse header
  const headers = [];
  let current = '';
  let inQuotes = false;
  for (const ch of lines[0]) {
    if (ch === '"') { inQuotes = !inQuotes; continue; }
    if ((ch === ',' || ch === '\r') && !inQuotes) { headers.push(current.trim().toLowerCase()); current = ''; continue; }
    if (ch === '\r') continue;
    current += ch;
  }
  headers.push(current.trim().toLowerCase());
  
  const results = [];
  for (let i = 1; i < lines.length; i++) {
    if (!lines[i].trim()) continue;
    
    const values = [];
    current = '';
    inQuotes = false;
    for (const ch of lines[i]) {
      if (ch === '"') { inQuotes = !inQuotes; continue; }
      if ((ch === ',' || ch === '\r') && !inQuotes) { values.push(current.trim()); current = ''; continue; }
      if (ch === '\r') continue;
      current += ch;
    }
    values.push(current.trim());
    
    const row = {};
    headers.forEach((h, idx) => { row[h] = values[idx] || ''; });
    results.push(row);
  }
  return results;
}

async function main() {
  console.log('Reading CSV...');
  const csvText = fs.readFileSync(CSV_PATH, 'utf-8');
  const rows = parseCSV(csvText);
  console.log(`Parsed ${rows.length} rows from CSV`);
  
  // Deduplicate by email - keep best tier
  const emailMap = new Map();
  for (const row of rows) {
    // Choose best email: Work > Personal
    const workEmail = (row.work_email || '').split('|')[0].trim();
    const personalEmail = (row.personal_email || '').split('|')[0].trim();
    const email = workEmail || personalEmail;
    if (!email || email === 'nan') continue;
    
    const tierNum = parseTier(row.tier || '');
    const contactName = (row.contact_name || '').trim();
    const firstName = contactName.split(' ')[0] || '';
    
    const existing = emailMap.get(email);
    if (!existing || tierNum < existing.tier) {
      emailMap.set(email, {
        studio_name: (row.studio || '').trim(),
        contact_name: contactName,
        first_name: firstName,
        email: email,
        job_title: (row.job_title || '').trim(),
        linkedin_url: (row.linkedin || '').trim(),
        tier: tierNum,
        outreach_status: 'pending',
        source: 'csv_import',
        tags: [],
        notes: '',
      });
    }
  }
  
  const leads = Array.from(emailMap.values());
  // Filter out tier 99 (Unranked) to focus on actionable leads
  const actionableLeads = leads.filter(l => l.tier <= 3);
  console.log(`Deduplicated: ${leads.length} unique emails, ${actionableLeads.length} with Tier 1-3`);
  
  // Import all leads (including unranked) - batch 50 at a time
  const BATCH_SIZE = 50;
  let imported = 0;
  let skipped = 0;
  
  for (let i = 0; i < leads.length; i += BATCH_SIZE) {
    const batch = leads.slice(i, i + BATCH_SIZE);
    
    const res = await fetch(`${SUPABASE_URL}/rest/v1/crm_outreach_leads`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'apikey': SUPABASE_KEY,
        'Authorization': `Bearer ${SUPABASE_KEY}`,
        'Prefer': 'resolution=ignore-duplicates,return=minimal',
      },
      body: JSON.stringify(batch),
    });
    
    if (res.ok) {
      imported += batch.length;
      console.log(`  Batch ${Math.floor(i/BATCH_SIZE)+1}: ${batch.length} leads imported (total: ${imported})`);
    } else {
      const errText = await res.text();
      // Try inserting one by one on batch failure
      console.log(`  Batch ${Math.floor(i/BATCH_SIZE)+1} failed, trying one-by-one...`);
      for (const lead of batch) {
        const r2 = await fetch(`${SUPABASE_URL}/rest/v1/crm_outreach_leads`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'apikey': SUPABASE_KEY,
            'Authorization': `Bearer ${SUPABASE_KEY}`,
            'Prefer': 'resolution=ignore-duplicates,return=minimal',
          },
          body: JSON.stringify(lead),
        });
        if (r2.ok) {
          imported++;
        } else {
          skipped++;
        }
      }
      console.log(`    Imported: ${imported}, Skipped: ${skipped}`);
    }
  }
  
  console.log(`\n✅ Done! Imported: ${imported}, Skipped: ${skipped}`);
  console.log(`Total unique leads in database should be: ${imported + 5} (5 were already there)`);
}

main().catch(console.error);
