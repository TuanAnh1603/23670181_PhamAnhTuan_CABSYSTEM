
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


