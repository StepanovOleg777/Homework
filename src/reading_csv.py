import csv


def read_csv_file(file_path):
    """Функция для считывания финансовых операций из CSV файла."""
    list_csv = []
    with open(file_path) as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            list_csv.append(row)
    print(list_csv)


read_csv_file("data/transactions.csv")
