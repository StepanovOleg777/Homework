import pandas as pd


def read_excel_file(file_path):
    """считывает файл excel, выводит в виде списка словарей"""
    df = pd.read_excel(file_path, parse_dates=["date"])
    transactions = df.to_dict(orient="records")
    return transactions




# read_excel_file("data/transactions_excel.xlsx")
