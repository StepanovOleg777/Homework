from collections import Counter
import json


with open("data/operations.json", "r", encoding="utf-8") as file:
    data = json.load(file)

categories = [
    "Перевод с карты на счет",
    "Перевод с карты на карту",
    "Перевод организации",
    "Открытие вклада",
    "Перевод со счета на счет",
]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях
    и список категорий операций, а возвращает словарь, в котором ключи — это
    названия категорий, а значения — это количество операций в каждой категории."""
    category_list = [
        operation.get("description", "") for operation in data if operation.get("description", "") in categories
    ]
    category_count = Counter(category_list)
    return dict(category_count)


result = process_bank_operations(data, categories)
print(result)
