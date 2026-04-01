import requests

BASE_URL = "http://127.0.0.1:5000/number/"

print("=== Тест POST ===")
resp_post = requests.post(
    BASE_URL,
    json={"jsonParam": 4},
    headers={"Content-Type": "application/json"},
    proxies={"http": None, "https": None}  # отключаем прокси
)
print(f"Статус: {resp_post.status_code}")
print(f"Ответ: {resp_post.json()}\n")

print("=== Тест DELETE ===")
resp_delete = requests.delete(
    BASE_URL,
    proxies={"http": None, "https": None}
)
print(f"Статус: {resp_delete.status_code}")
print(f"Ответ: {resp_delete.json()}")