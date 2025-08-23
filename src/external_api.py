import os
from dotenv import load_dotenv
import requests


load_dotenv()
API_KEY = os.getenv("API_KEY")


def transaction_amount(transaction):
    """Функция возвращает сумму транзакций в рублях.Если транзакция в USD или EUR конвертирует в рубли."""
    for i in transaction:
        if i == {}:
            return "Нет транзакции!"
        elif i["operationAmount"]["currency"]["code"] == "RUB":
            return i["operationAmount"]["amount"]
        elif i["operationAmount"]["currency"]["code"] == "USD" or i["operationAmount"]["currency"]["code"] == "EUR":
            value = float(i["operationAmount"]["amount"])
            if i["operationAmount"]["currency"]["code"] == "EUR":
                url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={value}"
            elif i["operationAmount"]["currency"]["code"] == "USD":
                url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={value}"
            payload = {}
            headers = {"apikey": f"{API_KEY}"}
            response = requests.get(url, headers=headers, data=payload)
            status_code = response.status_code
            if status_code == 200:
                convert_amount = response.json()
                result = convert_amount["result"]
                return result
            elif status_code == 400:
                return "Запрос содержит синтаксическую ошибку или неверные параметры."
            elif status_code == 500:
                return "Ошибка на сервере"
