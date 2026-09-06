# CAB System

> Hệ thống nền tảng đặt xe trực tuyến CAB

---

# 1. Stakeholders

| Stakeholder | Vai trò | Nhiệm vụ |
|---|---|---|
| Ban giám đốc | Sponsor / Decision Maker | Định hướng, phê duyệt mục tiêu, phạm vi và ngân sách |
| Product Owner | Product Owner | Xác định ưu tiên và quản lý sản phẩm |
| Business Analyst | Business Analyst | Thu thập, phân tích và làm rõ yêu cầu |
| Khách hàng | End User | Đăng ký, đặt xe, theo dõi, thanh toán và đánh giá |
| Tài xế | End User | Nhận chuyến, cập nhật trạng thái và hoàn thành chuyến |
| Nhân viên vận hành | Operations | Giám sát chuyến, tài xế và xử lý sự cố |
| Kế toán / Tài chính | Financial | Quản lý doanh thu, giao dịch và đối soát |
| Quản trị hệ thống | System Administrator | Quản lý tài khoản, quyền và cấu hình |
| Đội phát triển | Development Team | Phân tích, thiết kế, lập trình và kiểm thử |
| DevOps / IT | Technical Operations | Hạ tầng, triển khai, monitoring và scaling |
| Security / Compliance | Security | Bảo mật, phân quyền và audit |
| Nhà cung cấp thanh toán | External Provider | Xử lý thanh toán điện tử |
| Nhà cung cấp bản đồ | External Provider | Cung cấp vị trí, khoảng cách và định tuyến |
| Nhà cung cấp thông báo | External Provider | Gửi SMS, Email và Push Notification |

---

# 2. Stakeholder Influence Matrix

| Stakeholder | Ảnh hưởng | Quan tâm | Chiến lược |
|---|---|---|---|
| Ban giám đốc | Cao | Cao | Quản lý chặt chẽ |
| Product Owner | Cao | Cao | Quản lý chặt chẽ |
| Quản lý vận hành | Cao | Cao | Quản lý chặt chẽ |
| Business Analyst | Cao | Cao | Quản lý chặt chẽ |
| Nhân viên vận hành | Cao | Cao | Quản lý chặt chẽ |
| Kế toán / Tài chính | Cao | Cao | Quản lý chặt chẽ |
| Security / Compliance | Cao | Cao | Quản lý chặt chẽ |
| DevOps / IT | Cao | Cao | Phối hợp thường xuyên |
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
| BG04 | Giảm thời gian tìm tài xế | Tự động chuyển sang tài xế khác khi từ chối hoặc timeout |
| BG05 | Quản lý tài xế tập trung | Quản lý hồ sơ, phương tiện, trạng thái và vị trí |
| BG06 | Minh bạch trạng thái chuyến | Theo dõi chuyến từ lúc đặt đến khi hoàn thành |
| BG07 | Tự động hóa tính cước và thanh toán | Hỗ trợ tính cước và nhiều phương thức thanh toán |
| BG08 | Bảo vệ thông tin thanh toán | Không lưu trực tiếp dữ liệu thanh toán nhạy cảm |
| BG09 | Thông báo đa kênh | Gửi thông báo cho khách hàng và tài xế |
| BG10 | Nâng cao hiệu quả vận hành | Cung cấp công cụ quản lý và xử lý sự cố |
| BG11 | Báo cáo quản trị | Cung cấp dữ liệu về chuyến, doanh thu và hiệu quả |
| BG12 | Khả năng mở rộng | Hỗ trợ lượng lớn khách hàng và tài xế |
| BG13 | Tính ổn định | Lỗi một thành phần không làm dừng toàn hệ thống |
| BG14 | Bảo mật | Xác thực, phân quyền và bảo vệ dữ liệu |
| BG15 | Audit | Lưu vết các thao tác quan trọng |
| BG16 | Linh hoạt phát triển | Dễ bổ sung dịch vụ, thanh toán và thông báo |
| BG17 | Chuẩn hóa nghiệp vụ | Làm rõ tính cước, dispatch, timeout, hủy và retry |

---

# 4. Business Boundary

## 4.1 Business Domains

| Mã | Business Domain | Giới hạn quản lý |
|---|---|---|
| B01 | User Management | Tài khoản, danh tính và quyền người dùng |
| B02 | Driver & Vehicle Management | Tài xế, phương tiện, trạng thái và vị trí |
| B03 | Booking & Trip Management | Yêu cầu đặt xe và vòng đời chuyến |
| B04 | Driver Dispatch | Tìm kiếm và phân công tài xế |
| B05 | Fare & Payment | Tính cước và thanh toán |
| B06 | Notification | Gửi và quản lý thông báo |
| B07 | Operations Management | Giám sát và xử lý vận hành |
| B08 | Reporting & Analytics | Báo cáo và phân tích dữ liệu |

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

**Không quản lý:** Đặt xe, điều phối, tính cước và thanh toán.

---

## 4.3 B02 - Driver & Vehicle Management

**Phạm vi:** Quản lý tài xế, phương tiện và trạng thái hoạt động.

| Mã | Business con |
|---|---|
| B02.01 | Hồ sơ tài xế |
| B02.02 | Quản lý phương tiện |
| B02.03 | Trạng thái tài xế |
| B02.04 | Vị trí tài xế |
| B02.05 | Lịch sử hoạt động |

**Không quản lý:** Quyết định phân công, tính cước và thanh toán.

---

## 4.4 B03 - Booking & Trip Management

**Phạm vi:** Quản lý vòng đời yêu cầu đặt xe và chuyến đi.

| Mã | Business con |
|---|---|
| B03.01 | Tạo yêu cầu đặt xe |
| B03.02 | Quản lý yêu cầu |
| B03.03 | Quản lý chuyến |
| B03.04 | Cập nhật trạng thái |
| B03.05 | Hủy chuyến |
| B03.06 | Lịch sử chuyến |

---

## 4.5 B04 - Driver Dispatch

**Phạm vi:** Tìm kiếm, lựa chọn và phân công tài xế.

| Mã | Business con |
|---|---|
| B04.01 | Tìm tài xế |
| B04.02 | Lọc tài xế |
| B04.03 | Xếp hạng tài xế |
| B04.04 | Gửi yêu cầu nhận chuyến |
| B04.05 | Xử lý timeout |
| B04.06 | Re-dispatch |
| B04.07 | Không tìm được tài xế |

---

## 4.6 B05 - Fare & Payment

**Phạm vi:** Tính số tiền phải trả và xử lý thanh toán.

| Mã | Business con |
|---|---|
| B05.01 | Tính cước |
| B05.02 | Phương thức thanh toán |
| B05.03 | Tạo giao dịch |
| B05.04 | Thanh toán điện tử |
| B05.05 | Xử lý thanh toán thất bại |
| B05.06 | Đối soát |
| B05.07 | Lịch sử thanh toán |

---

## 4.7 B06 - Notification

**Phạm vi:** Quản lý và gửi thông báo.

| Mã | Business con |
|---|---|
| B06.01 | Thông báo đặt xe |
| B06.02 | Thông báo phân công |
| B06.03 | Thông báo tài xế đến |
| B06.04 | Thông báo hoàn thành |
| B06.05 | Thông báo thanh toán |
| B06.06 | Quản lý kênh thông báo |

**Kênh:** Push Notification, SMS, Email.

---

## 4.8 B07 - Operations Management

**Phạm vi:** Giám sát và xử lý hoạt động vận hành.

| Mã | Business con |
|---|---|
| B07.01 | Giám sát chuyến |
| B07.02 | Giám sát tài xế |
| B07.03 | Hỗ trợ khách hàng |
| B07.04 | Quản lý tài xế |
| B07.05 | Xử lý sự cố |
| B07.06 | Hỗ trợ thanh toán |
| B07.07 | Quản lý quyền nhân viên |

---

## 4.9 B08 - Reporting & Analytics

**Phạm vi:** Tổng hợp dữ liệu phục vụ quản trị và ra quyết định.

| Mã | Business con |
|---|---|
| B08.01 | Báo cáo chuyến |
| B08.02 | Báo cáo doanh thu |
| B08.03 | Báo cáo hoàn thành |
| B08.04 | Báo cáo hủy |
| B08.05 | Báo cáo hiệu quả tài xế |
| B08.06 | Dashboard KPI |

---

# 5. Business Requirements

## B01 - User Management

### BR01 - Quản lý người dùng
Hệ thống phải hỗ trợ đăng ký, đăng nhập, cập nhật thông tin và quản lý quyền người dùng.

---

## B02 - Driver & Vehicle Management

### BR02 - Quản lý tài xế và phương tiện
Hệ thống phải hỗ trợ quản lý hồ sơ tài xế, phương tiện và trạng thái sẵn sàng nhận chuyến.

### BR03 - Quản lý vị trí tài xế
Hệ thống phải quản lý vị trí tài xế để phục vụ điều phối và theo dõi chuyến.

---

## B03 - Booking & Trip Management

### BR04 - Đặt xe
Hệ thống phải cho phép khách hàng tạo yêu cầu đặt xe với điểm đón, điểm đến và loại xe.

### BR05 - Quản lý chuyến đi
Hệ thống phải quản lý vòng đời chuyến đi từ khi tạo yêu cầu đến khi hoàn thành hoặc hủy.

### BR06 - Theo dõi chuyến
Hệ thống phải cho phép khách hàng và nhân viên vận hành theo dõi trạng thái và thông tin chuyến.

---

## B04 - Driver Dispatch

### BR07 - Tự động tìm và phân công tài xế
Hệ thống phải tự động tìm và ưu tiên tài xế phù hợp dựa trên vị trí, trạng thái và tiêu chí vận hành.

### BR08 - Xử lý tài xế từ chối hoặc không phản hồi
Hệ thống phải tiếp tục tìm tài xế khác khi tài xế không phản hồi hoặc từ chối chuyến.

### BR09 - Không tìm được tài xế
Hệ thống phải thông báo rõ ràng cho khách hàng khi không tìm được tài xế.

---

## B05 - Fare & Payment

### BR10 - Tính cước
Hệ thống phải xác định số tiền khách hàng phải trả theo chính sách tính cước của doanh nghiệp.

### BR11 - Thanh toán
Hệ thống phải hỗ trợ thanh toán tiền mặt và thanh toán điện tử thông qua nhà cung cấp bên ngoài.

### BR12 - Thanh toán thất bại
Hệ thống phải thông báo kết quả và hỗ trợ xử lý lại giao dịch khi thanh toán thất bại.

---

## B06 - Notification

### BR13 - Thông báo
Hệ thống phải thông báo cho khách hàng và tài xế về các sự kiện quan trọng của chuyến đi và thanh toán.

---

## B07 - Operations Management

### BR14 - Quản lý vận hành
Hệ thống phải cung cấp chức năng để nhân viên vận hành giám sát, tra cứu và xử lý các trường hợp bất thường.

---

## B08 - Reporting & Analytics

### BR15 - Báo cáo
Hệ thống phải cung cấp báo cáo về chuyến đi, doanh thu, tỷ lệ hoàn thành, tỷ lệ hủy và hiệu quả tài xế.

---

## Cross-cutting Requirements

### BR16 - Bảo mật và kiểm soát truy cập
Hệ thống phải bảo vệ dữ liệu và kiểm soát quyền truy cập đối với các chức năng nhạy cảm.

### BR17 - Khả năng mở rộng
Hệ thống phải cho phép mở rộng quy mô, bổ sung dịch vụ, phương thức thanh toán và kênh thông báo mà hạn chế ảnh hưởng đến hệ thống hiện tại.

### BR18 - Audit
Hệ thống phải lưu vết các thao tác quan trọng để phục vụ kiểm tra và xử lý sự cố.

---

# CAB System - Business Process

## BP01 - Quản lý tài khoản
**BR:** BR01, BR16

1. Đăng ký / đăng nhập
2. Xác thực người dùng
3. Quản lý thông tin và quyền truy cập

---

## BP02 - Đặt xe
**BR:** BR04, BR06, BR13

1. Khách hàng nhập thông tin chuyến và gửi yêu cầu
2. Hệ thống tiếp nhận và tạo chuyến
3. Thông báo trạng thái yêu cầu

---

## BP03 - Điều phối tài xế
**BR:** BR02, BR03, BR07, BR08, BR09, BR13

1. Hệ thống tìm và ưu tiên tài xế phù hợp
2. Gửi yêu cầu nhận chuyến
3. Tài xế nhận / từ chối / không phản hồi
4. Nếu không nhận, hệ thống tìm tài xế khác
5. Thông báo kết quả cho khách hàng

---

## BP04 - Thực hiện chuyến
**BR:** BR05, BR06, BR13

1. Tài xế nhận và thực hiện chuyến
2. Cập nhật trạng thái và vị trí
3. Hoàn thành hoặc hủy chuyến
4. Thông báo trạng thái cho khách hàng

---

## BP05 - Tính cước & thanh toán
**BR:** BR10, BR11, BR12, BR13

1. Hệ thống tính cước sau khi chuyến hoàn thành
2. Khách hàng chọn phương thức thanh toán
3. Hệ thống xử lý và ghi nhận thanh toán
4. Thông báo kết quả
5. Xử lý lại nếu thanh toán thất bại

---

## BP06 - Lịch sử & đánh giá
**BR:** BR05, BR06

1. Khách hàng xem lịch sử và chi tiết chuyến
2. Khách hàng xem cước
3. Khách hàng đánh giá tài xế
4. Hệ thống lưu kết quả

---

## BP07 - Vận hành & báo cáo
**BR:** BR14, BR15, BR16, BR18

1. Nhân viên quản lý và giám sát hệ thống
2. Tra cứu và xử lý chuyến / giao dịch bất thường
3. Hệ thống ghi nhận Audit Log
4. Hệ thống tổng hợp và cung cấp báo cáo

---

## BP08 - Mở rộng hệ thống
**BR:** BR17

1. Quản lý các thành phần độc lập
2. Bổ sung dịch vụ mới
3. Bổ sung phương thức thanh toán
4. Bổ sung kênh / nhà cung cấp thông báo

