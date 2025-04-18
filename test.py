import requests

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIn0.MBRH_c3gYjFHeAfLJePUN9VRzFGybCcQDU92q2mNGCE"
}

data = {
    "delivery_address": "Назарбаева"
}

response = requests.get("http://127.0.0.1:8080/orders/", headers=headers)
print(response.json())