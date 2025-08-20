from src.utils import input_transaction
from src.reading_csv import read_csv_file
from src.reading_excel import read_excel_file
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card




def main():
    while True:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input()

        if choice == "1":
             data = input_transaction('data/operations.json')
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
             print("Неправильное значение.Попробуйте еще раз.")

    available_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:

        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        choice = input("").strip().upper()

        if choice in available_statuses:
            if choice == 'EXECUTED':
                filtered = filter_by_state(data, 'EXECUTED')
            elif choice == "CANCELED":
                filtered = filter_by_state(data, "CANCELED")
            else:
                filtered = filter_by_state(data, "PENDING")
            print(f"Операции отфильтрованы по статусу \"{choice}\"")
            break
        else:
            print(f"Статус операции \"{choice}\" недоступен.")

    while True:
        print(f'Отсортировать операции по дате?')
        choice = input('Да/Нет').strip().upper()
        if choice == 'ДА':
            print(f'Отсортировать по возрастанию или по убыванию?')
            choice = input('По возрастанию /По убыванию').strip().upper()
            if choice == 'ПО ВОЗРАСТАНИЮ':
                filtered = sort_by_date(filtered,  rev = False)
                break
            elif choice == 'ПО УБЫВАНИЮ':
                filtered = sort_by_date(filtered, rev=True)
                break
            else:
                print('Повторите попытку')
        elif choice == 'НЕТ':
            break
        else:
            print('Повторите попытку')

    #While True
    #Выводить только рублевые транзакции? Да/Нет

    #While True
    #Отфильтровать список транзакций по определенному слову в описании? Да/Нет


    list_of_final_transactions = []
    for transaction in filtered:
        final_transactions = []
        date = get_date(transaction.get("date", {}))

        if date == "Please, enter the date in the 'year-month-day' format":
            timestamp = transaction.get("date", {})
            formatted_date = timestamp.strftime("%Y-%m-%d")
            date = get_date(formatted_date)

        final_transactions.append(date)
        description = transaction.get("description", {})
        final_transactions.append(description)

        if description == "Открытие вклада":
            account = mask_account_card(transaction.get("to", {}))
            final_transactions.append(account)

        else:
            card_1 = mask_account_card(transaction.get("from", {}))
            card_2 = mask_account_card(transaction.get("to", {}))
            operation = card_1 + " -> " + card_2
            final_transactions.append(operation)

        if transaction.get("operationAmount", 0) != 0:
            currency = transaction.get("operationAmount", {}).get("currency", {}).get("name", {})
            sum = "Сумма: " + str(transaction.get("operationAmount", {}).get("amount", {})) + " " + currency
            final_transactions.append(sum)
        else:
            currency = transaction.get("currency_name")
            sum = "Сумма: " + str(transaction.get("amount", {})) + " " + currency
            final_transactions.append(sum)
            list_of_final_transactions.append("\n" + "\n".join(final_transactions))
    print(
        f"""
    Распечатываю итоговый список транзакций...
    Всего банковских операций в выборке: {len(filtered)}"""
    )

    print("\n".join(list_of_final_transactions))






if __name__ == '__main__':
    main()