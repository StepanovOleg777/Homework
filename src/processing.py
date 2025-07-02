def filter_by_state(list_of_status_state: list[dict],  state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрует статус операции"""

    operation_executed = []
    operation_canceled = []

    for operation in list_of_status_state:
        if operation["state"] == "EXECUTED":
            operation_executed.append(operation)
        elif operation["state"] == "CANCELED":
            operation_canceled.append(operation)
    if state == "EXECUTED":
        return operation_executed
    elif state == "CANCELED":
        return operation_canceled


def sort_by_date(list_of_date: list[dict], rev: bool = True) -> list[dict]:
    """Функция сортировки элементов списка по убыванию даты"""

    sorted_list_of_date = sorted(list_of_date, key=lambda i: i["date"], reverse=rev)
    return sorted_list_of_date

