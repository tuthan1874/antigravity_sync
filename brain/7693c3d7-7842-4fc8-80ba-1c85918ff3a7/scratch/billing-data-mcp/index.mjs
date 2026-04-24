#!/usr/bin/env node
/**
 * TD Games Billing Data MCP Plugin for OpenClaw
 *
 * Provides 10 read-only tools for agents to query billing app data
 * from Supabase via the billing-report Edge Function.
 */

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const EDGE_FN_URL = process.env.BILLING_REPORT_URL ||
  "https://fifuhkupaqcfjwyouwpa.supabase.co/functions/v1/billing-report";
const SUPABASE_ANON_KEY = process.env.SUPABASE_ANON_KEY ||
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZpZnVoa3VwYXFjZmp3eW91d3BhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEzNDUyMjIsImV4cCI6MjA4NjkyMTIyMn0.tA8a5ElWwsupGZiNEG-1QMgMDJgykP6LNnxuVuZvwBY";

async function callBillingAPI(action, params = {}) {
  const res = await fetch(EDGE_FN_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "apikey": SUPABASE_ANON_KEY,
      "Authorization": `Bearer ${SUPABASE_ANON_KEY}`,
    },
    body: JSON.stringify({ action, params }),
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`Billing API error (${res.status}): ${text}`);
  }
  return await res.json();
}

function formatVND(n) {
  return Number(n).toLocaleString("vi-VN") + " ₫";
}

const server = new Server(
  { name: "billing-data", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

// ── List Tools ──────────────────────────────────────────────────
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "get_billing_overview",
      description: "Lấy tổng quan toàn bộ hệ thống billing: doanh thu, chi phí, P&L, số nhân viên, số dự án, tasks. Dùng để trả lời câu hỏi tổng quát về tình hình công ty.",
      inputSchema: { type: "object", properties: {}, required: [] },
    },
    {
      name: "get_revenue_report",
      description: "Báo cáo doanh thu theo tháng và theo khách hàng trong năm. Bao gồm số lượng hoá đơn, tổng doanh thu, breakdown theo tháng và client.",
      inputSchema: {
        type: "object",
        properties: {
          year: { type: "number", description: "Năm cần báo cáo (mặc định năm hiện tại)" },
        },
      },
    },
    {
      name: "get_expense_report",
      description: "Báo cáo chi phí theo category và tháng. Bao gồm P&L từng tháng, phân loại chi phí, và so sánh budget.",
      inputSchema: {
        type: "object",
        properties: {
          year: { type: "number", description: "Năm cần báo cáo" },
        },
      },
    },
    {
      name: "get_hr_summary",
      description: "Tóm tắt nhân sự: danh sách nhân viên active, phân bổ theo phòng ban, hợp đồng sắp hết hạn, đơn nghỉ phép chờ duyệt.",
      inputSchema: { type: "object", properties: {}, required: [] },
    },
    {
      name: "get_payroll_summary",
      description: "Tóm tắt bảng lương theo năm: lương ròng, chi phí công ty, số nhân viên mỗi tháng.",
      inputSchema: {
        type: "object",
        properties: {
          year: { type: "number", description: "Năm cần báo cáo" },
        },
      },
    },
    {
      name: "get_workforce_status",
      description: "Trạng thái dự án và nhân lực: workers, tasks theo status, settlements gần đây, project acceptances.",
      inputSchema: { type: "object", properties: {}, required: [] },
    },
    {
      name: "get_crm_pipeline",
      description: "Pipeline khách hàng và dự án CRM: danh sách clients, projects theo status, documents.",
      inputSchema: { type: "object", properties: {}, required: [] },
    },
    {
      name: "get_outreach_stats",
      description: "Thống kê email outreach: số leads, tỉ lệ gửi email, batches gần đây.",
      inputSchema: { type: "object", properties: {}, required: [] },
    },
    {
      name: "get_attendance_report",
      description: "Báo cáo chấm công và nghỉ phép theo tháng.",
      inputSchema: {
        type: "object",
        properties: {
          month: { type: "number", description: "Tháng (1-12)" },
          year: { type: "number", description: "Năm" },
        },
      },
    },
    {
      name: "get_monthly_kpi",
      description: "KPI tháng: doanh thu, chi phí, lợi nhuận, burn rate, headcount, tasks, revenue/employee.",
      inputSchema: {
        type: "object",
        properties: {
          month: { type: "number", description: "Tháng (1-12)" },
          year: { type: "number", description: "Năm" },
        },
      },
    },
  ],
}));

// ── Call Tool ────────────────────────────────────────────────────
const ACTION_MAP = {
  get_billing_overview: "overview",
  get_revenue_report: "revenue_report",
  get_expense_report: "expense_report",
  get_hr_summary: "hr_summary",
  get_payroll_summary: "payroll_summary",
  get_workforce_status: "workforce_status",
  get_crm_pipeline: "crm_pipeline",
  get_outreach_stats: "outreach_stats",
  get_attendance_report: "attendance_report",
  get_monthly_kpi: "monthly_kpi",
};

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args = {} } = request.params;
  const action = ACTION_MAP[name];
  if (!action) {
    return {
      content: [{ type: "text", text: `Unknown tool: ${name}` }],
      isError: true,
    };
  }

  try {
    const result = await callBillingAPI(action, args);
    return {
      content: [
        {
          type: "text",
          text: JSON.stringify(result.data, null, 2),
        },
      ],
    };
  } catch (error) {
    return {
      content: [{ type: "text", text: `Error: ${error.message}` }],
      isError: true,
    };
  }
});

// ── Start Server ────────────────────────────────────────────────
const transport = new StdioServerTransport();
await server.connect(transport);
console.error("Billing Data MCP server running on stdio");
