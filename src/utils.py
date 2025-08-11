import json


def input_transaction(input_list):
    '''  Функция возвращает список словарей с данными о финансовых транзакциях
    из json-файла.'''
    try:
        with open(input_list, "r", encoding="utf-8") as f:
            transaction = json.load(f)
        return transaction
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []
    except TypeError:
        return []


print(input_transaction("data/operations.json"))
