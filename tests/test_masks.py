import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('value, expected', [
    ('64686473678894779589', '**9589'),
    ('646864736788947795', 'Недопустимая длина счета'),
    ('64686473678894779kjh', 'Счет содержит недопустимые символы'),
    ('64686473678894775576', '**5576'),
    ('64686473678894773324', '**3324'),
    ('646864736788947795775847', 'Недопустимая длина счета'),
    ('6t?.,:;3678894779kjh', 'Счет содержит недопустимые символы'),
])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected



@pytest.mark.parametrize('value, expected', [
    ('1596837868705199', '1596 83** **** 5199'),
    ('1596837868705', 'Недопустимая длина счета'),
    ('15968378 68705199', 'Счет содержит недопустимые символы'),
    ('1596837868705yrt', 'Счет содержит недопустимые символы'),
    ('159hg37868705yrt', 'Счет содержит недопустимые символы'),
    ('1596837868706587', '1596 83** **** 6587'),
])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected
