import pandas as pd


def read_excel_file(file_path):
    df = pd.read_excel(file_path)
    result = []

    for index, row in df.iterrows():
        dict_ = {}

        for key, value in row.items():
            dict_[key] = value
            if 'id' in dict_:
                dict_['id'] = int(dict_['id'])

            result.append(dict_)

        return print(result)

read_excel_file('data/transactions_excel.xlsx')