
# CAB System

## Stakeholders

| Stakeholder | Vai trò | Nhiệm vụ |
|---|---|---|
| Ban giám đốc | Sponsor / Decision Maker | Định hướng, phê duyệt ngân sách, phạm vi và mục tiêu |
| Business Analyst | Phân tích nghiệp vụ | Thu thập, phân tích và làm rõ yêu cầu |
| Khách hàng | End User | Đăng ký, đặt xe, theo dõi chuyến, thanh toán, đánh giá |
| Tài xế | End User | Nhận chuyến, cập nhật trạng thái, hoàn thành chuyến |
| Nhân viên vận hành | Operations | Quản lý khách hàng, tài xế, chuyến đi và xử lý sự cố |
| Kế toán / Tài chính | Financial | Quản lý doanh thu, giao dịch và đối soát |
| Quản trị hệ thống | System Administrator | Quản lý tài khoản, phân quyền và cấu hình |
| Đội phát triển | Development Team | Thiết kế, lập trình, kiểm thử và bảo trì |
| DevOps / IT | Technical Operations | Hạ tầng, triển khai, monitoring và scaling |
| Security / Compliance | Security | Bảo vệ dữ liệu, phân quyền và audit |
| Nhà cung cấp thanh toán | External Provider | Xử lý thanh toán điện tử |
| Nhà cung cấp bản đồ | External Provider | Cung cấp vị trí, khoảng cách và định tuyến |
| Nhà cung cấp thông báo | External Provider | Gửi SMS, Email, Push Notification |

## Ma trận mức độ ảnh hưởng

| Stakeholder | Ảnh hưởng | Quan tâm | Chiến lược |
|---|---|---|---|
| Ban giám đốc | Cao | Cao | Quản lý chặt chẽ |
| Product Owner | Cao | Cao | Quản lý chặt chẽ |
| Quản lý vận hành | Cao | Cao | Quản lý chặt chẽ |
| Business Analyst | Cao | Cao | Quản lý chặt chẽ |
| Nhân viên vận hành | Cao | Cao | Quản lý chặt chẽ |
| Khách hàng | Trung bình | Cao | Tham khảo và cập nhật |
| Tài xế | Trung bình | Cao | Tham khảo và cập nhật |
| Kế toán / Tài chính | Cao | Cao | Quản lý chặt chẽ |
| Security / Compliance | Cao | Cao | Quản lý chặt chẽ |
| Đội phát triển | Trung bình | Cao | Phối hợp thường xuyên |
| DevOps / IT | Cao | Cao | Phối hợp thường xuyên |
| Nhà cung cấp thanh toán | Trung bình | Trung bình | Duy trì hài lòng |
| Nhà cung cấp bản đồ | Trung bình | Trung bình | Duy trì hài lòng |
| Nhà cung cấp thông báo | Thấp - Trung bình | Trung bình | Theo dõi |

# Business Goals

| Mã BG | Mục tiêu nghiệp vụ | Mô tả |
|---|---|---|
| BG01 | Xây dựng nền tảng CAB đặt xe trực tuyến | Xây dựng nền tảng đặt xe tập trung, thay thế phương thức đặt xe thủ công và ứng dụng hiện tại. |
| BG02 | Nâng cao trải nghiệm khách hàng | Cho phép khách hàng đăng ký, đăng nhập, đặt xe, theo dõi chuyến, xem lịch sử, thanh toán và đánh giá tài xế. |
| BG03 | Tự động hóa quy trình phân công tài xế | Tự động tìm kiếm và lựa chọn tài xế phù hợp dựa trên vị trí, trạng thái sẵn sàng và các tiêu chí vận hành. |
| BG04 | Rút ngắn thời gian tìm và phân công tài xế | Tự động tìm tài xế khác khi tài xế từ chối hoặc không phản hồi. |
| BG05 | Quản lý tập trung hoạt động tài xế | Quản lý hồ sơ, phương tiện, trạng thái hoạt động và vị trí tài xế. |
| BG06 | Minh bạch hóa trạng thái chuyến đi | Cho phép theo dõi trạng thái chuyến từ lúc tạo yêu cầu đến khi hoàn thành. |
| BG07 | Tự động hóa tính cước và thanh toán | Tính cước và hỗ trợ thanh toán tiền mặt hoặc điện tử. |
| BG08 | Đảm bảo an toàn thông tin thanh toán | Không lưu trực tiếp thông tin nhạy cảm của thẻ hoặc tài khoản thanh toán. |
| BG09 | Xây dựng hệ thống thông báo đa kênh | Gửi thông báo cho khách hàng và tài xế, đồng thời hỗ trợ mở rộng thêm kênh trong tương lai. |
| BG10 | Nâng cao hiệu quả vận hành | Cung cấp giao diện quản trị để quản lý khách hàng, tài xế, phương tiện và chuyến đi. |
| BG11 | Cung cấp dữ liệu và báo cáo quản trị | Báo cáo số chuyến, doanh thu, tỷ lệ hoàn thành, tỷ lệ hủy và hiệu quả tài xế. |
| BG12 | Đảm bảo khả năng mở rộng hệ thống | Hỗ trợ số lượng lớn khách hàng, tài xế và mở rộng độc lập các thành phần. |
| BG13 | Đảm bảo tính ổn định và sẵn sàng | Lỗi thanh toán hoặc thông báo không làm ngừng toàn bộ hệ thống. |
| BG14 | Đảm bảo bảo mật và kiểm soát truy cập | Xác thực, phân quyền và bảo vệ dữ liệu cá nhân, vị trí và giao dịch. |
| BG15 | Đảm bảo khả năng kiểm tra và truy vết | Lưu vết các thao tác quan trọng để kiểm tra và điều tra sự cố. |
| BG16 | Tạo nền tảng linh hoạt cho phát triển tương lai | Cho phép bổ sung dịch vụ, phương thức thanh toán và nhà cung cấp mới. |
| BG17 | Chuẩn hóa và làm rõ chính sách nghiệp vụ | Làm rõ tính cước, ưu tiên tài xế, timeout, hủy chuyến, retry thanh toán và lưu trữ dữ liệu. |
# CAB System - Modules

## 1. Tổng quan

Hệ thống CAB được chia thành các module dựa trên trách nhiệm nghiệp vụ.
Mỗi module có phạm vi quản lý riêng và có thể phát triển tương đối độc lập.

---

## 2. Danh sách Module

| Mã | Module | Loại |
|---|---|---|
| M01 | Quản lý tài khoản & người dùng | Supporting |
| M02 | Quản lý tài xế & phương tiện | Core |
| M03 | Đặt xe & quản lý chuyến đi | Core Business |
| M04 | Điều phối & tìm tài xế | Core Business |
| M05 | Định vị & theo dõi chuyến | Core |
| M06 | Tính cước & thanh toán | Core Business |
| M07 | Thông báo | Supporting |
| M08 | Đánh giá & phản hồi | Supporting |
| M09 | Quản lý vận hành | Supporting |
| M10 | Quản trị & phân quyền | Supporting |
| M11 | Báo cáo & thống kê | Supporting |
| M12 | Bảo mật & Audit | Supporting |

---

# 3. M01 - Quản lý tài khoản & người dùng

### Phạm vi

Quản lý tài khoản, danh tính và quyền truy cập của người dùng CAB.

### Chức năng

- Đăng ký tài khoản
- Đăng nhập / đăng xuất
- Xác thực người dùng
- Cập nhật thông tin cá nhân
- Quản lý trạng thái tài khoản
- Phân quyền người dùng

### Actor

- Khách hàng
- Tài xế
- Nhân viên vận hành
- Quản trị viên

---

# 4. M02 - Quản lý tài xế & phương tiện

### Phạm vi

Quản lý hồ sơ tài xế, phương tiện và trạng thái hoạt động.

### Chức năng

- Tạo tài khoản tài xế
- Quản lý hồ sơ tài xế
- Quản lý phương tiện
- Quản lý loại xe
- Cập nhật trạng thái tài xế
- Bật/tắt trạng thái sẵn sàng
- Cập nhật vị trí tài xế
- Xem lịch sử hoạt động

### Actor

- Tài xế
- Nhân viên vận hành
- Quản trị viên

---

# 5. M03 - Đặt xe & quản lý chuyến đi

### Phạm vi

Quản lý vòng đời yêu cầu đặt xe và chuyến đi từ khi khách hàng tạo yêu cầu đến khi chuyến hoàn thành hoặc bị hủy.

### Chức năng

- Nhập điểm đón
- Nhập điểm đến
- Chọn loại xe
- Tạo yêu cầu đặt xe
- Tiếp nhận yêu cầu
- Theo dõi trạng thái chuyến
- Cập nhật trạng thái chuyến
- Hủy chuyến
- Hoàn thành chuyến
- Xem lịch sử chuyến

### Trạng thái chuyến

```text
NEW
 ↓
SEARCHING_DRIVER
 ↓
DRIVER_ASSIGNED
 ↓
DRIVER_ARRIVING
 ↓
DRIVER_ARRIVED
 ↓
PASSENGER_PICKED_UP
 ↓
IN_TRIP
 ↓
COMPLETED


# Business Boundary - CAB System

## 1. Tổng quan

Hệ thống CAB được phân chia thành các Business Domain dựa trên trách nhiệm nghiệp vụ. 
Mỗi Business có một phạm vi quản lý riêng và chịu trách nhiệm cho một nhóm nghiệp vụ cụ thể.

---

## 2. Business Domain

| Mã | Business | Giới hạn quản lý |
|---|---|---|
| B01 | User Management | Quản lý danh tính, tài khoản và quyền truy cập người dùng |
| B02 | Driver & Vehicle Management | Quản lý hồ sơ, phương tiện, trạng thái và vị trí tài xế |
| B03 | Booking & Trip Management | Quản lý vòng đời yêu cầu đặt xe và chuyến đi |
| B04 | Driver Dispatch | Tìm kiếm, lựa chọn và phân công tài xế |
| B05 | Fare & Payment | Tính cước và quản lý quá trình thanh toán |
| B06 | Notification | Quản lý và gửi thông báo đến khách hàng và tài xế |
| B07 | Operations Management | Giám sát, hỗ trợ và xử lý các vấn đề vận hành |
| B08 | Reporting & Analytics | Tổng hợp dữ liệu và cung cấp báo cáo quản trị |

---

# 3. B01 - User Management

### Giới hạn quản lý

Quản lý danh tính và tài khoản của người sử dụng hệ thống CAB.

### Business con

| Mã | Business con | Phạm vi |
|---|---|---|
| B01.01 | Đăng ký tài khoản | Tạo tài khoản người dùng |
| B01.02 | Xác thực & đăng nhập | Xác thực người dùng và đăng nhập |
| B01.03 | Quản lý hồ sơ | Cập nhật thông tin cá nhân |
| B01.04 | Phân quyền | Xác định quyền của từng nhóm người dùng |
| B01.05 | Trạng thái tài khoản | Active, Locked, Suspended |

### Không quản lý

- Đặt chuyến
- Tìm tài xế
- Tính cước
- Thanh toán

---

# 4. B02 - Driver & Vehicle Management

### Giới hạn quản lý

Quản lý thông tin, năng lực và trạng thái hoạt động của tài xế và phương tiện.

### Business con

| Mã | Business con | Phạm vi |
|---|---|---|
| B02.01 | Hồ sơ tài xế | Thông tin tài xế |
| B02.02 | Quản lý phương tiện | Thông tin xe và loại xe |
| B02.03 | Trạng thái tài xế | Online, Offline, Available, Busy |
| B02.04 | Vị trí tài xế | Lưu và cập nhật vị trí |
| B02.05 | Lịch sử hoạt động | Lịch sử hoạt động của tài xế |
| B02.06 | Đánh giá tài xế | Thông tin đánh giá từ khách hàng |

### Không quản lý

- Quyết định tài xế nhận chuyến
- Tính cước chuyến
- Xử lý thanh toán

---

# 5. B03 - Booking & Trip Management

### Giới hạn quản lý

Quản lý vòng đời của yêu cầu đặt xe và chuyến đi từ khi khách hàng tạo yêu cầu đến khi chuyến hoàn thành hoặc bị hủy.

### Business con

| Mã | Business con | Phạm vi |
|---|---|---|
| B03.01 | Tạo yêu cầu đặt xe | Điểm đón, điểm đến, loại xe |
| B03.02 | Quản lý yêu cầu | Created, Searching, Assigned |
| B03.03 | Quản lý chuyến đi | Quản lý vòng đời Trip |
| B03.04 | Cập nhật trạng thái | Arrived, Picked Up, In Trip, Completed |
| B03.05 | Hủy chuyến | Xử lý các trường hợp hủy |
| B03.06 | Lịch sử chuyến | Tra cứu các chuyến đã thực hiện |

### Không quản lý

- Thuật toán lựa chọn tài xế
- Tính tiền
- Gửi thông báo

---

# 6. B04 - Driver Dispatch

### Giới hạn quản lý

Tìm kiếm, đánh giá, lựa chọn và phân công tài xế cho một yêu cầu đặt xe.

### Business con

| Mã | Business con | Phạm vi |
|---|---|---|
| B04.01 | Tìm tài xế | Tìm tài xế phù hợp |
| B04.02 | Lọc tài xế | Theo vị trí, trạng thái, loại xe |
| B04.03 | Xếp hạng tài xế | Ưu tiên tài xế phù hợp |
| B04.04 | Gửi yêu cầu nhận chuyến | Gửi offer cho tài xế |
| B04.05 | Timeout | Xử lý tài xế không phản hồi |
| B04.06 | Re-dispatch | Tìm tài xế tiếp theo |
| B04.07 | Không tìm được tài xế | Thông báo không có tài xế |

### Không quản lý

- Tạo yêu cầu đặt xe
- Quản lý trạng thái Trip
- Tính cước

---

# 7. B05 - Fare & Payment

### Giới hạn quản lý

Xác định số tiền khách hàng phải trả và quản lý quá trình thanh toán.

### Business con

| Mã | Business con | Phạm vi |
|---|---|---|
| B05.01 | Tính cước | Xác định giá chuyến |
| B05.02 | Phương thức thanh toán | Cash / Electronic |
| B05.03 | Tạo giao dịch | Tạo Payment Transaction |
| B05.04 | Thanh toán điện tử | Tích hợp Payment Provider |
| B05.05 | Xử lý thất bại | Retry / Failed |
| B05.06 | Đối soát | Kiểm tra giao dịch |
| B05.07 | Lịch sử thanh toán | Tra cứu giao dịch |

### Không quản lý

- Điều phối tài xế
- Cập nhật trạng thái chuyến
- Quản lý tài khoản người dùng

---

# 8. B06 - Notification

### Giới hạn quản lý

Quản lý việc tạo và gửi thông báo nghiệp vụ đến khách hàng và tài xế.

### Business con

| Mã | Business con | Phạm vi |
|---|---|---|
| B06.01 | Thông báo đặt xe | Yêu cầu được tiếp nhận |
| B06.02 | Thông báo phân công | Tài xế nhận chuyến |
| B06.03 | Thông báo tài xế đến | Driver Arrived |
| B06.04 | Thông báo hoàn thành | Trip Completed |
| B06.05 | Thông báo thanh toán | Payment Success / Failed |
| B06.06 | Quản lý kênh | Push, SMS, Email |

### Nguyên tắc

Notification là business hỗ trợ.

Nếu dịch vụ thông báo gặp lỗi thì các nghiệp vụ chính như đặt xe và chuyến đi vẫn phải tiếp tục hoạt động.

---

# 9. B07 - Operations Management

### Giới hạn quản lý

Giám sát, hỗ trợ và xử lý các vấn đề phát sinh trong quá trình vận hành hệ thống CAB.

### Business con

| Mã | Business con | Phạm vi |
|---|---|---|
| B07.01 | Giám sát chuyến | Theo dõi các chuyến đang hoạt động |
| B07.02 | Giám sát tài xế | Kiểm tra trạng thái tài xế |
| B07.03 | Hỗ trợ khách hàng | Tra cứu và hỗ trợ khách |
| B07.04 | Quản lý tài xế | Hỗ trợ và quản lý thông tin tài xế |
| B07.05 | Xử lý sự cố | Xử lý Trip lỗi hoặc bất thường |
| B07.06 | Hỗ trợ thanh toán | Tra cứu giao dịch |
| B07.07 | Quản lý quyền nhân viên | Kiểm soát quyền thao tác |

---

# 10. B08 - Reporting & Analytics

### Giới hạn quản lý

Tổng hợp dữ liệu nghiệp vụ để phục vụ quản trị, theo dõi KPI và ra quyết định.

### Business con

| Mã | Business con | Phạm vi |
|---|---|---|
| B08.01 | Báo cáo chuyến | Số lượng chuyến |
| B08.02 | Báo cáo doanh thu | Revenue |
| B08.03 | Báo cáo hoàn thành | Completion Rate |
| B08.04 | Báo cáo hủy | Cancellation Rate |
| B08.05 | Báo cáo tài xế | Driver Performance |
| B08.06 | Dashboard | KPI vận hành |

---

# 11. Business Boundary Diagram

```mermaid
flowchart TB

    CAB["CAB PLATFORM"]

    B01["B01<br/>User Management"]
    B02["B02<br/>Driver & Vehicle"]
    B03["B03<br/>Booking & Trip"]
    B04["B04<br/>Driver Dispatch"]
    B05["B05<br/>Fare & Payment"]
    B06["B06<br/>Notification"]
    B07["B07<br/>Operations"]
    B08["B08<br/>Reporting"]

    CAB --> B01
    CAB --> B02
    CAB --> B03
    CAB --> B04
    CAB --> B05
    CAB --> B06
    CAB --> B07
    CAB --> B08

    B03 --> B04
    B04 --> B02
    B03 --> B05
    B03 --> B06
    B05 --> B06
    B07 --> B03
    B07 --> B02

    B03 --> B08
    B04 --> B08
    B05 --> B08
    B02 --> B08


