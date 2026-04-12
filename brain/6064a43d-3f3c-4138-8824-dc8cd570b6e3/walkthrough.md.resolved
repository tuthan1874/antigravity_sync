# Báo cáo Tổng quan VPS Megahost_02
**Ngày báo cáo:** 12/04/2026 23:05 (Giờ địa phương)

## 1. Thông tin Hệ thống
- **Tên Máy chủ:** Megahost_02 (Hostname: `vps6core`)
- **Hệ điều hành:** Ubuntu 22.04.5 LTS
- **Phiên bản Kernel:** 5.15.0-164-generic
- **Thời gian hoạt động (Uptime):** 92 ngày, 0 giờ

## 2. Tình trạng Tài nguyên
Hệ thống đang hoạt động rất ổn định với mức tải thấp.

| Tài nguyên | Sử dụng | Trạng thái |
| :--- | :--- | :--- |
| **CPU** | 6.96% | ✅ Rất tốt |
| **Memory** | 34.42% | ✅ Ổn định |
| **Disk** | 66.73% (59.9GB / 89.7GB) | ⚠️ Cần lưu ý |
| **Load Average** | 0.15, 0.19, 0.39 | ✅ Rất thấp |

## 3. Các Dịch vụ Quan trọng đang hoạt động
Hệ thống đang chạy tổng cộng **29 dịch vụ** hệ thống. Các dịch vụ cốt lõi của TD Games bao gồm:

- **ChatSync (`chatsync.service`)**: Đồng bộ ClickUp/Slack/Discord/Drive - **Đang chạy**
- **CLIProxyAPI (`cliproxy.service`)**: Model Proxy API - **Đang chạy**
- **TD Mem0 OSS (`td-mem0-oss.service`)**: Bộ nhớ AI (FastAPI) - **Đang chạy**
- **Slack Redirect (`slack-redirect.service`)**: Xử lý OAuth cho Slack - **Đang chạy**
- **Nginx & Docker**: Hạ tầng web và container - **Đang chạy**

## 4. Các Tiến trình hàng đầu (Top Processes)
Các tiến trình đang tiêu thụ tài nguyên nhiều nhất:

1. **openclaw-gateway**: 14.4% CPU (Tiến trình chính của Gateway AI)
2. **moltbot (Java)**: 12.0% Memory (Bot dịch vụ)
3. **Open WebUI**: 5.8% Memory (Giao diện người dùng web)
4. **CLIProxyAPI**: Hoạt động ổn định ở mức nền.

## 5. Đánh giá & Khuyến nghị
- **Hiệu năng:** VPS đang hoạt động cực kỳ mượt mà, tài nguyên CPU và RAM còn rất dồi dào.
- **Lưu trữ:** Ổ đĩa đã sử dụng hơn 66%. Khuyến nghị kiểm tra và dọn dẹp các log cũ hoặc file không cần thiết nếu con số này vượt quá 85%.
- **Tính ổn định:** Uptime 92 ngày cho thấy hệ thống rất tin cậy.

> [!TIP]
> Bạn có thể sử dụng lệnh `df -h` để xem chi tiết các phân vùng đĩa nếu cần kiểm tra sâu hơn về dung lượng.
