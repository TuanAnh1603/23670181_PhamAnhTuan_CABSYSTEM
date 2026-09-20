
import requests

# ============================================================
# CONFIG
# ============================================================

BASE_URL = "http://localhost:8080"

CUSTOMER_PHONE = "0901234567"
CUSTOMER_PASSWORD = "12345678"

DRIVER_PHONE = "0912345678"
DRIVER_PASSWORD = "12345678"

DRIVER_ID = 201
CUSTOMER_ID = 101
TRIP_ID = 1001


# ============================================================
# HELPER
# ============================================================

def login(phone, password):
    """
    Login và lấy JWT token.
    """

    response = requests.post(
        f"{BASE_URL}/api/auth/login",
        json={
            "phone": phone,
            "password": password
        }
    )

    print("\nLOGIN RESPONSE:")
    print(response.status_code)
    print(response.text)

    if response.status_code != 200:
        return None

    data = response.json()

    return data.get(
        "accessToken",
        data.get("token")
    )


def auth_header(token):
    """
    Tạo Authorization Header.
    """

    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


# ============================================================
# TC_AUTH_001
# Đăng ký Customer
# API: POST /api/auth/register
# Expected: 201
# ============================================================

def test_TC_AUTH_001_register():

    payload = {
        "fullName": "Nguyen Van A",
        "phone": CUSTOMER_PHONE,
        "password": CUSTOMER_PASSWORD,
        "role": "CUSTOMER"
    }

    response = requests.post(
        f"{BASE_URL}/api/auth/register",
        json=payload
    )

    print("\nTC_AUTH_001")
    print(response.status_code)
    print(response.text)

    assert response.status_code in [201, 409]


# ============================================================
# TC_AUTH_002
# Đăng ký tài khoản đã tồn tại
# API: POST /api/auth/register
# Expected: 409
# ============================================================

def test_TC_AUTH_002_register_existing():

    payload = {
        "fullName": "Nguyen Van A",
        "phone": CUSTOMER_PHONE,
        "password": CUSTOMER_PASSWORD,
        "role": "CUSTOMER"
    }

    response = requests.post(
        f"{BASE_URL}/api/auth/register",
        json=payload
    )

    print("\nTC_AUTH_002")
    print(response.status_code)
    print(response.text)

    assert response.status_code == 409


# ============================================================
# TC_AUTH_003
# Login thành công
# API: POST /api/auth/login
# Expected: 200
# ============================================================

def test_TC_AUTH_003_login():

    token = login(
        CUSTOMER_PHONE,
        CUSTOMER_PASSWORD
    )

    assert token is not None
    assert len(token) > 0


# ============================================================
# TC_AUTH_004
# Login sai password
# API: POST /api/auth/login
# Expected: 401
# ============================================================

def test_TC_AUTH_004_wrong_password():

    response = requests.post(
        f"{BASE_URL}/api/auth/login",
        json={
            "phone": CUSTOMER_PHONE,
            "password": "wrong_password"
        }
    )

    print("\nTC_AUTH_004")
    print(response.status_code)
    print(response.text)

    assert response.status_code == 401


# ============================================================
# TC_DRIVER_001
# Update Driver
# API: PUT /api/drivers/{driverId}
# Expected: 200
# ============================================================

def test_TC_DRIVER_001_update_driver():

    token = login(
        DRIVER_PHONE,
        DRIVER_PASSWORD
    )

    assert token is not None

    payload = {
        "fullName": "Tran Van B",
        "phone": DRIVER_PHONE,
        "licenseNumber": "B2-123456"
    }

    response = requests.put(
        f"{BASE_URL}/api/drivers/{DRIVER_ID}",
        headers=auth_header(token),
        json=payload
    )

    print("\nTC_DRIVER_001")
    print(response.status_code)
    print(response.text)

    assert response.status_code == 200


# ============================================================
# TC_DRIVER_002
# Update GPS hợp lệ
# API: POST /api/drivers/{driverId}/location
# Expected: 200
# ============================================================

def test_TC_DRIVER_002_update_gps():

    token = login(
        DRIVER_PHONE,
        DRIVER_PASSWORD
    )

    assert token is not None

    payload = {
        "latitude": 10.7769,
        "longitude": 106.7009
    }

    response = requests.post(
        f"{BASE_URL}/api/drivers/{DRIVER_ID}/location",
        headers=auth_header(token),
        json=payload
    )

    print("\nTC_DRIVER_002")
    print(response.status_code)
    print(response.text)

    assert response.status_code == 200


# ============================================================
# TC_DRIVER_003
# GPS không hợp lệ
# API: POST /api/drivers/{driverId}/location
# Expected: 400
# ============================================================

def test_TC_DRIVER_003_invalid_gps():

    token = login(
        DRIVER_PHONE,
        DRIVER_PASSWORD
    )

    assert token is not None

    payload = {
        "latitude": 100,
        "longitude": 106.7009
    }

    response = requests.post(
        f"{BASE_URL}/api/drivers/{DRIVER_ID}/location",
        headers=auth_header(token),
        json=payload
    )

    print("\nTC_DRIVER_003")
    print(response.status_code)
    print(response.text)

    assert response.status_code == 400


# ============================================================
# TC_TRIP_001
# Tạo chuyến
# API: POST /api/trips
# Expected: 201
# ============================================================

def test_TC_TRIP_001_create_trip():

    token = login(
        CUSTOMER_PHONE,
        CUSTOMER_PASSWORD
    )

    assert token is not None

    payload = {
        "customerId": CUSTOMER_ID,
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

    response = requests.post(
        f"{BASE_URL}/api/trips",
        headers=auth_header(token),
        json=payload
    )

    print("\nTC_TRIP_001")
    print(response.status_code)
    print(response.text)

    assert response.status_code == 201


# ============================================================
# TC_TRIP_002
# Tạo chuyến không login
# API: POST /api/trips
# Expected: 401
# ============================================================

def test_TC_TRIP_002_create_trip_without_login():

    payload = {
        "customerId": CUSTOMER_ID,
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

    response = requests.post(
        f"{BASE_URL}/api/trips",
        json=payload
    )

    print("\nTC_TRIP_002")
    print(response.status_code)
    print(response.text)

    assert response.status_code == 401


# ============================================================
# TC_TRIP_003
# Dispatch có Driver
# API: POST /api/trips/{tripId}/dispatch
# Expected: 200
# ============================================================

def test_TC_TRIP_003_dispatch():

    token = login(
        CUSTOMER_PHONE,
        CUSTOMER_PASSWORD
    )

    assert token is not None

    payload = {
        "searchRadius": 5
    }

    response = requests.post(
        f"{BASE_URL}/api/trips/{TRIP_ID}/dispatch",
        headers=auth_header(token),
        json=payload
    )

    print("\nTC_TRIP_003")
    print(response.status_code)
    print(response.text)

    assert response.status_code == 200


# ============================================================
# TC_TRIP_004
# Dispatch không có Driver
# API: POST /api/trips/{tripId}/dispatch
# Expected: 404
# ============================================================

def test_TC_TRIP_004_dispatch_no_driver():

    token = login(
        CUSTOMER_PHONE,
        CUSTOMER_PASSWORD
    )

    assert token is not None

    payload = {
        "searchRadius": 0.001
    }

    response = requests.post(
        f"{BASE_URL}/api/trips/{TRIP_ID}/dispatch",
        headers=auth_header(token),
        json=payload
    )

    print("\nTC_TRIP_004")
    print(response.status_code)
    print(response.text)

    assert response.status_code == 404


# ============================================================
# TC_TRIP_005
# Update Trip Status
# API: PUT /api/trips/{tripId}/status
# Expected: 200
# ============================================================

def test_TC_TRIP_005_update_status():

    token = login(
        DRIVER_PHONE,
        DRIVER_PASSWORD
    )

    assert token is not None

    payload = {
        "status": "IN_TRIP"
    }

    response = requests.put(
        f"{BASE_URL}/api/trips/{TRIP_ID}/status",
        headers=auth_header(token),
        json=payload
    )

    print("\nTC_TRIP_005")
    print(response.status_code)
    print(response.text)

    assert response.status_code == 200


# ============================================================
# TC_TRIP_006
# Update Trip Status không hợp lệ
# API: PUT /api/trips/{tripId}/status
# Expected: 400 hoặc 409
# ============================================================

def test_TC_TRIP_006_invalid_status():

    token = login(
        DRIVER_PHONE,
        DRIVER_PASSWORD
    )

    assert token is not None

    payload = {
        "status": "INVALID_STATUS"
    }

    response = requests.put(
        f"{BASE_URL}/api/trips/{TRIP_ID}/status",
        headers=auth_header(token),
        json=payload
    )

    print("\nTC_TRIP_006")
    print(response.status_code)
    print(response.text)

    assert response.status_code in [400, 409]


# ============================================================
# TC_PAYMENT_001
# Thanh toán Wallet
# API: POST /api/trips/{tripId}/payment
# Expected: 200
# ============================================================

def test_TC_PAYMENT_001_payment_success():

    token = login(
        CUSTOMER_PHONE,
        CUSTOMER_PASSWORD
    )

    assert token is not None

    payload = {
        "paymentMethod": "WALLET",
        "amount": 85000
    }

    response = requests.post(
        f"{BASE_URL}/api/trips/{TRIP_ID}/payment",
        headers=auth_header(token),
        json=payload
    )

    print("\nTC_PAYMENT_001")
    print(response.status_code)
    print(response.text)

    assert response.status_code == 200


# ============================================================
# TC_PAYMENT_002
# Thanh toán thất bại
# API: POST /api/trips/{tripId}/payment
# Expected: 402
# ============================================================

def test_TC_PAYMENT_002_payment_failed():

    token = login(
        CUSTOMER_PHONE,
        CUSTOMER_PASSWORD
    )

    assert token is not None

    payload = {
        "paymentMethod": "WALLET",
        "amount": 999999999
    }

    response = requests.post(
        f"{BASE_URL}/api/trips/{TRIP_ID}/payment",
        headers=auth_header(token),
        json=payload
    )

    print("\nTC_PAYMENT_002")
    print(response.status_code)
    print(response.text)

    assert response.status_code == 402


# ============================================================
# TC_REVIEW_001
# Đánh giá chuyến
# API: POST /api/trips/{tripId}/review
# Expected: 201
# ============================================================

def test_TC_REVIEW_001_create_review():

    token = login(
        CUSTOMER_PHONE,
        CUSTOMER_PASSWORD
    )

    assert token is not None

    payload = {
        "rating": 5,
        "comment": "Tai xe rat nhiet tinh"
    }

    response = requests.post(
        f"{BASE_URL}/api/trips/{TRIP_ID}/review",
        headers=auth_header(token),
        json=payload
    )

    print("\nTC_REVIEW_001")
    print(response.status_code)
    print(response.text)

    assert response.status_code == 201


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("CAB SYSTEM - API AUTOMATED TEST")
    print("=" * 60)
    print(f"BASE URL: {BASE_URL}")
    print("=" * 60)
