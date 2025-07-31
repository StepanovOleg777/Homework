from typing import Iterable


def filter_by_currency(transactions: list, currency: str) -> Iterable:
    """Функция принимает список словарей и возвращает список только с валютой USD"""

    for i in transactions:
        if i["operationAmount"]["currency"]["code"] == currency:
            yield i


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

usd_transactions = filter_by_currency(transactions, "USD")

for transaction in usd_transactions:
    print(transaction)


def transaction_descriptions(transactions: list[dict]):
    """Генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""

    for transaction in transactions:
        result_trans_descr = transaction.get("description")
        yield result_trans_descr


gen = transaction_descriptions(transactions)

print(next(gen))
print(next(gen))

def card_number_generator(start=1, stop=9999999999999999):
    """Функция генерирует номер карты"""

    for gen_num in range(start, stop):
        len_numbers = 16 - len(str(gen_num))
        if gen_num <= 16:
            card_number_gen = ("0" * len_numbers) + str(gen_num)
            card_number_gen = (
                card_number_gen[:4]
                + " "
                + card_number_gen[4:8]
                + " "
                + card_number_gen[8:12]
                + " "
                + card_number_gen[-4:]
            )
            yield card_number_gen


card_gen = card_number_generator(start=1, stop=6)
for card_number in card_gen:
    print(card_number)
