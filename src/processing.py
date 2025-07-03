def filter_by_state(list_of_dict: list, state="EXECUTED") -> list:
    filtered_list = []
    for dict_item in list_of_dict:
        if dict_item.get("state") == state:
            filtered_list.append(dict_item)
        else:
            continue
    return filtered_list


def sort_by_date(list_of_date: list[dict], rev: bool = True) -> list[dict]:
    """Функция сортировки элементов списка по убыванию даты"""

    date_list = sorted(list_of_date, key=lambda i: i["date"], reverse=rev)
    return date_list
