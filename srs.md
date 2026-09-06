# CAB System

> Hệ thống nền tảng đặt xe trực tuyến CAB

---

# 1. Stakeholders

| Stakeholder | Vai trò | Nhiệm vụ |
|---|---|---|
| Ban giám đốc | Sponsor | Định hướng, phê duyệt mục tiêu, phạm vi và ngân sách |
| Product Owner | Product Owner | Xác định ưu tiên và quản lý sản phẩm |
| Business Analyst | Business Analyst | Phân tích và làm rõ yêu cầu |
| Khách hàng | End User | Đặt xe, theo dõi chuyến, thanh toán và đánh giá |
| Tài xế | End User | Nhận chuyến, thực hiện và hoàn thành chuyến |
| Nhân viên vận hành | Operations | Giám sát và xử lý hoạt động |
| Kế toán / Tài chính | Financial | Quản lý doanh thu và giao dịch |
| Quản trị hệ thống | Administrator | Quản lý tài khoản, quyền và cấu hình |
| Đội phát triển | Development | Thiết kế, lập trình và kiểm thử |
| DevOps / IT | Technical | Hạ tầng, triển khai và giám sát |
| Security / Compliance | Security | Bảo mật, phân quyền và audit |
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
| BG04 | Giảm thời gian tìm tài xế | Tự động tìm tài xế khác khi bị từ chối hoặc timeout |
| BG05 | Quản lý tài xế tập trung | Quản lý hồ sơ, phương tiện, trạng thái và vị trí |
| BG06 | Minh bạch trạng thái chuyến | Theo dõi chuyến trong suốt vòng đời |
| BG07 | Tự động hóa tính cước và thanh toán | Hỗ trợ tính cước và nhiều phương thức thanh toán |
| BG08 | Bảo vệ thông tin thanh toán | Không lưu dữ liệu thanh toán nhạy cảm |
| BG09 | Thông báo đa kênh | Hỗ trợ Push, SMS và Email |
| BG10 | Nâng cao hiệu quả vận hành | Hỗ trợ giám sát và xử lý sự cố |
| BG11 | Báo cáo quản trị | Cung cấp dữ liệu về chuyến, doanh thu và tài xế |
| BG12 | Khả năng mở rộng | Hỗ trợ số lượng lớn khách hàng và tài xế |
| BG13 | Tính ổn định | Lỗi một thành phần không làm dừng toàn hệ thống |
| BG14 | Bảo mật | Xác thực, phân quyền và bảo vệ dữ liệu |
| BG15 | Audit | Lưu vết các thao tác quan trọng |
| BG16 | Linh hoạt phát triển | Dễ bổ sung dịch vụ, thanh toán và thông báo |
| BG17 | Chuẩn hóa nghiệp vụ | Làm rõ các chính sách nghiệp vụ còn chưa xác định |

---

# 4. Business Boundary

## 4.1 Business Domains

| Mã | Business Domain | Phạm vi quản lý |
|---|---|---|
| B01 | User Management | Tài khoản, danh tính và quyền |
| B02 | Driver & Vehicle Management | Tài xế, phương tiện, trạng thái và vị trí |
| B03 | Booking & Trip Management | Đặt xe và vòng đời chuyến |
| B04 | Driver Dispatch | Tìm kiếm và phân công tài xế |
| B05 | Fare & Payment | Tính cước và thanh toán |
| B06 | Notification | Gửi và quản lý thông báo |
| B07 | Operations Management | Giám sát và xử lý vận hành |
| B08 | Reporting & Analytics | Báo cáo và thống kê |

---

## 4.2 B01 - User Management

**Phạm vi:** Quản lý tài khoản và danh tính người dùng.

| Mã | Business con | Phạm vi |
|---|---|---|
| B01.01 | Đăng ký tài khoản | Tạo tài khoản |
| B01.02 | Đăng nhập & xác thực | Xác thực người dùng |
| B01.03 | Quản lý hồ sơ | Cập nhật thông tin |
| B01.04 | Phân quyền | Quản lý quyền truy cập |
| B01.05 | Trạng thái tài khoản | Active / Locked / Suspended |

**Không quản lý:** Đặt xe, điều phối, tính cước và thanh toán.

---

## 4.3 B02 - Driver & Vehicle Management

**Phạm vi:** Quản lý tài xế, phương tiện và trạng thái hoạt động.

| Mã | Business con | Phạm vi |
|---|---|---|
| B02.01 | Hồ sơ tài xế | Thông tin tài xế |
| B02.02 | Phương tiện | Thông tin xe và loại xe |
| B02.03 | Trạng thái tài xế | Online / Offline / Available / Busy |
| B02.04 | Vị trí tài xế | Cập nhật vị trí |
| B02.05 | Hoạt động tài xế | Theo dõi lịch sử hoạt động |

**Không quản lý:** Quyết định phân công, tính cước và thanh toán.

---

## 4.4 B03 - Booking & Trip Management

**Phạm vi:** Quản lý yêu cầu đặt xe và vòng đời chuyến.

| Mã | Business con | Phạm vi |
|---|---|---|
| B03.01 | Tạo yêu cầu | Điểm đón, điểm đến, loại xe |
| B03.02 | Quản lý chuyến | Quản lý thông tin chuyến |
| B03.03 | Trạng thái chuyến | Theo dõi trạng thái |
| B03.04 | Hủy / hoàn thành | Kết thúc chuyến |
| B03.05 | Lịch sử chuyến | Tra cứu chuyến |

---

## 4.5 B04 - Driver Dispatch

**Phạm vi:** Tìm kiếm, lựa chọn và phân công tài xế.

| Mã | Business con | Phạm vi |
|---|---|---|
| B04.01 | Tìm tài xế | Tìm tài xế phù hợp |
| B04.02 | Ưu tiên tài xế | Xếp hạng theo tiêu chí |
| B04.03 | Gửi yêu cầu | Gửi chuyến cho tài xế |
| B04.04 | Xử lý phản hồi | Nhận / từ chối / timeout |
| B04.05 | Tìm tài xế khác | Re-dispatch |
| B04.06 | Không tìm được tài xế | Kết thúc tìm kiếm |

---

## 4.6 B05 - Fare & Payment

**Phạm vi:** Tính số tiền phải trả và xử lý thanh toán.

| Mã | Business con | Phạm vi |
|---|---|---|
| B05.01 | Tính cước | Xác định giá chuyến |
| B05.02 | Phương thức thanh toán | Cash / Electronic |
| B05.03 | Xử lý thanh toán | Tạo và xử lý giao dịch |
| B05.04 | Thanh toán thất bại | Retry / Failed |
| B05.05 | Lịch sử giao dịch | Tra cứu thanh toán |
| B05.06 | Đối soát | Kiểm tra giao dịch |

---

## 4.7 B06 - Notification

**Phạm vi:** Quản lý và gửi thông báo nghiệp vụ.

| Mã | Business con | Phạm vi |
|---|---|---|
| B06.01 | Thông báo đặt xe | Yêu cầu được tiếp nhận |
| B06.02 | Thông báo tài xế | Tài xế nhận chuyến |
| B06.03 | Thông báo chuyến | Thay đổi trạng thái |
| B06.04 | Thông báo thanh toán | Kết quả thanh toán |
| B06.05 | Quản lý kênh | Push / SMS / Email |

> Notification là thành phần hỗ trợ. Nếu Notification lỗi, các nghiệp vụ chính vẫn phải tiếp tục hoạt động.

---

## 4.8 B07 - Operations Management

**Phạm vi:** Giám sát và xử lý hoạt động vận hành.

| Mã | Business con | Phạm vi |
|---|---|---|
| B07.01 | Giám sát chuyến | Theo dõi chuyến đang chạy |
| B07.02 | Giám sát tài xế | Theo dõi trạng thái |
| B07.03 | Hỗ trợ khách hàng | Tra cứu và hỗ trợ |
| B07.04 | Xử lý sự cố | Xử lý chuyến bất thường |
| B07.05 | Hỗ trợ giao dịch | Tra cứu thanh toán |
| B07.06 | Quản lý quyền | Phân quyền nhân viên |

---

## 4.9 B08 - Reporting & Analytics

**Phạm vi:** Tổng hợp dữ liệu phục vụ quản trị.

| Mã | Business con | Phạm vi |
|---|---|---|
| B08.01 | Báo cáo chuyến | Số lượng chuyến |
| B08.02 | Báo cáo doanh thu | Doanh thu |
| B08.03 | Báo cáo hoàn thành | Completion Rate |
| B08.04 | Báo cáo hủy | Cancellation Rate |
| B08.05 | Báo cáo tài xế | Driver Performance |
| B08.06 | Dashboard | KPI vận hành |

---

# 5. Business Requirements

| Mã | Business Requirement |
|---|---|
| BR01 | Hệ thống phải hỗ trợ đăng ký, đăng nhập, cập nhật thông tin và quản lý quyền người dùng. |
| BR02 | Hệ thống phải quản lý hồ sơ tài xế, phương tiện và trạng thái hoạt động. |
| BR03 | Hệ thống phải quản lý vị trí tài xế để phục vụ điều phối và theo dõi. |
| BR04 | Hệ thống phải cho phép khách hàng tạo yêu cầu đặt xe. |
| BR05 | Hệ thống phải quản lý vòng đời chuyến từ tạo đến hoàn thành hoặc hủy. |
| BR06 | Hệ thống phải cho phép khách hàng theo dõi trạng thái và thông tin chuyến. |
| BR07 | Hệ thống phải tự động tìm và ưu tiên tài xế phù hợp. |
| BR08 | Hệ thống phải tìm tài xế khác khi tài xế từ chối hoặc không phản hồi. |
| BR09 | Hệ thống phải thông báo khi không tìm được tài xế. |
| BR10 | Hệ thống phải xác định số tiền khách hàng phải trả theo chính sách tính cước. |
| BR11 | Hệ thống phải hỗ trợ thanh toán tiền mặt và thanh toán điện tử. |
| BR12 | Hệ thống phải thông báo và hỗ trợ xử lý lại khi thanh toán thất bại. |
| BR13 | Hệ thống phải gửi thông báo về các sự kiện quan trọng cho khách hàng và tài xế. |
| BR14 | Hệ thống phải hỗ trợ nhân viên giám sát và xử lý các trường hợp bất thường. |
| BR15 | Hệ thống phải cung cấp báo cáo về chuyến, doanh thu và hiệu quả tài xế. |
| BR16 | Hệ thống phải xác thực, phân quyền và bảo vệ dữ liệu. |
| BR17 | Hệ thống phải hỗ trợ mở rộng quy mô và bổ sung dịch vụ trong tương lai. |
| BR18 | Hệ thống phải lưu vết các thao tác quan trọng để phục vụ kiểm tra. |

---

# 6. Business Process

> Quy trình được tối giản thành **7 Business Process chính**.
> Không tách các thao tác kỹ thuật nhỏ thành Business Process riêng.

| Mã | Quy trình | BR liên quan | Các bước chính |
|---|---|---|---|
| BP01 | Quản lý tài khoản | BR01, BR16 | Đăng ký / đăng nhập → Xác thực → Quản lý tài khoản |
| BP02 | Đặt & quản lý chuyến | BR04, BR05, BR06, BR13 | Tạo yêu cầu → Tiếp nhận → Theo dõi → Hủy / Hoàn thành |
| BP03 | Điều phối tài xế | BR02, BR03, BR07, BR08, BR09, BR13 | Tìm tài xế → Gửi chuyến → Nhận / từ chối → Phân công hoặc tìm tiếp |
| BP04 | Thực hiện chuyến | BR02, BR03, BR05, BR06, BR13 | Nhận chuyến → Thực hiện → Cập nhật trạng thái → Hoàn thành |
| BP05 | Tính cước & thanh toán | BR10, BR11, BR12, BR13 | Tính cước → Thanh toán → Ghi nhận kết quả → Xử lý thất bại |
| BP06 | Hậu chuyến | BR05, BR06, BR13 | Xem lịch sử → Xem cước → Đánh giá → Lưu kết quả |
| BP07 | Vận hành & báo cáo | BR14, BR15, BR16, BR18 | Giám sát → Xử lý → Audit → Báo cáo |

---

# 7. Business Flow

## 7.1 Luồng chính

```text
Khách hàng
    ↓
BP01 - Quản lý tài khoản
    ↓
BP02 - Đặt & quản lý chuyến
    ↓
BP03 - Điều phối tài xế
    ↓
BP04 - Thực hiện chuyến
    ↓
BP05 - Tính cước & thanh toán
    ↓
BP06 - Hậu chuyến
```

## 7.2 Luồng vận hành

```text
BP07 - Vận hành & báo cáo
        ↓
Giám sát
        ↓
Xử lý sự cố
        ↓
Audit
        ↓
Báo cáo
```

---

# 8. Business Process Detail

## BP01 - Quản lý tài khoản

| Bước | Nội dung |
|---|---|
| 1 | Người dùng đăng ký hoặc đăng nhập |
| 2 | Hệ thống xác thực |
| 3 | Người dùng quản lý thông tin tài khoản |

---

## BP02 - Đặt & quản lý chuyến

| Bước | Nội dung |
|---|---|
| 1 | Khách hàng nhập thông tin và tạo yêu cầu |
| 2 | Hệ thống tiếp nhận yêu cầu |
| 3 | Khách hàng theo dõi trạng thái |
| 4 | Chuyến được hoàn thành hoặc hủy |

---

## BP03 - Điều phối tài xế

| Bước | Nội dung |
|---|---|
| 1 | Hệ thống tìm tài xế phù hợp |
| 2 | Gửi yêu cầu nhận chuyến |
| 3 | Tài xế nhận, từ chối hoặc không phản hồi |
| 4 | Hệ thống phân công hoặc tìm tài xế khác |

---

## BP04 - Thực hiện chuyến

| Bước | Nội dung |
|---|---|
| 1 | Tài xế nhận chuyến |
| 2 | Tài xế đến điểm đón và đón khách |
| 3 | Tài xế thực hiện chuyến |
| 4 | Tài xế hoàn thành chuyến |

---

## BP05 - Tính cước & thanh toán

| Bước | Nội dung |
|---|---|
| 1 | Hệ thống tính cước |
| 2 | Khách hàng thanh toán |
| 3 | Hệ thống ghi nhận kết quả |
| 4 | Nếu thất bại, thực hiện xử lý lại theo chính sách |

---

## BP06 - Hậu chuyến

| Bước | Nội dung |
|---|---|
| 1 | Khách hàng xem lịch sử chuyến |
| 2 | Xem số tiền đã thanh toán |
| 3 | Đánh giá tài xế |
| 4 | Hệ thống lưu kết quả |

---

## BP07 - Vận hành & báo cáo

| Bước | Nội dung |
|---|---|
| 1 | Nhân viên giám sát hệ thống |
| 2 | Xử lý trường hợp bất thường |
| 3 | Hệ thống lưu Audit Log |
| 4 | Quản lý xem báo cáo |

---

# 9. Requirement Traceability Matrix

| Business Goal | Business Requirement | Business Process |
|---|---|---|
| BG01 | BR04, BR05 | BP02, BP04 |
| BG02 | BR04, BR06, BR11, BR13 | BP02, BP05, BP06 |
| BG03 | BR07, BR08 | BP03 |
| BG04 | BR08, BR09 | BP03 |
| BG05 | BR02, BR03 | BP03, BP04 |
| BG06 | BR05, BR06 | BP02, BP04 |
| BG07 | BR10, BR11, BR12 | BP05 |
| BG08 | BR11, BR16 | BP05 |
| BG09 | BR13 | BP02–BP06 |
| BG10 | BR14 | BP07 |
| BG11 | BR15 | BP07 |
| BG12 | BR17 | Toàn hệ thống |
| BG13 | BR17 | Toàn hệ thống |
| BG14 | BR16 | BP01, BP07 |
| BG15 | BR18 | BP07 |
| BG16 | BR17 | Toàn hệ thống |
| BG17 | BR07, BR10, BR12 | BP03, BP05 |

---

# 10. Non-Functional Requirements

| Mã | Nhóm | Yêu cầu |
|---|---|---|
| NFR01 | Performance | Hệ thống phải đáp ứng tốt khi số lượng người dùng tăng cao. |
| NFR02 | Scalability | Các thành phần có thể mở rộng độc lập khi tải tăng. |
| NFR03 | Availability | Lỗi thanh toán hoặc thông báo không làm dừng chức năng đặt xe. |
| NFR04 | Security | Bảo vệ dữ liệu cá nhân, vị trí và giao dịch. |
| NFR05 | Authorization | Chức năng quản trị phải được phân quyền. |
| NFR06 | Auditability | Các thao tác quan trọng phải được ghi log. |
| NFR07 | Maintainability | Có thể thay đổi hoặc nâng cấp từng thành phần mà hạn chế ảnh hưởng toàn hệ thống. |
| NFR08 | Extensibility | Có thể bổ sung dịch vụ, phương thức thanh toán và kênh thông báo. |

---

# 11. Business Rules

| Mã | Business Rule |
|---|---|
| BRULE01 | Chỉ người dùng đã xác thực mới được sử dụng chức năng yêu cầu tài khoản. |
| BRULE02 | Chỉ tài xế ở trạng thái sẵn sàng mới được xem xét điều phối. |
| BRULE03 | Tài xế từ chối hoặc không phản hồi thì hệ thống có thể tìm tài xế khác. |
| BRULE04 | Nếu không tìm được tài xế, khách hàng phải được thông báo. |
| BRULE05 | Chuyến hoàn thành phải được tính cước trước khi ghi nhận thanh toán. |
| BRULE06 | Thông tin thanh toán nhạy cảm không được lưu trực tiếp trong CAB. |
| BRULE07 | Thanh toán thất bại phải được ghi nhận và xử lý theo chính sách retry. |
| BRULE08 | Chức năng quản trị phải kiểm tra quyền trước khi thực hiện thao tác. |
| BRULE09 | Các thao tác quan trọng phải được ghi nhận vào Audit Log. |

---

# 12. Open Issues

Các nội dung cần Business Analyst xác nhận với khách hàng:

| STT | Nội dung |
|---|---|
| 1 | Công thức và chính sách tính cước |
| 2 | Tiêu chí ưu tiên tài xế |
| 3 | Thời gian tài xế phải phản hồi |
| 4 | Số lần hoặc thời gian retry điều phối |
| 5 | Chính sách hủy chuyến |
| 6 | Chính sách retry thanh toán |
| 7 | Xử lý khi mất kết nối mạng |
| 8 | Thời gian lưu trữ dữ liệu |
| 9 | Chính sách lưu trữ dữ liệu vị trí |
| 10 | Thời gian lưu Audit Log |

---

# 13. Tổng kết cấu trúc

## Business Goals

```text
17 Business Goals
```

## Business Domains

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

## Business Requirements

```text
18 Business Requirements
```

## Business Processes

```text
BP01 Quản lý tài khoản
BP02 Đặt & quản lý chuyến
BP03 Điều phối tài xế
BP04 Thực hiện chuyến
BP05 Tính cước & thanh toán
BP06 Hậu chuyến
BP07 Vận hành & báo cáo
```

## Nguyên tắc phân rã

```text
Business Goal
      ↓
Business Domain
      ↓
Business Requirement
      ↓
Business Process
      ↓
Functional Requirement
      ↓
Use Case
      ↓
Design / API / Code
```

> **Lưu ý:** Không code trực tiếp từ Business Process.
> Business Process chỉ mô tả luồng nghiệp vụ ở mức tổng quát.
> Các chi tiết như API, database, timeout, retry, provider, notification channel...
> sẽ được phân tích ở các bước thiết kế và phát triển tiếp theo.
