import pytest
from src.decorators import log


@log()
def my_function(x, y):
    return x / y


# Тест на успешное выполнение функции


def test_my_function_success(capsys):
    result = my_function(4, 2)
    assert result == 2
    captured = capsys.readouterr()
    assert "my_function ok. Результат: 2" in captured.out


# Тест на обработку ошибки деления на ноль


def test_my_function_division_by_zero(capsys):
    with pytest.raises(ZeroDivisionError):
        my_function(4, 0)
    captured = capsys.readouterr()
    assert "my_function error: division by zero. Inputs: (4, 0), {}" in captured.out
