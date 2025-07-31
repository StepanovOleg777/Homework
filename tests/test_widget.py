import pytest


from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("value, expected", [
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


def test_get_date(date):
    assert get_date(date) == "11.03.2024"
