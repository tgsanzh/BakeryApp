import requests

BASE_URL = "http://127.0.0.1:8080/users"

# 1. Регистрация
register_data = {
    "phone": "string",
    "password": "string"
}
# register_response = requests.post(f"{BASE_URL}/register", json=register_data)
# print("Регистрация:", register_response.status_code, register_response.json())

# 2. Логин
login_response = requests.post(f"{BASE_URL}/login", json=register_data)
print("Логин:", login_response.status_code, login_response.json())

# 3. Получение токена
token = login_response.json().get("access_token")

# 4. Доступ к защищённому маршруту
headers = {
    "Authorization": f"Bearer {token}"
}
protected_response = requests.get(f"{BASE_URL}/protected", headers=headers)
print("Защищённый эндпоинт:", protected_response.status_code, protected_response.json())
