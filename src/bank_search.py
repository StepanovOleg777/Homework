import json
import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция, которая будет принимать список словарей с данными о банковских операциях и список
    категорий операций, а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории."""
    result_list = []
    with open(data, "r", encoding="utf-8") as f:
        transactions = json.load(f)
        for d in transactions:
            if re.findall(search, "description", flags=re.IGNORECASE):
                result_list.append(d)
            else:
                continue
        return result_list
