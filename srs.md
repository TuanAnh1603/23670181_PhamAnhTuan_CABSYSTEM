# CAB System

> Hệ thống nền tảng đặt xe trực tuyến CAB

---

# 1. Stakeholders

| Stakeholder | Vai trò | Nhiệm vụ |
|---|---|---|
| Ban giám đốc | Sponsor | Định hướng, phê duyệt mục tiêu, phạm vi và ngân sách |
| Product Owner | Product Owner | Xác định ưu tiên và quản lý sản phẩm |
| Business Analyst | Business Analyst | Phân tích và làm rõ yêu cầu |
| Khách hàng | End User | Đặt xe, theo dõi, thanh toán, đánh giá |
| Tài xế | End User | Nhận và thực hiện chuyến |
| Nhân viên vận hành | Operations | Giám sát và xử lý hoạt động |
| Kế toán / Tài chính | Financial | Quản lý doanh thu và giao dịch |
| Quản trị hệ thống | Administrator | Quản lý tài khoản, quyền và cấu hình |
| Đội phát triển | Development | Thiết kế, lập trình và kiểm thử |
| DevOps / IT | Technical | Hạ tầng, triển khai và giám sát |
| Security / Compliance | Security | Bảo mật và kiểm tra hệ thống |
| Nhà cung cấp thanh toán | External Provider | Xử lý thanh toán điện tử |
| Nhà cung cấp bản đồ | External Provider | Cung cấp vị trí và định tuyến |
| Nhà cung cấp thông báo | External Provider | Gửi thông báo |

---

# 2. Stakeholder Influence Matrix

| Stakeholder | Ảnh hưởng | Quan tâm | Chiến lược |
|---|---|---|---|
| Ban giám đốc | Cao | Cao | Quản lý chặt chẽ |
| Product Owner | Cao | Cao | Quản lý chặt chẽ |
| Business Analyst | Cao | Cao | Quản lý chặt chẽ |
| Quản lý vận hành | Cao | Cao | Quản lý chặt chẽ |
| Kế toán / Tài chính | Cao | Cao | Quản lý chặt chẽ |
| Security / Compliance | Cao | Cao | Quản lý chặt chẽ |
| DevOps / IT | Cao | Cao | Phối hợp thường xuyên |
| Nhân viên vận hành | Cao | Cao | Phối hợp thường xuyên |
| Khách hàng | Trung bình | Cao | Tham khảo và cập nhật |
| Tài xế | Trung bình | Cao | Tham khảo và cập nhật |
| Đội phát triển | Trung bình | Cao | Phối hợp thường xuyên |
| Nhà cung cấp thanh toán | Trung bình | Trung bình | Duy trì hài lòng |
| Nhà cung cấp bản đồ | Trung bình | Trung bình | Duy trì hài lòng |
| Nhà cung cấp thông báo | Thấp - Trung bình | Trung bình | Theo dõi |

---

# 3. Business Goals

| Mã | Business Goal | Mô tả |
|---|---|---|
| BG01 | Xây dựng nền tảng CAB | Xây dựng nền tảng đặt xe trực tuyến tập trung |
| BG02 | Nâng cao trải nghiệm khách hàng | Hỗ trợ đặt xe, theo dõi, thanh toán và đánh giá |
| BG03 | Tự động hóa điều phối | Tự động tìm và phân công tài xế |
| BG04 | Giảm thời gian tìm tài xế | Tự động tìm tài xế khác khi cần |
| BG05 | Quản lý tài xế tập trung | Quản lý tài xế, phương tiện và vị trí |
| BG06 | Minh bạch trạng thái chuyến | Theo dõi chuyến trong suốt vòng đời |
| BG07 | Tự động hóa tính cước và thanh toán | Hỗ trợ tính cước và thanh toán |
| BG08 | Bảo vệ thông tin thanh toán | Không lưu dữ liệu thanh toán nhạy cảm |
| BG09 | Thông báo đa kênh | Hỗ trợ nhiều kênh thông báo |
| BG10 | Nâng cao hiệu quả vận hành | Hỗ trợ giám sát và xử lý sự cố |
| BG11 | Báo cáo quản trị | Cung cấp dữ liệu phục vụ quản lý |
| BG12 | Khả năng mở rộng | Hỗ trợ lượng lớn người dùng |
| BG13 | Tính ổn định | Lỗi một thành phần không làm dừng toàn hệ thống |
| BG14 | Bảo mật | Xác thực, phân quyền và bảo vệ dữ liệu |
| BG15 | Audit | Lưu vết các thao tác quan trọng |
| BG16 | Linh hoạt phát triển | Dễ bổ sung chức năng và dịch vụ |
| BG17 | Chuẩn hóa nghiệp vụ | Làm rõ các chính sách còn chưa xác định |

---

# 4. Business Boundary

## 4.1 Business Domains

| Mã | Business Domain | Phạm vi |
|---|---|---|
| B01 | User Management | Tài khoản và quyền người dùng |
| B02 | Driver & Vehicle Management | Tài xế, phương tiện và vị trí |
| B03 | Booking & Trip Management | Đặt xe và chuyến đi |
| B04 | Driver Dispatch | Tìm và phân công tài xế |
| B05 | Fare & Payment | Tính cước và thanh toán |
| B06 | Notification | Quản lý thông báo |
| B07 | Operations Management | Giám sát và xử lý vận hành |
| B08 | Reporting & Analytics | Báo cáo và thống kê |

---

## 4.2 B01 - User Management

**Phạm vi:** Quản lý tài khoản và danh tính người dùng.

- Đăng ký / đăng nhập
- Xác thực tài khoản
- Quản lý thông tin
- Quản lý quyền
- Quản lý trạng thái tài khoản

---

## 4.3 B02 - Driver & Vehicle Management

**Phạm vi:** Quản lý tài xế, phương tiện và trạng thái hoạt động.

- Quản lý hồ sơ tài xế
- Quản lý phương tiện
- Quản lý trạng thái
- Quản lý vị trí
- Theo dõi hoạt động

---

## 4.4 B03 - Booking & Trip Management

**Phạm vi:** Quản lý yêu cầu đặt xe và vòng đời chuyến.

- Tạo yêu cầu
- Quản lý chuyến
- Cập nhật trạng thái
- Hủy / hoàn thành
- Lịch sử chuyến

---

## 4.5 B04 - Driver Dispatch

**Phạm vi:** Tìm kiếm và phân công tài xế.

- Tìm tài xế
- Ưu tiên tài xế
- Gửi yêu cầu nhận chuyến
- Xử lý từ chối / không phản hồi
- Tìm tài xế khác
- Xử lý không có tài xế

---

## 4.6 B05 - Fare & Payment

**Phạm vi:** Tính tiền và xử lý thanh toán.

- Tính cước
- Quản lý phương thức thanh toán
- Xử lý thanh toán
- Xử lý thất bại
- Lịch sử giao dịch
- Đối soát

---

## 4.7 B06 - Notification

**Phạm vi:** Gửi thông báo nghiệp vụ.

- Thông báo đặt xe
- Thông báo phân công
- Thông báo trạng thái
- Thông báo thanh toán
- Quản lý kênh

**Kênh:** Push, SMS, Email.

---

## 4.8 B07 - Operations Management

**Phạm vi:** Giám sát và xử lý hoạt động vận hành.

- Giám sát chuyến
- Giám sát tài xế
- Hỗ trợ khách hàng
- Xử lý sự cố
- Tra cứu giao dịch
- Quản lý quyền nhân viên

---

## 4.9 B08 - Reporting & Analytics

**Phạm vi:** Tổng hợp dữ liệu phục vụ quản trị.

- Báo cáo chuyến
- Báo cáo doanh thu
- Báo cáo hoàn thành
- Báo cáo hủy
- Báo cáo tài xế
- Dashboard KPI

---

# 5. Business Requirements

| Mã | Business Requirement |
|---|---|
| BR01 | Hệ thống phải hỗ trợ đăng ký, đăng nhập, cập nhật thông tin và quản lý quyền người dùng. |
| BR02 | Hệ thống phải quản lý hồ sơ tài xế, phương tiện và trạng thái hoạt động. |
| BR03 | Hệ thống phải quản lý vị trí tài xế để phục vụ điều phối và theo dõi. |
| BR04 | Hệ thống phải cho phép khách hàng tạo yêu cầu đặt xe. |
| BR05 | Hệ thống phải quản lý vòng đời chuyến từ tạo đến hoàn thành hoặc hủy. |
| BR06 | Hệ thống phải cho phép theo dõi trạng thái và thông tin chuyến. |
| BR07 | Hệ thống phải tự động tìm và ưu tiên tài xế phù hợp. |
| BR08 | Hệ thống phải tìm tài xế khác khi tài xế từ chối hoặc không phản hồi. |
| BR09 | Hệ thống phải thông báo khi không tìm được tài xế. |
| BR10 | Hệ thống phải xác định số tiền khách hàng phải trả theo chính sách. |
| BR11 | Hệ thống phải hỗ trợ thanh toán tiền mặt và điện tử. |
| BR12 | Hệ thống phải thông báo và hỗ trợ xử lý lại khi thanh toán thất bại. |
| BR13 | Hệ thống phải thông báo các sự kiện quan trọng cho khách hàng và tài xế. |
| BR14 | Hệ thống phải hỗ trợ nhân viên giám sát và xử lý các trường hợp bất thường. |
| BR15 | Hệ thống phải cung cấp báo cáo về chuyến, doanh thu và hiệu quả tài xế. |
| BR16 | Hệ thống phải xác thực, phân quyền và bảo vệ dữ liệu. |
| BR17 | Hệ thống phải hỗ trợ mở rộng người dùng, dịch vụ, thanh toán và thông báo. |
| BR18 | Hệ thống phải lưu vết các thao tác quan trọng. |

---

# 6. Business Process

> Chỉ giữ các bước nghiệp vụ chính.  
> Chi tiết kỹ thuật sẽ được xử lý ở Functional Requirement và Design.

| Mã | Quy trình | BR liên quan | Các bước chính |
|---|---|---|---|
| BP01 | Quản lý tài khoản | BR01, BR16 | Đăng ký / đăng nhập → Xác thực → Quản lý tài khoản |
| BP02 | Đặt xe | BR04, BR06, BR13 | Tạo yêu cầu → Tiếp nhận → Thông báo |
| BP03 | Điều phối tài xế | BR02, BR03, BR07–BR09, BR13 | Tìm tài xế → Nhận / từ chối → Phân công hoặc tìm tiếp → Thông báo |
| BP04 | Thực hiện chuyến | BR05, BR06, BR13 | Nhận chuyến → Thực hiện → Cập nhật → Hoàn thành / hủy |
| BP05 | Tính cước & thanh toán | BR10–BR13 | Tính cước → Thanh toán → Ghi nhận kết quả → Xử lý thất bại |
| BP06 | Lịch sử & đánh giá | BR05, BR06 | Xem lịch sử → Đánh giá → Lưu kết quả |
| BP07 | Vận hành & báo cáo | BR14–BR16, BR18 | Giám sát → Xử lý → Ghi nhận → Báo cáo |
| BP08 | Mở rộng hệ thống | BR17 | Mở rộng → Bổ sung dịch vụ / thanh toán / thông báo |

---

# 7. Business Flow

| Bước | Quy trình |
|---|---|
| 1 | Khách hàng đặt xe |
| 2 | Hệ thống điều phối tài xế |
| 3 | Tài xế thực hiện chuyến |
| 4 | Hệ thống tính cước |
| 5 | Khách hàng thanh toán |
| 6 | Khách hàng xem lịch sử và đánh giá |

### Luồng chính

```text
Đặt xe
   ↓
Điều phối tài xế
   ↓
Thực hiện chuyến
   ↓
Tính cước
   ↓
Thanh toán
   ↓
Lịch sử & đánh giá
```

---

# 8. Requirement Traceability

| Business Goal | Business Requirement | Business Process |
|---|---|---|
| BG01 | BR04, BR05 | BP02, BP04 |
| BG02 | BR04, BR06, BR11, BR13 | BP02, BP05, BP06 |
| BG03 | BR07, BR08 | BP03 |
| BG04 | BR08, BR09 | BP03 |
| BG05 | BR02, BR03 | BP03, BP04 |
| BG06 | BR05, BR06 | BP04 |
| BG07 | BR10, BR11, BR12 | BP05 |
| BG08 | BR11, BR16 | BP05 |
| BG09 | BR13 | BP02–BP05 |
| BG10 | BR14 | BP07 |
| BG11 | BR15 | BP07 |
| BG12 | BR17 | BP08 |
| BG13 | BR17 | BP08 |
| BG14 | BR16 | BP01, BP07 |
| BG15 | BR18 | BP07 |
| BG16 | BR17 | BP08 |
| BG17 | BR07, BR10, BR12 | BP03, BP05 |

---

# 9. Open Issues

Các vấn đề cần xác nhận với khách hàng:

| STT | Nội dung cần làm rõ |
|---|---|
| 1 | Chính sách tính cước |
| 2 | Tiêu chí ưu tiên tài xế |
| 3 | Thời gian tài xế phản hồi |
| 4 | Chính sách hủy chuyến |
| 5 | Chính sách retry thanh toán |
| 6 | Xử lý khi mất kết nối |
| 7 | Thời gian lưu trữ dữ liệu |
| 8 | Chính sách bảo mật dữ liệu vị trí |
| 9 | Thời gian lưu Audit Log |




