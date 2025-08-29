import json
import re



def filter_by_state(list_dictionary: list, state="EXECUTED") -> list:
    """Функция фильтрует значение словарей по ключу"""

    filtered_list = []
    for dict_item in list_dictionary:
        if dict_item.get("state") == state:
            filtered_list.append(dict_item)
        else:
            continue
    return filtered_list

# print(filter_by_state(
#     [
#     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
#     ]))


def sort_by_date(list_of_date: list[dict], rev: bool = True) -> list[dict]:
    """Функция сортировки элементов списка по убыванию даты"""

    date_list = sorted(list_of_date, key=lambda i: i["date"], reverse=rev)
    return date_list


# print(sort_by_date(
#     [
#      {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
#      ]))


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