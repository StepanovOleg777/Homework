import csv


def read_csv_file(file_path):
    """Функция для считывания финансовых операций из CSV файла."""
    list_csv = []
    with open(file_path, encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            list_csv.append(row)
    return list_csv
