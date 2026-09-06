# 🚕 CAB System

> Nền tảng đặt xe trực tuyến CAB

---

# 1. Stakeholders

| Stakeholder | Vai trò | Nhiệm vụ |
|---|---|---|
| Ban giám đốc | Sponsor | Định hướng, phê duyệt mục tiêu, phạm vi, ngân sách |
| Product Owner | Product Owner | Xác định ưu tiên và quản lý sản phẩm |
| Business Analyst | BA | Phân tích và làm rõ yêu cầu |
| Khách hàng | End User | Đặt xe, theo dõi, thanh toán, đánh giá |
| Tài xế | End User | Nhận, thực hiện và hoàn thành chuyến |
| Nhân viên vận hành | Operations | Giám sát và xử lý sự cố |
| Kế toán / Tài chính | Financial | Quản lý doanh thu và giao dịch |
| Quản trị hệ thống | Administrator | Quản lý tài khoản, quyền và cấu hình |
| Đội phát triển | Development | Thiết kế, lập trình, kiểm thử |
| DevOps / IT | Technical | Hạ tầng, triển khai, giám sát |
| Security / Compliance | Security | Bảo mật, phân quyền, Audit |
| Payment Provider | External | Xử lý thanh toán điện tử |
| Map Provider | External | Cung cấp vị trí và định tuyến |
| Notification Provider | External | Gửi thông báo |

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
| Payment Provider | Trung bình | Trung bình | Duy trì hài lòng |
| Map Provider | Trung bình | Trung bình | Duy trì hài lòng |
| Notification Provider | Thấp - Trung bình | Trung bình | Theo dõi |

---

# 3. Business Goals

| Mã | Business Goal |
|---|---|
| BG01 | Xây dựng nền tảng CAB đặt xe trực tuyến |
| BG02 | Nâng cao trải nghiệm khách hàng |
| BG03 | Tự động hóa điều phối tài xế |
| BG04 | Giảm thời gian tìm tài xế |
| BG05 | Quản lý tài xế tập trung |
| BG06 | Minh bạch trạng thái chuyến |
| BG07 | Tự động hóa tính cước và thanh toán |
| BG08 | Bảo vệ thông tin thanh toán |
| BG09 | Hỗ trợ thông báo đa kênh |
| BG10 | Nâng cao hiệu quả vận hành |
| BG11 | Cung cấp báo cáo quản trị |
| BG12 | Đảm bảo khả năng mở rộng |
| BG13 | Đảm bảo tính ổn định |
| BG14 | Đảm bảo bảo mật |
| BG15 | Lưu vết Audit |
| BG16 | Linh hoạt phát triển trong tương lai |
| BG17 | Chuẩn hóa nghiệp vụ |

---

# 4. Business Boundary

## 4.1 Business Domains

| Mã | Business Domain | Phạm vi |
|---|---|---|
| B01 | User Management | Tài khoản, danh tính, quyền |
| B02 | Driver & Vehicle | Tài xế, phương tiện, trạng thái, vị trí |
| B03 | Booking & Trip | Đặt xe và vòng đời chuyến |
| B04 | Driver Dispatch | Tìm và phân công tài xế |
| B05 | Fare & Payment | Tính cước và thanh toán |
| B06 | Notification | Gửi và quản lý thông báo |
| B07 | Operations | Giám sát và xử lý vận hành |
| B08 | Reporting | Báo cáo và thống kê |

---

## 4.2 B01 - User Management

**Phạm vi:** Quản lý tài khoản và danh tính người dùng.

| Mã | Business con |
|---|---|
| B01.01 | Đăng ký tài khoản |
| B01.02 | Đăng nhập & xác thực |
| B01.03 | Quản lý hồ sơ |
| B01.04 | Phân quyền |
| B01.05 | Trạng thái tài khoản |

---

## 4.3 B02 - Driver & Vehicle

**Phạm vi:** Quản lý tài xế, phương tiện và trạng thái hoạt động.

| Mã | Business con |
|---|---|
| B02.01 | Hồ sơ tài xế |
| B02.02 | Quản lý phương tiện |
| B02.03 | Trạng thái tài xế |
| B02.04 | Vị trí tài xế |
| B02.05 | Lịch sử hoạt động |

---

## 4.4 B03 - Booking & Trip

**Phạm vi:** Quản lý yêu cầu đặt xe và vòng đời chuyến.

| Mã | Business con |
|---|---|
| B03.01 | Tạo yêu cầu đặt xe |
| B03.02 | Quản lý chuyến |
| B03.03 | Cập nhật trạng thái |
| B03.04 | Hủy / hoàn thành |
| B03.05 | Lịch sử chuyến |

---

## 4.5 B04 - Driver Dispatch

**Phạm vi:** Tìm kiếm, lựa chọn và phân công tài xế.

| Mã | Business con |
|---|---|
| B04.01 | Tìm tài xế |
| B04.02 | Ưu tiên tài xế |
| B04.03 | Gửi yêu cầu nhận chuyến |
| B04.04 | Xử lý nhận / từ chối / timeout |
| B04.05 | Điều phối lại |
| B04.06 | Không tìm được tài xế |

---

## 4.6 B05 - Fare & Payment

**Phạm vi:** Tính cước và xử lý thanh toán.

| Mã | Business con |
|---|---|
| B05.01 | Tính cước |
| B05.02 | Chọn phương thức thanh toán |
| B05.03 | Xử lý giao dịch |
| B05.04 | Xử lý thanh toán thất bại |
| B05.05 | Lịch sử giao dịch |
| B05.06 | Đối soát |

---

## 4.7 B06 - Notification

**Phạm vi:** Quản lý và gửi thông báo.

| Mã | Business con |
|---|---|
| B06.01 | Thông báo đặt xe |
| B06.02 | Thông báo tài xế |
| B06.03 | Thông báo trạng thái chuyến |
| B06.04 | Thông báo thanh toán |
| B06.05 | Quản lý kênh |

**Kênh:** Push / SMS / Email

---

## 4.8 B07 - Operations

**Phạm vi:** Giám sát và xử lý hoạt động vận hành.

| Mã | Business con |
|---|---|
| B07.01 | Giám sát chuyến |
| B07.02 | Giám sát tài xế |
| B07.03 | Hỗ trợ khách hàng |
| B07.04 | Xử lý sự cố |
| B07.05 | Hỗ trợ giao dịch |
| B07.06 | Quản lý quyền nhân viên |

---

## 4.9 B08 - Reporting

**Phạm vi:** Tổng hợp dữ liệu phục vụ quản trị.

| Mã | Business con |
|---|---|
| B08.01 | Báo cáo chuyến |
| B08.02 | Báo cáo doanh thu |
| B08.03 | Báo cáo hoàn thành |
| B08.04 | Báo cáo hủy |
| B08.05 | Hiệu quả tài xế |
| B08.06 | Dashboard KPI |

---

# 5. Business Requirements

| Mã | Business Requirement |
|---|---|
| BR01 | Hỗ trợ đăng ký, đăng nhập, cập nhật và quản lý quyền người dùng |
| BR02 | Quản lý hồ sơ tài xế, phương tiện và trạng thái hoạt động |
| BR03 | Quản lý vị trí tài xế phục vụ điều phối và theo dõi |
| BR04 | Cho phép khách hàng tạo yêu cầu đặt xe |
| BR05 | Quản lý vòng đời chuyến từ tạo đến hoàn thành hoặc hủy |
| BR06 | Cho phép theo dõi trạng thái và thông tin chuyến |
| BR07 | Tự động tìm và ưu tiên tài xế phù hợp |
| BR08 | Tự động tìm tài xế khác khi từ chối hoặc timeout |
| BR09 | Thông báo khi không tìm được tài xế |
| BR10 | Tính số tiền khách hàng phải trả |
| BR11 | Hỗ trợ thanh toán tiền mặt và điện tử |
| BR12 | Xử lý và retry khi thanh toán thất bại |
| BR13 | Gửi thông báo đến khách hàng và tài xế |
| BR14 | Hỗ trợ nhân viên giám sát và xử lý sự cố |
| BR15 | Cung cấp báo cáo chuyến, doanh thu và tài xế |
| BR16 | Xác thực, phân quyền và bảo vệ dữ liệu |
| BR17 | Hỗ trợ mở rộng hệ thống và bổ sung dịch vụ |
| BR18 | Lưu vết các thao tác quan trọng |

---

# 6. Business Process

> Quy trình được tối giản thành **7 quy trình chính**.

| Mã | Quy trình | Các bước |
|---|---|---|
| BP01 | Quản lý tài khoản | Đăng ký / đăng nhập → Xác thực → Quản lý tài khoản |
| BP02 | Đặt & quản lý chuyến | Tạo yêu cầu → Tiếp nhận → Theo dõi → Hủy / Hoàn thành |
| BP03 | Điều phối tài xế | Tìm tài xế → Gửi chuyến → Nhận / Từ chối → Điều phối lại |
| BP04 | Thực hiện chuyến | Nhận chuyến → Đón khách → Di chuyển → Hoàn thành |
| BP05 | Tính cước & thanh toán | Tính cước → Thanh toán → Ghi nhận kết quả |
| BP06 | Hậu chuyến | Xem lịch sử → Xem cước → Đánh giá |
| BP07 | Vận hành & báo cáo | Giám sát → Xử lý → Audit → Báo cáo |

---

# 7. Functional Requirements

| Mã | Functional Requirement | BR |
|---|---|---|
| FR01 | Đăng ký, đăng nhập và quản lý tài khoản | BR01 |
| FR02 | Quản lý tài xế và phương tiện | BR02 |
| FR03 | Quản lý vị trí tài xế | BR03 |
| FR04 | Tạo và quản lý chuyến | BR04, BR05 |
| FR05 | Theo dõi trạng thái chuyến | BR06 |
| FR06 | Tự động tìm và phân công tài xế | BR07 |
| FR07 | Xử lý từ chối, timeout và điều phối lại | BR08, BR09 |
| FR08 | Tính cước chuyến | BR10 |
| FR09 | Xử lý thanh toán | BR11, BR12 |
| FR10 | Gửi thông báo | BR13 |
| FR11 | Quản lý vận hành | BR14 |
| FR12 | Báo cáo và thống kê | BR15 |
| FR13 | Phân quyền và bảo mật | BR16 |
| FR14 | Lưu và tra cứu Audit Log | BR18 |

---

# 8. Roles

| Role | Nhiệm vụ |
|---|---|
| Khách hàng | Đặt xe, theo dõi, thanh toán, đánh giá |
| Tài xế | Nhận và thực hiện chuyến |
| Nhân viên vận hành | Giám sát và xử lý sự cố |
| Quản trị viên | Quản lý tài khoản và phân quyền |
| Kế toán | Quản lý giao dịch và doanh thu |
| Hệ thống | Điều phối, tính cước, gửi thông báo |
| Payment Provider | Xử lý thanh toán |
| Map Provider | Cung cấp vị trí và định tuyến |
| Notification Provider | Gửi thông báo |

---

# 9. Exceptions

| Mã | Exception | Xử lý |
|---|---|---|
| EX01 | Không tìm được tài xế | Thông báo khách hàng |
| EX02 | Tài xế từ chối | Điều phối tài xế khác |
| EX03 | Tài xế timeout | Điều phối tài xế khác |
| EX04 | Khách hủy chuyến | Xử lý theo chính sách |
| EX05 | Thanh toán thất bại | Thông báo và retry |
| EX06 | Mất kết nối | Đồng bộ lại khi kết nối |
| EX07 | Lỗi thông báo | Retry, không dừng đặt xe |
| EX08 | Lỗi hệ thống | Ghi log và xử lý |

---

# 10. Non-Functional Requirements

| Mã | Nhóm | Yêu cầu |
|---|---|---|
| NFR01 | Performance | Đáp ứng tốt khi có nhiều yêu cầu đồng thời |
| NFR02 | Scalability | Có thể mở rộng khi tải tăng |
| NFR03 | Availability | Lỗi một thành phần không làm dừng toàn hệ thống |
| NFR04 | Security | Bảo vệ dữ liệu và kiểm soát truy cập |
| NFR05 | Reliability | Đảm bảo dữ liệu chuyến và giao dịch chính xác |
| NFR06 | Maintainability | Dễ bảo trì và triển khai |
| NFR07 | Auditability | Lưu vết thao tác quan trọng |
| NFR08 | Extensibility | Dễ thêm dịch vụ, thanh toán và thông báo |

---

# 11. Entities

| Mã | Entity | Mục đích |
|---|---|---|
| E01 | User | Tài khoản người dùng |
| E02 | Driver | Thông tin tài xế |
| E03 | Vehicle | Thông tin phương tiện |
| E04 | VehicleType | Loại xe |
| E05 | DriverLocation | Vị trí tài xế |
| E06 | Booking | Yêu cầu đặt xe |
| E07 | Trip | Chuyến đi |
| E08 | Fare | Thông tin cước |
| E09 | Payment | Thanh toán |
| E10 | Notification | Thông báo |
| E11 | Rating | Đánh giá |
| E12 | AuditLog | Nhật ký hệ thống |

---

# 12. Entity Relationships

| Entity | Quan hệ | Entity |
|---|---|---|
| User | 1 - 1 | Driver |
| Driver | 1 - N | Vehicle |
| VehicleType | 1 - N | Vehicle |
| Driver | 1 - N | DriverLocation |
| User | 1 - N | Booking |
| Booking | 1 - 1 | Trip |
| Driver | 1 - N | Trip |
| Trip | 1 - 1 | Fare |
| Trip | 1 - 1 | Payment |
| User | 1 - N | Notification |
| User | 1 - N | Rating |
| Trip | 1 - 1 | Rating |
| User | 1 - N | AuditLog |

---

# 13. Use Cases

| Mã | Use Case | Actor | FR |
|---|---|---|---|
| UC01 | Quản lý tài khoản | Khách hàng, Tài xế, Admin | FR01 |
| UC02 | Quản lý tài xế & phương tiện | Tài xế, Operations | FR02 |
| UC03 | Quản lý vị trí tài xế | Tài xế, Hệ thống | FR03 |
| UC04 | Đặt xe | Khách hàng | FR04 |
| UC05 | Quản lý & theo dõi chuyến | Khách hàng, Tài xế, Operations | FR05 |
| UC06 | Điều phối tài xế | Hệ thống, Tài xế | FR06, FR07 |
| UC07 | Tính cước | Hệ thống | FR08 |
| UC08 | Thanh toán | Khách hàng, Payment Provider | FR09 |
| UC09 | Gửi thông báo | Hệ thống, Notification Provider | FR10 |
| UC10 | Quản lý vận hành | Operations | FR11 |
| UC11 | Báo cáo & thống kê | Quản lý, Kế toán | FR12 |
| UC12 | Phân quyền & bảo mật | Admin | FR13 |
| UC13 | Audit hệ thống | Admin, Security | FR14 |
| UC14 | Đánh giá tài xế | Khách hàng | FR05 |

---

# 14. Main Use Case Flow

```text
Khách hàng
    ↓
Đặt xe
    ↓
Điều phối tài xế
    ↓
Tài xế nhận chuyến
    ↓
Thực hiện chuyến
    ↓
Tính cước
    ↓
Thanh toán
    ↓
Đánh giá

