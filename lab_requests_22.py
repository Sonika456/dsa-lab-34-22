import random
import requests
from typing import Dict, Any

# Адрес локального сервера
BASE_URL = "http://127.0.0.1:5000/number/"

def send_get_request() -> Dict[str, Any]:
    """
    Задача 1: Отправить GET запрос с параметром param (рандомное число 1-10).
    """
    param_value = random.randint(1, 10)
    response = requests.get(BASE_URL, params={"param": param_value})
    
    print(f"GET запрос с param={param_value}")
    print(f"Статус код: {response.status_code}")
    
    data = response.json()
    print(f"Ответ сервера: {data}\n")
    
    return data


def send_post_request() -> Dict[str, Any]:
    """
    Задача 2: Отправить POST запрос с телом JSON {"jsonParam": рандомное число 1-10}.
    """
    param_value = random.randint(1, 10)
    headers = {"Content-Type": "application/json"}
    json_data = {"jsonParam": param_value}
    
    response = requests.post(BASE_URL, json=json_data, headers=headers)
    
    print(f"POST запрос с jsonParam={param_value}")
    print(f"Статус код: {response.status_code}")
    
    data = response.json()
    print(f"Ответ сервера: {data}\n")
    
    return data


def send_delete_request() -> Dict[str, Any]:
    """
    Задача 3: Отправить DELETE запрос.
    """
    response = requests.delete(BASE_URL)
    
    print("DELETE запрос")
    print(f"Статус код: {response.status_code}")
    
    data = response.json()
    print(f"Ответ сервера: {data}\n")
    
    return data


def calculate_expression(get_data: Dict, post_data: Dict, delete_data: Dict) -> int:
    """
    Задача 4: Составить выражение из полученных ответов и посчитать результат.
    Операции выполняются последовательно.
    """
    # Получаем числа и операции из ответов
    number_1 = get_data["number"]
    operation_1 = get_data["operation"]
    
    number_2 = post_data["number"]
    operation_2 = post_data["operation"]
    
    number_3 = delete_data["number"]
    operation_3 = delete_data["operation"]
    
    # Словарь операций для вычислений
    operations_map = {
        "sum": lambda x, y: x + y,
        "sub": lambda x, y: x - y,
        "mul": lambda x, y: x * y,
        "div": lambda x, y: x / y if y != 0 else x  # Защита от деления на 0
    }
    
    # Выполняем операции последовательно
    print("Вычисление выражения")
    print(f"Шаг 1: {number_1} {operation_1} {number_2}")
    
    result = operations_map[operation_1](number_1, number_2)
    print(f"Промежуточный результат: {result}")
    
    print(f"Шаг 2: {result} {operation_2} {number_3}")
    
    result = operations_map[operation_2](result, number_3)
    print(f"Промежуточный результат: {result}")
    
    # Приводим к int, как требуется в задании
    final_result = int(result)
    
    return final_result


def main():
    # 1. Отправляем запросы и сохраняем ответы
    get_response = send_get_request()
    post_response = send_post_request()
    delete_response = send_delete_request()
    
    # 2. Вычисляем итоговое выражение
    final_result = calculate_expression(get_response, post_response, delete_response)
    
    print(f"Итоговый результат (int): {final_result}")

main()

