# Research Results: masothue.com Structure

## Progress Tracking
- [x] Check robots.txt (Allows everything except /Ajax/*)
- [x] Explore homepage for Industry and Province links
- [x] Analyze Industry URL pattern: `https://masothue.com/tra-cuu-ma-so-thue-theo-nganh-nghe/[slug]-[id]`
- [x] Analyze Province URL pattern: `https://masothue.com/tra-cuu-ma-so-thue-theo-tinh/[slug]-[id]`
- [x] Analyze Company listing data fields: Name, Tax Code, Representative, Address.
- [x] Analyze Pagination pattern: `?page=n`
- [x] Look for combined Industry + Province filtering: Not found in direct URL hierarchy; likely requires site search.
- [x] Identify anti-scraping measures: Persistent modal "Xem thêm nội dung" requiring ad view.

## Detailed Findings
### URL Patterns
- **Province List**: `https://masothue.com/tra-cuu-ma-so-thue-theo-tinh/`
- **Specific Province**: `https://masothue.com/tra-cuu-ma-so-thue-theo-tinh/[province-slug]-[id]` (e.g., `binh-duong-17`)
- **Industry List**: `https://masothue.com/tra-cuu-ma-so-thue-theo-nganh-nghe/`
- **Specific Industry**: `https://masothue.com/tra-cuu-ma-so-thue-theo-nganh-nghe/[industry-slug]-[id]` (e.g., `xay-dung-nha-cac-loai-4100`)
- **Pagination**: Appending `?page=2`, `?page=3`, etc., to any listing URL.

### Company Data Fields
Each listing contains:
1. **Company Name** (Link to detail page)
2. **Tax Code** (labeled as "Mã số thuế")
3. **Representative** (labeled as "Người đại diện")
4. **Address** (indicated by a location icon)

### Anti-Scraping Measures
- **Robots.txt**: Permissive except for `/Ajax/*`.
- **Engagement Barrier**: A modal named "Xem thêm nội dung" appears frequently, asking the user to watch an ad to "unlock" full access for 24 hours. This blocks interaction with the full list after a few items.
- **Dynamic Content**: Some data might be loaded via AJAX, though company lists are mostly in the initial HTML.

### Combined Search
- No direct "Province/Industry" combined URL found (e.g., `/binh-duong/xay-dung/` does not exist).
- Search query `https://masothue.com/Search/?q=[keyword]` can be used, but results are mixed.
