# CAB System

> Hệ thống nền tảng đặt xe trực tuyến CAB

---

# 1. Stakeholders

| Stakeholder | Vai trò | Nhiệm vụ |
|---|---|---|
| Ban giám đốc | Sponsor | Định hướng, phê duyệt mục tiêu, phạm vi và ngân sách |
| Product Owner | Product Owner | Xác định ưu tiên và quản lý sản phẩm |
| Business Analyst | Business Analyst | Thu thập, phân tích và làm rõ yêu cầu |
| Khách hàng | End User | Đặt xe, theo dõi, thanh toán và đánh giá |
| Tài xế | End User | Nhận và thực hiện chuyến |
| Nhân viên vận hành | Operations | Giám sát và xử lý hoạt động |
| Kế toán / Tài chính | Financial | Quản lý doanh thu và giao dịch |
| Quản trị hệ thống | Administrator | Quản lý tài khoản, quyền và cấu hình |
| Đội phát triển | Development | Phân tích, thiết kế, lập trình và kiểm thử |
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
- Quản lý thông tin cá nhân
- Quản lý quyền truy cập
- Quản lý trạng thái tài khoản

**Không quản lý:** Đặt xe, điều phối và thanh toán.

---

## 4.3 B02 - Driver & Vehicle Management

**Phạm vi:** Quản lý tài xế, phương tiện và trạng thái hoạt động.

- Quản lý hồ sơ tài xế
- Quản lý phương tiện
- Quản lý trạng thái tài xế
- Quản lý vị trí tài xế
- Theo dõi hoạt động tài xế

**Không quản lý:** Quyết định phân công và tính cước.

---

## 4.4 B03 - Booking & Trip Management

**Phạm vi:** Quản lý yêu cầu đặt xe và vòng đời chuyến.

- Tạo yêu cầu đặt xe
- Quản lý chuyến
- Cập nhật trạng thái
- Hủy / hoàn thành chuyến
- Lịch sử chuyến

**Không quản lý:** Thuật toán điều phối và thanh toán.

---

## 4.5 B04 - Driver Dispatch

**Phạm vi:** Tìm kiếm và phân công tài xế.

- Tìm tài xế phù hợp
- Ưu tiên tài xế
- Gửi yêu cầu nhận chuyến
- Xử lý từ chối / không phản hồi
- Tìm tài xế tiếp theo
- Xử lý trường hợp không có tài xế

**Không quản lý:** Tạo chuyến và tính cước.

---

## 4.6 B05 - Fare & Payment

**Phạm vi:** Tính số tiền và xử lý thanh toán.

- Tính cước
- Quản lý phương thức thanh toán
- Xử lý thanh toán
- Xử lý thanh toán thất bại
- Lưu lịch sử giao dịch
- Đối soát

**Không quản lý:** Thông tin thẻ hoặc tài khoản thanh toán nhạy cảm.

---

## 4.7 B06 - Notification

**Phạm vi:** Gửi thông báo nghiệp vụ.

- Thông báo đặt xe
- Thông báo phân công
- Thông báo trạng thái chuyến
- Thông báo thanh toán
- Quản lý kênh thông báo

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
- Báo cáo hiệu quả tài xế
- Dashboard KPI

---

# 5. Business Requirements

## BR01 - Quản lý người dùng
Hệ thống phải hỗ trợ đăng ký, đăng nhập, cập nhật thông tin và quản lý quyền người dùng.

## BR02 - Quản lý tài xế và phương tiện
Hệ thống phải hỗ trợ quản lý hồ sơ tài xế, phương tiện và trạng thái hoạt động.

## BR03 - Quản lý vị trí tài xế
Hệ thống phải quản lý vị trí tài xế để phục vụ điều phối và theo dõi chuyến.

## BR04 - Đặt xe
Hệ thống phải cho phép khách hàng tạo yêu cầu đặt xe với điểm đón, điểm đến và loại xe.

## BR05 - Quản lý chuyến đi
Hệ thống phải quản lý vòng đời chuyến từ khi tạo đến khi hoàn thành hoặc hủy.

## BR06 - Theo dõi chuyến
Hệ thống phải cho phép theo dõi trạng thái và thông tin chuyến.

## BR07 - Điều phối tài xế
Hệ thống phải tự động tìm và ưu tiên tài xế phù hợp.

## BR08 - Xử lý từ chối / Timeout
Hệ thống phải tiếp tục tìm tài xế khác khi tài xế từ chối hoặc không phản hồi.

## BR09 - Không tìm được tài xế
Hệ thống phải thông báo cho khách hàng khi không tìm được tài xế.

## BR10 - Tính cước
Hệ thống phải xác định số tiền khách hàng phải trả theo chính sách của doanh nghiệp.

## BR11 - Thanh toán
Hệ thống phải hỗ trợ thanh toán tiền mặt và thanh toán điện tử.

## BR12 - Thanh toán thất bại
Hệ thống phải thông báo và hỗ trợ xử lý lại giao dịch khi thanh toán thất bại.

## BR13 - Thông báo
Hệ thống phải thông báo các sự kiện quan trọng cho khách hàng và tài xế.

## BR14 - Quản lý vận hành
Hệ thống phải hỗ trợ nhân viên giám sát, tra cứu và xử lý các trường hợp bất thường.

## BR15 - Báo cáo
Hệ thống phải cung cấp báo cáo về chuyến, doanh thu, hoàn thành, hủy và hiệu quả tài xế.

## BR16 - Bảo mật và phân quyền
Hệ thống phải xác thực người dùng, kiểm soát quyền và bảo vệ dữ liệu.

## BR17 - Khả năng mở rộng
Hệ thống phải hỗ trợ mở rộng người dùng, dịch vụ, thanh toán và thông báo.

## BR18 - Audit
Hệ thống phải lưu vết các thao tác quan trọng.

---

# 6. Business Process

> Chỉ mô tả các bước nghiệp vụ chính.  
> Các chi tiết như timeout, retry, filter, API và provider sẽ được xử lý ở các tài liệu thiết kế sau.

## BP01 - Quản lý tài khoản
**BR:** BR01, BR16

1. Người dùng đăng ký / đăng nhập
2. Hệ thống xác thực và quản lý tài khoản

---

## BP02 - Đặt xe
**BR:** BR04, BR06, BR13

1. Khách hàng tạo yêu cầu đặt xe
2. Hệ thống tiếp nhận và tạo chuyến
3. Hệ thống thông báo trạng thái

---

## BP03 - Điều phối tài xế
**BR:** BR02, BR03, BR07, BR08, BR09, BR13

1. Hệ thống tìm tài xế phù hợp
2. Tài xế nhận hoặc từ chối chuyến
3. Hệ thống phân công hoặc tìm tài xế khác
4. Hệ thống thông báo kết quả

---

## BP04 - Thực hiện chuyến
**BR:** BR05, BR06, BR13

1. Tài xế thực hiện chuyến
2. Hệ thống cập nhật trạng thái và vị trí
3. Chuyến hoàn thành hoặc bị hủy

---

## BP05 - Tính cước & thanh toán
**BR:** BR10, BR11, BR12, BR13

1. Hệ thống tính cước
2. Khách hàng thanh toán
3. Hệ thống ghi nhận kết quả
4. Xử lý lại khi cần

---

## BP06 - Lịch sử & đánh giá
**BR:** BR05, BR06

1. Khách hàng xem lịch sử và thông tin chuyến
2. Khách hàng đánh giá tài xế
3. Hệ thống lưu kết quả

---

## BP07 - Vận hành & báo cáo
**BR:** BR14, BR15, BR16, BR18

1. Nhân viên giám sát và xử lý vận hành
2. Hệ thống lưu vết hoạt động
3. Hệ thống cung cấp báo cáo

---

## BP08 - Mở rộng hệ thống
**BR:** BR17

1. Mở rộng các thành phần hệ thống
2. Bổ sung dịch vụ, thanh toán và thông báo

---

# 7. Requirement Traceability

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
| BG09 | BR13 | BP02, BP03, BP04, BP05 |
| BG10 | BR14 | BP07 |
| BG11 | BR15 | BP07 |
| BG12 | BR17 | BP08 |
| BG13 | BR17 | BP08 |
| BG14 | BR16 | BP01, BP07 |
| BG15 | BR18 | BP07 |
| BG16 | BR17 | BP08 |
| BG17 | BR07, BR10, BR12 | BP03, BP05 |

---

# 8. Open Issues

Các nội dung chưa được doanh nghiệp xác định rõ và cần BA làm rõ trước khi phát triển:

- Chính sách tính cước
- Tiêu chí ưu tiên tài xế
- Thời gian timeout nhận chuyến
- Chính sách hủy chuyến
- Chính sách retry thanh toán
- Xử lý khi mất kết nối mạng
- Thời gian lưu trữ dữ liệu
- Chính sách bảo mật dữ liệu vị trí
- Chính sách lưu Audit Log

---

# 9. Tổng quan

### Business Domains

```text
B01 User Management
B02 Driver & Vehicle Management
B03 Booking & Trip Management
B04 Driver Dispatch
B05 Fare & Payment
B06 Notification
B07 Operations Management
B08 Reporting & Analytics
```

### Business Processes

```text
BP01 → Quản lý tài khoản
BP02 → Đặt xe
BP03 → Điều phối tài xế
BP04 → Thực hiện chuyến
BP05 → Tính cước & thanh toán
BP06 → Lịch sử & đánh giá
BP07 → Vận hành & báo cáo
BP08 → Mở rộng hệ thống
```

### Luồng nghiệp vụ chính

```text
Khách hàng
    ↓
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

