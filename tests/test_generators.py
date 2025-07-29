import pytest


from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


transaction = [
    {
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
    },
    {
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
    },
    {
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
    },
    {
        "operationAmount": {"amount": "56883.54", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод с карты на карту",
    },
    {
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
    },
]


@pytest.mark.parametrize(
    "transactions, currency, expected",
    [
        (
            transaction,
            "USD",
            {
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
            },
        ),
        (
            transaction,
            "EUR",
            {
                "operationAmount": {"amount": "56883.54", "currency": {"name": "EUR", "code": "EUR"}},
                "description": "Перевод с карты на карту",
            },
        ),
    ],
)
def test_filter_by_currency(transactions, currency, expected):
    assert next(filter_by_currency(transactions, currency)) == expected


def test_transaction_descriptions():
    assert next(transaction_descriptions(transaction)) == "Перевод организации"


def test_card_number_generator():
    assert next(card_number_generator(start=1, stop=10)) == "0000 0000 0000 0001"
