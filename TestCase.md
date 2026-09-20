Nếu bạn muốn **file `.md` để đưa thẳng lên GitHub**, bạn có thể tạo file `TEST_CASE.md` với nội dung sau:

 TEST\_CASE.md

# CAB System - API Test Cases

 ## 1\. Tổng quan

 Tài liệu này mô tả các Test Case kiểm thử REST API cho hệ thống **CAB - Nền tảng đặt xe trực tuyến**.

 ### Công nghệ kiểm thử

 - Python
- Pytest
- REST API
- Requests
- JWT Authentication

 ### Base URL

```
http://localhost:8080
```

---

 ## 2\. Danh sách Test Case

 | Test Case ID | Test Scenario | Test Case | API | Expected Result | Priority |
| --- | --- | --- | --- | --- | --- |
| TC\_AUTH\_001 | Đăng ký tài khoản | Đăng ký Customer với thông tin hợp lệ | `POST /api/auth/register` | `201 Created` \- Tạo tài khoản thành công | High |
| TC\_AUTH\_002 | Đăng ký tài khoản | Đăng ký với số điện thoại đã tồn tại | `POST /api/auth/register` | `409 Conflict` \- Tài khoản đã tồn tại | High |
| TC\_AUTH\_003 | Đăng nhập | Đăng nhập với thông tin hợp lệ | `POST /api/auth/login` | `200 OK` \- Trả về JWT/token | High |
| TC\_AUTH\_004 | Đăng nhập | Đăng nhập với password sai | `POST /api/auth/login` | `401 Unauthorized` | High |
| TC\_DRIVER\_001 | Quản lý tài xế | Cập nhật thông tin tài xế hợp lệ | `PUT /api/drivers/{driverId}` | `200 OK` | Medium |
| TC\_DRIVER\_002 | GPS tài xế | Cập nhật vị trí GPS hợp lệ | `POST /api/drivers/{driverId}/location` | `200 OK` | High |
| TC\_DRIVER\_003 | GPS tài xế | Cập nhật GPS với tọa độ không hợp lệ | `POST /api/drivers/{driverId}/location` | `400 Bad Request` | Medium |
| TC\_TRIP\_001 | Đặt xe | Customer tạo chuyến với dữ liệu hợp lệ | `POST /api/trips` | `201 Created` | High |
| TC\_TRIP\_002 | Đặt xe | Tạo chuyến khi chưa đăng nhập | `POST /api/trips` | `401 Unauthorized` | High |
| TC\_TRIP\_003 | Điều phối | Điều phối khi có tài xế phù hợp | `POST /api/trips/{tripId}/dispatch` | `200 OK` | High |
| TC\_TRIP\_004 | Điều phối | Điều phối khi không có tài xế phù hợp | `POST /api/trips/{tripId}/dispatch` | `404 Not Found` | High |
| TC\_TRIP\_005 | Quản lý chuyến | Cập nhật trạng thái chuyến hợp lệ | `PUT /api/trips/{tripId}/status` | `200 OK` | High |
| TC\_TRIP\_006 | Quản lý chuyến | Cập nhật trạng thái không hợp lệ | `PUT /api/trips/{tripId}/status` | `400` hoặc `409` | High |
| TC\_PAYMENT\_001 | Thanh toán | Thanh toán bằng Wallet thành công | `POST /api/trips/{tripId}/payment` | `200 OK` | High |
| TC\_PAYMENT\_002 | Thanh toán | Thanh toán Wallet thất bại | `POST /api/trips/{tripId}/payment` | `402 Payment Required` | High |
| TC\_REVIEW\_001 | Đánh giá | Customer đánh giá chuyến đã hoàn thành | `POST /api/trips/{tripId}/review` | `201 Created` | Medium |

---

 # 3\. Chi tiết Test Case

 ## TC\_AUTH\_001 - Đăng ký Customer thành công

 **Test Scenario:** Đăng ký tài khoản

 **API:**

```
POST /api/auth/register
```

 **Preconditions:**

 - API Server đang hoạt động.
- Số điện thoại chưa tồn tại trong hệ thống.

 **Request Body:**

```
{
  "fullName": "Nguyen Van A",
  "phone": "0901234567",
  "password": "12345678",
  "role": "CUSTOMER"
}
```

 **Expected Result:**

```
HTTP 201 Created
```

 - Tài khoản Customer được tạo thành công.
- Thông tin tài khoản được lưu vào database.

 **Priority:** High

---

 ## TC\_AUTH\_002 - Đăng ký tài khoản đã tồn tại

 **Test Scenario:** Đăng ký tài khoản

 **API:**

```
POST /api/auth/register
```

 **Preconditions:**

 - Số điện thoại `0901234567` đã tồn tại.

 **Request Body:**

```
{
  "fullName": "Nguyen Van A",
  "phone": "0901234567",
  "password": "12345678",
  "role": "CUSTOMER"
}
```

 **Expected Result:**

```
HTTP 409 Conflict
```

 - Hệ thống thông báo tài khoản đã tồn tại.
- Không tạo thêm tài khoản mới.

 **Priority:** High

---

 ## TC\_AUTH\_003 - Đăng nhập thành công

 **Test Scenario:** Đăng nhập

 **API:**

```
POST /api/auth/login
```

 **Preconditions:**

 - Tài khoản đã tồn tại.
- Password chính xác.

 **Request Body:**

```
{
  "phone": "0901234567",
  "password": "12345678"
}
```

 **Expected Result:**

```
HTTP 200 OK
```

 - Đăng nhập thành công.
- API trả về JWT/token.
- Token có thể được sử dụng cho các API yêu cầu authentication.

 **Priority:** High

---

 ## TC\_AUTH\_004 - Đăng nhập sai password

 **Test Scenario:** Đăng nhập

 **API:**

```
POST /api/auth/login
```

 **Request Body:**

```
{
  "phone": "0901234567",
  "password": "wrong123"
}
```

 **Expected Result:**

```
HTTP 401 Unauthorized
```

 - Không cấp JWT/token.
- Người dùng không được đăng nhập.

 **Priority:** High

---

 ## TC\_DRIVER\_001 - Cập nhật thông tin tài xế

 **Test Scenario:** Quản lý tài xế

 **API:**

```
PUT /api/drivers/{driverId}
```

 **Preconditions:**

 - Driver đã đăng nhập.
- JWT hợp lệ.
- Driver tồn tại.

 **Path Parameter:**

```
driverId = 201
```

 **Request Body:**

```
{
  "fullName": "Tran Van B",
  "phone": "0912345678",
  "licenseNumber": "B2-123456"
}
```

 **Expected Result:**

```
HTTP 200 OK
```

 Thông tin Driver được cập nhật thành công.

 **Priority:** Medium

---

 ## TC\_DRIVER\_002 - Cập nhật GPS hợp lệ

 **Test Scenario:** Cập nhật vị trí GPS

 **API:**

```
POST /api/drivers/{driverId}/location
```

 **Preconditions:**

 - Driver đã đăng nhập.
- JWT hợp lệ.

 **Request Body:**

```
{
  "latitude": 10.7769,
  "longitude": 106.7009
}
```

 **Expected Result:**

```
HTTP 200 OK
```

 - Tọa độ GPS được cập nhật.
- Hệ thống lưu vị trí mới của Driver.

 **Priority:** High

---

 ## TC\_DRIVER\_003 - GPS không hợp lệ

 **Test Scenario:** Cập nhật GPS

 **API:**

```
POST /api/drivers/{driverId}/location
```

 **Request Body:**

```
{
  "latitude": 100,
  "longitude": 106.7009
}
```

 **Expected Result:**

```
HTTP 400 Bad Request
```

 Hệ thống từ chối dữ liệu vì:

```
latitude > 90
```

 **Priority:** Medium

---

 ## TC\_TRIP\_001 - Tạo chuyến thành công

 **Test Scenario:** Đặt xe

 **API:**

```
POST /api/trips
```

 **Preconditions:**

 - Customer đã đăng nhập.
- JWT hợp lệ.

 **Request Body:**

```
{
  "customerId": 101,
  "pickup": {
    "latitude": 10.7769,
    "longitude": 106.7009
  },
  "destination": {
    "latitude": 10.8231,
    "longitude": 106.6297
  },
  "vehicleType": "CAR"
}
```

 **Expected Result:**

```
HTTP 201 Created
```

 Trip được tạo thành công với trạng thái:

```
CREATED
```

 **Priority:** High

---

 ## TC\_TRIP\_002 - Tạo chuyến khi chưa đăng nhập

 **Test Scenario:** Đặt xe

 **API:**

```
POST /api/trips
```

 **Preconditions:**

 - Không có JWT.
- Không gửi Authorization Header.

 **Request Body:**

```
{
  "customerId": 101,
  "pickup": {
    "latitude": 10.7769,
    "longitude": 106.7009
  },
  "destination": {
    "latitude": 10.8231,
    "longitude": 106.6297
  },
  "vehicleType": "CAR"
}
```

 **Expected Result:**

```
HTTP 401 Unauthorized
```

 Trip không được tạo.

 **Priority:** High

---

 ## TC\_TRIP\_003 - Điều phối tài xế thành công

 **Test Scenario:** Điều phối

 **API:**

```
POST /api/trips/{tripId}/dispatch
```

 **Preconditions:**

 - Trip tồn tại.
- Trip đang ở trạng thái `CREATED`.
- Có Driver online trong khu vực.

 **Path Parameter:**

```
tripId = 1001
```

 **Request Body:**

```
{
  "searchRadius": 5
}
```

 **Expected Result:**

```
HTTP 200 OK
```

 - Hệ thống tìm được Driver.
- Driver được gán vào Trip.
- Trip chuyển sang:

```
ASSIGNED
```

 **Priority:** High

---

 ## TC\_TRIP\_004 - Không tìm thấy tài xế

 **Test Scenario:** Điều phối

 **API:**

```
POST /api/trips/{tripId}/dispatch
```

 **Preconditions:**

 - Trip tồn tại.
- Không có Driver phù hợp trong bán kính tìm kiếm.

 **Request Body:**

```
{
  "searchRadius": 5
}
```

 **Expected Result:**

```
HTTP 404 Not Found
```

 Hệ thống thông báo không tìm thấy Driver phù hợp.

 **Priority:** High

---

 ## TC\_TRIP\_005 - Cập nhật trạng thái chuyến

 **Test Scenario:** Quản lý chuyến

 **API:**

```
PUT /api/trips/{tripId}/status
```

 **Preconditions:**

 - Trip tồn tại.
- Driver đã nhận chuyến.
- Trip đang ở trạng thái `ASSIGNED`.

 **Request Body:**

```
{
  "status": "IN_TRIP"
}
```

 **Expected Result:**

```
HTTP 200 OK
```

 Trạng thái Trip được cập nhật thành:

```
IN_TRIP
```

 **Priority:** High

---

 ## TC\_TRIP\_006 - Cập nhật trạng thái không hợp lệ

 **Test Scenario:** Quản lý chuyến

 **API:**

```
PUT /api/trips/{tripId}/status
```

 **Request Body:**

```
{
  "status": "INVALID_STATUS"
}
```

 **Expected Result:**

```
HTTP 400 Bad Request
```

 hoặc:

```
HTTP 409 Conflict
```

 Trạng thái Trip không được thay đổi.

 **Priority:** High

---

 ## TC\_PAYMENT\_001 - Thanh toán Wallet thành công

 **Test Scenario:** Thanh toán

 **API:**

```
POST /api/trips/{tripId}/payment
```

 **Preconditions:**

 - Trip đã hoàn thành.
- Wallet có đủ số dư.
- Trip chưa được thanh toán.

 **Request Body:**

```
{
  "paymentMethod": "WALLET",
  "amount": 85000
}
```

 **Expected Result:**

```
HTTP 200 OK
```

 - Thanh toán thành công.
- Transaction được ghi nhận.
- Payment được lưu vào database.

 **Priority:** High

---

 ## TC\_PAYMENT\_002 - Thanh toán Wallet thất bại

 **Test Scenario:** Thanh toán

 **API:**

```
POST /api/trips/{tripId}/payment
```

 **Preconditions:**

 - Trip đã hoàn thành.
- Wallet không đủ tiền hoặc Payment Gateway từ chối giao dịch.

 **Request Body:**

```
{
  "paymentMethod": "WALLET",
  "amount": 85000
}
```

 **Expected Result:**

```
HTTP 402 Payment Required
```

 - Thanh toán thất bại.
- Không ghi nhận giao dịch thành công.
- Người dùng có thể thử lại hoặc chuyển sang `CASH`.

 **Priority:** High

---

 ## TC\_REVIEW\_001 - Đánh giá chuyến đi

 **Test Scenario:** Đánh giá

 **API:**

```
POST /api/trips/{tripId}/review
```

 **Preconditions:**

 - Trip đã hoàn thành.
- Trip chưa có Review.

 **Request Body:**

```
{
  "rating": 5,
  "comment": "Tai xe rat nhiet tinh"
}
```

 **Expected Result:**

```
HTTP 201 Created
```

 - Review được tạo thành công.
- Rating được lưu trong khoảng `1 - 5`.
- Comment được lưu vào database.

 **Priority:** Medium

---

 # 4\. API Coverage

 | API | Test Case |
| --- | --- |
| `POST /api/auth/register` | TC\_AUTH\_001, TC\_AUTH\_002 |
| `POST /api/auth/login` | TC\_AUTH\_003, TC\_AUTH\_004 |
| `PUT /api/drivers/{driverId}` | TC\_DRIVER\_001 |
| `POST /api/drivers/{driverId}/location` | TC\_DRIVER\_002, TC\_DRIVER\_003 |
| `POST /api/trips` | TC\_TRIP\_001, TC\_TRIP\_002 |
| `POST /api/trips/{tripId}/dispatch` | TC\_TRIP\_003, TC\_TRIP\_004 |
| `PUT /api/trips/{tripId}/status` | TC\_TRIP\_005, TC\_TRIP\_006 |
| `POST /api/trips/{tripId}/payment` | TC\_PAYMENT\_001, TC\_PAYMENT\_002 |
| `POST /api/trips/{tripId}/review` | TC\_REVIEW\_001 |

---

 # 5\. Requirement Traceability

 | Test Case | FR | AC | API |
| --- | --- | --- | --- |
| TC\_AUTH\_001 | FR01 | AC01 | `/api/auth/register` |
| TC\_AUTH\_002 | FR01 | AC01 | `/api/auth/register` |
| TC\_AUTH\_003 | FR01 | AC01 | `/api/auth/login` |
| TC\_AUTH\_004 | FR01 | AC01 | `/api/auth/login` |
| TC\_DRIVER\_001 | FR02 | AC02 | `/api/drivers/{driverId}` |
| TC\_DRIVER\_002 | FR02 | AC02 | `/api/drivers/{driverId}/location` |
| TC\_DRIVER\_003 | FR02 | AC02 | `/api/drivers/{driverId}/location` |
| TC\_TRIP\_001 | FR03 | AC03 | `/api/trips` |
| TC\_TRIP\_002 | FR03 | AC03 | `/api/trips` |
| TC\_TRIP\_003 | FR04 | AC04 | `/api/trips/{tripId}/dispatch` |
| TC\_TRIP\_004 | FR04 | AC04 | `/api/trips/{tripId}/dispatch` |
| TC\_TRIP\_005 | FR03 | AC03 | `/api/trips/{tripId}/status` |
| TC\_TRIP\_006 | FR03 | AC03 | `/api/trips/{tripId}/status` |
| TC\_PAYMENT\_001 | FR05 | AC05 | `/api/trips/{tripId}/payment` |
| TC\_PAYMENT\_002 | FR05 | AC05 | `/api/trips/{tripId}/payment` |
| TC\_REVIEW\_001 | FR06 | AC06 | `/api/trips/{tripId}/review` |

---

 # 6\. Cách chạy Test

 Cài thư viện:

```
pip install pytest requests
```

 Chạy toàn bộ Test Case:

```
pytest -v
```

 Chạy một Test Case:

```
pytest -v tests/test_cab_api.py::test_TC_AUTH_003_login_success
```

 Chạy nhóm Authentication:

```
pytest -v tests/test_cab_api.py -k "AUTH"
```

 Chạy nhóm Trip:

```
pytest -v tests/test_cab_api.py -k "TRIP"
```

---

 # 7\. Cấu trúc Repository

```
CAB-System/
│
├── tests/
│   └── test_cab_api.py
│
├── requirements.txt
├── pytest.ini
├── TEST_CASE.md
└── README.md
```

 # 8\. Test Case Summary

 | Category | Số lượng |
| --- | --- |
| Authentication | 4 |
| Driver & GPS | 3 |
| Trip & Dispatch | 6 |
| Payment | 2 |
| Review | 1 |
| **Tổng cộng** | **16** |

> Lưu ý: danh sách hiện tại thực tế có **16 Test Case**, vì phần trước đã bổ sung `TC_TRIP_006` và `TC_REVIEW_001` vào danh sách 15 case ban đầu. Nếu yêu cầu bài của bạn bắt buộc **đúng 15 Test Case**, có thể bỏ `TC_TRIP_006` hoặc gộp nó vào nhóm kiểm thử Trip Status.

 Bạn chỉ cần copy phần trên vào file **`TEST_CASE.md`** rồi push lên GitHub.
