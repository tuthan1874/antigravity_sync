# Deploy td-games-invoice-app lên VPS

## Thông tin
- VPS: 180.93.144.98 | root | Port 22
- Domain: billing.tdgamestudio.com
- Deploy path: /opt/td-games-invoice-app
- Stack: Nginx static + Certbot SSL

## Checklist

- [ ] Đọc .env.local để lấy giá trị biến môi trường thật
- [ ] SSH: Cập nhật hệ thống và cài Node.js
- [ ] SSH: Clone repo từ GitHub
- [ ] SSH: Tạo .env với giá trị thật và build app
- [ ] SSH: Cấu hình Nginx cho domain billing.tdgamestudio.com
- [ ] SSH: Cài Certbot và cấp SSL
- [ ] Kiểm tra website hoạt động
