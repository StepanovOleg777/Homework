import pytest

from src.masks import get_mask_account


@pytest.mark.parametrize('value, expected', [
    ('64686473678894779589', '**9589'),
    ('646864736788947795', 'Недопустимая длина счета'),
    ('64686473678894779kjh', 'Счет содержит недопустимые символы'),

])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected