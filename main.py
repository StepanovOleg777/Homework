from src.utils import input_transaction
from src.reading_csv import read_csv_file
from src.reading_excel import read_excel_file
from src.processing import filter_by_state, sort_by_date, process_bank_search
from src.widget import get_date, mask_account_card
from src.generators import filter_by_currency


def main():
    """
    Основная функция программы. Обеспечивает взаимодействие с пользователем
    и обработку банковских транзакций согласно выбранным параметрам.
    """
    while True:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input()

        if choice == "1":
            data = input_transaction("data/operations.json")
            print("Для обработки выбран JSON-файл.")
            break
        elif choice == "2":
            data = read_csv_file("data/transactions.csv")
            print("Для обработки выбран CSV-файл.")
            break
        elif choice == "3":
            data = read_excel_file("data/transactions_excel.xlsx")
            print("Для обработки выбран XLSX-файл.")
            break
        else:
            print("Неправильное значение. Попробуйте еще раз.")

    available_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        choice = input("").strip().upper()

        if choice in available_statuses:
            filtered = filter_by_state(data, choice)
            print(f'Операции отфильтрованы по статусу "{choice}"')
            break
        else:
            print(f'Статус операции "{choice}" недоступен.')

    while True:
        print("Отсортировать операции по дате? Да/Нет")
        choice = input().strip().upper()
        if choice == "ДА":
            print("Отсортировать по возрастанию или по убыванию?")
            print("По возрастанию / По убыванию")
            sort_choice = input().strip().upper()
            if sort_choice == "ПО ВОЗРАСТАНИЮ":
                filtered = sort_by_date(filtered, rev=False)
                break
            elif sort_choice == "ПО УБЫВАНИЮ":
                filtered = sort_by_date(filtered, rev=True)
                break
            else:
                print("Повторите попытку")
        elif choice == "НЕТ":
            break
        else:
            print("Повторите попытку")

    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        choice = input().strip().upper()
        if choice == "ДА":
            filtered = filter_by_currency(filtered, "RUB")
            break
        elif choice == "НЕТ":
            break
        else:
            print("Повторите попытку")

    # Фильтрация по слову в описании
    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        choice = input().strip().upper()
        if choice == "ДА":
            search_word = input("Введите слово для поиска в описании: ").strip()
            filtered = process_bank_search(filtered, search_word)
            break
        elif choice == "НЕТ":
            break
        else:
            print("Повторите попытку")

    # Форматирование и вывод результатов
    list_of_final_transactions = []
    for transaction in filtered:
        final_transactions = []

        # Обработка даты
        date_str = transaction.get("date", "")
        if date_str:
            date = get_date(date_str)
            final_transactions.append(date)

        # Описание
        description = transaction.get("description", "")
        if description:
            final_transactions.append(description)

        # Откуда и куда
        if description == "Открытие вклада":
            to_account = transaction.get("to", "")
            if to_account:
                account = mask_account_card(to_account)
                final_transactions.append(account)
        else:
            from_account = transaction.get("from", "")
            to_account = transaction.get("to", "")
            if from_account and to_account:
                card_1 = mask_account_card(from_account)
                card_2 = mask_account_card(to_account)
                operation = f"{card_1} -> {card_2}"
                final_transactions.append(operation)

        # Сумма и валюта
        operation_amount = transaction.get("operationAmount", {})
        if operation_amount and isinstance(operation_amount, dict):
            amount = operation_amount.get("amount", "")
            currency = operation_amount.get("currency", "")
            if currency and isinstance(currency, dict):
                currency_name = currency.get("name", "")
            else:
                currency_name = str(currency) if currency else ""

            if amount and currency_name:
                sum_text = f"Сумма: {amount} {currency_name}"
                final_transactions.append(sum_text)

        if final_transactions:
            list_of_final_transactions.append("\n".join(final_transactions))

    # Вывод результатов
    if list_of_final_transactions:
        print("\nРаспечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(list_of_final_transactions)}\n")
        for transaction in list_of_final_transactions:
            print(transaction)
            print()  # Пустая строка между транзакциями
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
