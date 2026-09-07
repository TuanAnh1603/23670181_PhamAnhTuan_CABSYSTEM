# 🚕 HỆ THỐNG CAB - NỀN TẢNG ĐẶT XE TRỰC TUYẾN

---

## 1. CÁC BÊN LIÊN QUAN

| Bên liên quan | Vai trò | Nhiệm vụ chính |
|---|---|---|
| Ban giám đốc & PO | Quản lý | Định hướng, quản lý ngân sách và ưu tiên sản phẩm |
| Đội phát triển & Hạ tầng | Kỹ thuật | Thiết kế, lập trình, kiểm thử và triển khai |
| Khách hàng & Tài xế | Người dùng | Đặt xe, thực hiện chuyến đi, thanh toán, đánh giá |
| Vận hành & Kế toán | Nội bộ | Giám sát chuyến, xử lý sự cố, quản lý doanh thu |
| Bên thứ ba | Đối tác | Cung cấp Cổng thanh toán, Maps API, Push Notification |

---

## 2. MA TRẬN MỨC ĐỘ ẢNH HƯỞNG

| Bên liên quan | Mức độ | Chiến lược |
|---|---|---|
| Ban giám đốc, PO, Đội Kỹ thuật, Vận hành | Cao / Cao | Quản lý chặt chẽ & Phối hợp trực tiếp |
| Khách hàng, Tài xế | Trung bình / Cao | Thu thập phản hồi & Cập nhật tính năng |
| Đối tác bên thứ ba (Maps, Payment, Noti) | Trung bình / Trung bình | Duy trì kết nối API ổn định |

---

## 3. MỤC TIÊU NGHIỆP VỤ

| Mã | Mục tiêu nghiệp vụ ngắn gọn |
|---|---|
| BG01 | Xây dựng hệ thống đặt xe trực tuyến tự động, ổn định |
| BG02 | Tự động hóa điều phối tài xế, tính cước & thanh toán |
| BG03 | Giảm thời gian chờ, nâng cao trải nghiệm khách hàng |
| BG04 | Tự động hóa quản lý vận hành, báo cáo & lưu vết |

---

## 4. PHẠM VI NGHIỆP VỤ

| Mã | Miền nghiệp vụ | Phạm vi cô đọng |
|---|---|---|
| B01 | User & Auth | Đăng ký, đăng nhập, phân quyền người dùng |
| B02 | Driver & GPS | Hồ sơ tài xế, quản lý xe và định vị GPS |
| B03 | Booking & Trip | Tạo đặt xe, theo dõi và quản lý trạng thái chuyến |
| B04 | Dispatching | Thuật toán tự động tìm và gán tài xế |
| B05 | Billing & Payment | Tính tiền cước và xử lý thanh toán đa phương thức |
| B06 | Notification & Ops | Gửi thông báo, báo cáo và lưu nhật ký hệ thống |

---

## 5. YÊU CẦU NGHIỆP VỤ

| Mã | Yêu cầu nghiệp vụ cốt lõi |
|---|---|
| BR01 | Quản lý tài khoản, xác thực OTP/Password và phân quyền |
| BR02 | Quản lý thông tin tài xế, xe và cập nhật tọa độ GPS realtime |
| BR03 | Cho phép đặt xe, tự động khớp tài xế phù hợp gần nhất |
| BR04 | Quản lý vòng đời chuyến đi (Tạo -> Đón -> Di chuyển -> Hoàn thành/Hủy) |
| BR05 | Tự động điều phối lại nếu tài xế từ chối / hết thời gian chờ (timeout) |
| BR06 | Tự động tính cước và thanh toán (Tiền mặt / Ví điện tử) |
| BR07 | Gửi thông báo sự kiện chuyến đi và cho phép đánh giá sao |
| BR08 | Cung cấp công cụ giám sát vận hành, xuất báo cáo và lưu Audit Log |

---

## 6. QUY TRÌNH NGHIỆP VỤ

| Mã | Quy trình | Các bước tinh gọn |
|---|---|---|
| QT01 | Quản lý tài khoản | Đăng nhập/Đăng ký → Xác thực → Phân quyền |
| QT02 | Đặt & Quản lý chuyến | Đặt xe → Theo dõi realtime → Hoàn thành / Hủy |
| QT03 | Điều phối tài xế | Quét vị trí → Gửi yêu cầu → Nhận / Thử lại tài xế khác |
| QT04 | Thực hiện chuyến | Nhận chuyến → Đón khách → Di chuyển → Kết thúc |
| QT05 | Tính cước & Thanh toán | Tính tiền → Thanh toán (Cash/App) → Xác nhận |
| QT06 | Xử lý sau chuyến | Hiển thị hóa đơn → Đánh giá chuyến đi |
| QT07 | Vận hành & Báo cáo | Giám sát / Can thiệp lỗi → Ghi log → Báo cáo |

---

## 7. YÊU CẦU CHỨC NĂNG

| Mã | Yêu cầu chức năng | BR liên quan |
|---|---|---|
| FR01 | Đăng ký, đăng nhập, phân quyền (Auth Module) | BR01 |
| FR02 | Quản lý hồ sơ tài xế, xe & cập nhật vị trí GPS | BR02 |
| FR03 | Đặt xe, tính giá tạm tính & quản lý trạng thái chuyến | BR03, BR04 |
| FR04 | Thuật toán tự động tìm tài xế & xử lý điều phối lại | BR03, BR05 |
| FR05 | Tính cước thực tế & Tích hợp Cổng thanh toán | BR06 |
| FR06 | Gửi Push Notification / SMS & Đánh giá sao | BR07 |
| FR07 | Dashboard vận hành, Xuất báo cáo & System Log | BR08 |

---

## 8. VAI TRÒ HỆ THỐNG

| Vai trò | Nhiệm vụ chính trong code |
|---|---|
| Customer | Gọi API đặt xe, theo dõi vị trí, thanh toán, đánh giá |
| Driver | Gọi API nhận chuyến, bật/tắt online, cập nhật GPS |
| Admin / Ops | Quản trị dữ liệu, xem Dashboard, can thiệp chuyến lỗi |
| System (Backend) | Chạy Job điều phối, tính cước, push notification |

---

## 9. NGOẠI LỆ

| Mã | Ngoại lệ | Xử lý đơn giản |
|---|---|---|
| EX01 | Không tìm thấy / Từ chối xe | Chuyển tài xế tiếp theo; nếu hết xe thì báo khách |
| EX02 | Khách / Tài xế hủy chuyến | Cập nhật trạng thái `CANCELLED`, ghi lý do |
| EX03 | Thanh toán App thất bại | Báo lỗi, cho phép thử lại hoặc chuyển sang Tiền mặt |
| EX04 | Lỗi mạng / Lỗi hệ thống | Retry kết nối hoặc ghi log lỗi vào DB |

---

## 10. YÊU CẦU PHI CHỨC NĂNG

| Mã | Yêu cầu kỹ thuật |
|---|---|
| NFR01 | Response API `< 200ms`, xử lý điều phối xe `< 3s` |
| NFR02 | Hệ thống chạy ổn định 99.9%, mã hóa thông tin nhạy cảm |
| NFR03 | Dễ mở rộng dịch vụ mới và dễ bảo trì code |

---

## 11. THỰC THỂ DỮ LIỆU

> Gom gọn còn **6 bảng Database cốt lõi**:

| Mã | Bảng (Table) | Trọng tâm dữ liệu |
|---|---|---|
| E01 | `Users` | Lưu tất cả tài khoản (Customer, Driver, Admin). Phân biệt bằng `role` |
| E02 | `Vehicles` | Thông tin xe của tài xế (Biển số, loại xe) |
| E03 | `Trips` | Lưu thông tin chuyến (Điểm đón/đến, giá tiền, trạng thái, DriverID, CustomerID) |
| E04 | `Payments` | Lịch sử giao dịch (TripID, Phương thức, Số tiền, Trạng thái) |
| E05 | `Reviews` | Đánh giá chuyến đi (TripID, Rating, Comment) |
| E06 | `System_Logs` | Audit log thao tác hệ thống |

---

## 12. QUAN HỆ GIỮA CÁC THỰC THỂ

| Thực thể A | Quan hệ | Thực thể B |
|---|---|---|
| `Users` (Driver) | 1 - N | `Vehicles` |
| `Users` (Customer/Driver) | 1 - N | `Trips` |
| `Trips` | 1 - 1 | `Payments` |
| `Trips` | 1 - 1 | `Reviews` |
| `Users` | 1 - N | `System_Logs` |

---

## 13. USE CASE

| Mã | Ca sử dụng | Tác nhân chính |
|---|---|---|
| UC01 | Xử lý tài khoản & Phân quyền | Users, Admin |
| UC02 | Quản lý tài xế, xe & Định vị GPS | Driver, System |
| UC03 | Đặt xe & Theo dõi hành trình | Customer, Driver |
| UC04 | Thuật toán điều phối khớp xe | System, Driver |
| UC05 | Tính tiền & Thanh toán | Customer, System |
| UC06 | Thông báo & Đánh giá | System, Customer |
| UC07 | Quản trị, Báo cáo & Audit Log | Admin, Ops |

---

## 14. TIÊU CHÍ CHẤP NHẬN (AC)

| Mã AC | FR | Tiêu chí nghiệm thu ngắn gọn |
|---|---|---|
| AC01 | FR01 | Đăng ký/đăng nhập đúng OTP/Password; chặn truy cập sai quyền |
| AC02 | FR02 | Cập nhật được hồ sơ xe và tọa độ GPS của tài xế |
| AC03 | FR03 | Tạo chuyến thành công, hiển thị đúng trạng thái chuyến realtime |
| AC04 | FR04 | Tìm đúng xe gần nhất; tự đổi tài xế nếu từ chối/timeout |
| AC05 | FR05 | Tính đúng giá cước, thanh toán thành công (hoặc báo lỗi retry) |
| AC06 | FR06 | Nhận được thông báo sự kiện chuyến và lưu được đánh giá |
| AC07 | FR07 | Xem được Dashboard, xuất báo cáo và tra cứu được System Log |

---

## 15. MA TRẬN FR - AC

| Mã FR | Tiêu chí chấp nhận |
|---|---|
| FR01 | AC01 |
| FR02 | AC02 |
| FR03 | AC03 |
| FR04 | AC04 |
| FR05 | AC05 |
| FR06 | AC06 |
| FR07 | AC07 |

---

## 16. MA TRẬN TRUY VẾT YÊU CẦU

| Mục tiêu | BR | FR | AC | UC | QT |
|---|---|---|---|---|---|
| BG01 | BR01 | FR01 | AC01 | UC01 | QT01 |
| BG02 | BR02 | FR02 | AC02 | UC02 | QT03, QT04 |
| BG02, BG03 | BR03, BR04 | FR03 | AC03 | UC03 | QT02, QT04 |
| BG02 | BR05 | FR04 | AC04 | UC04 | QT03 |
| BG02 | BR06 | FR05 | AC05 | UC05 | QT05 |
| BG03 | BR07 | FR06 | AC06 | UC06 | QT02, QT06 |
| BG04 | BR08 | FR07 | AC07 | UC07 | QT07 |

---

## 17. QUY TẮC TRUY VẾT

```text
BG (Mục tiêu) -> BR (Yêu cầu) -> FR (Chức năng) -> AC (Nghiệm thu) -> UC (Ca sử dụng) -> QT (Quy trình)
