# Xây dựng n8n Workflow với Apify API cho LinkedIn Search

## Tổng quan

Tạo quy trình tự động hóa trên n8n để kết nối với Apify API, sử dụng Actor **google-search-scraper** để cào dữ liệu từ Google Search nhắm mục tiêu vào LinkedIn profiles. Workflow này sẽ mạnh mẽ hơn so với Google Custom Search API vì:

- **Không giới hạn quota**: Apify có thể cào nhiều kết quả hơn
- **Dữ liệu phong phú hơn**: Lấy được nhiều thông tin chi tiết từ search results
- **Linh hoạt**: Có thể tùy chỉnh các tham số scraping

## User Review Required

> [!IMPORTANT]
> **Apify API Key Required**: Bạn cần có Apify API token để sử dụng workflow này. Bạn có thể đăng ký miễn phí tại [https://apify.com/](https://apify.com/) và lấy API token từ Settings > Integrations.

> [!NOTE]
> **Apify Pricing**: Apify có free tier với $5 credit mỗi tháng. Actor `apify/google-search-scraper` tính phí khoảng $0.25 per 1000 results. Workflow này mặc định lấy 10 kết quả mỗi lần chạy.

## Proposed Changes

### n8n Workflow Components

Workflow sẽ bao gồm các nodes sau:

#### [NEW] [apify-linkedin-search-workflow.json](file:///e:/TDC_App/n8n-skills/apify-linkedin-search-workflow.json)

**Node 1: Form Trigger / Manual Trigger**
- Input fields: Job Title, Location
- Cho phép user nhập thông tin tìm kiếm

**Node 2: Prepare Apify Input**
- Code node để chuẩn bị input cho Apify Actor
- Tạo search query: `site:linkedin.com/in/ "Job Title" "Location"`
- Cấu hình các parameters cho google-search-scraper

**Node 3: Apify Actor Run (HTTP Request)**
- POST request đến Apify API để chạy Actor
- Endpoint: `https://api.apify.com/v2/acts/apify~google-search-scraper/runs`
- Headers: Authorization với Apify API token
- Body: Input configuration cho Actor

**Node 4: Wait for Actor Completion**
- Polling mechanism để đợi Actor hoàn thành
- GET request đến Actor run status endpoint
- Retry logic với timeout

**Node 5: Get Actor Results**
- GET request để lấy kết quả từ Actor dataset
- Endpoint: Dataset items API

**Node 6: Format LinkedIn Results**
- Code node để xử lý và format dữ liệu
- Extract: title, URL, snippet, position từ search results
- Filter chỉ lấy LinkedIn profile URLs

**Node 7: Output Results**
- Aggregate và format final output
- JSON structure với metadata và results list

---

#### [NEW] [apify-linkedin-search-simple.json](file:///e:/TDC_App/n8n-skills/apify-linkedin-search-simple.json)

**Simplified Version** - Sử dụng Apify Task thay vì Actor trực tiếp:
- Đơn giản hóa bằng cách tạo Apify Task trước
- Chỉ cần 3 nodes: Trigger → Run Task → Format Results
- Dễ maintain và configure hơn

---

### Documentation

#### [NEW] [docs/apify-linkedin-workflow-guide.md](file:///e:/TDC_App/n8n-skills/docs/apify-linkedin-workflow-guide.md)

Hướng dẫn chi tiết bao gồm:
- Cách setup Apify account và lấy API token
- Cách import workflow vào n8n
- Cách configure credentials
- Cách sử dụng workflow
- Troubleshooting common issues
- Ví dụ input/output

## Verification Plan

### Manual Verification

1. **Review workflow structure**: Kiểm tra logic flow và connections giữa các nodes
2. **Validate Apify API configuration**: Đảm bảo API endpoints và parameters đúng
3. **Check error handling**: Verify retry logic và error messages
4. **Review documentation**: Đảm bảo hướng dẫn đầy đủ và dễ hiểu

### User Testing Required

> [!WARNING]
> Workflow cần được test với Apify API token thực tế. Tôi sẽ tạo workflow structure nhưng bạn cần:
> 1. Đăng ký Apify account và lấy API token
> 2. Import workflow vào n8n instance của bạn
> 3. Configure Apify credentials
> 4. Test với sample inputs (ví dụ: Job Title="Software Engineer", Location="Vietnam")
