import pytest

from src.decorators import log


def test_log():
    @log(filename="my_log.txt")
    def summa(x, y):
        return x + y

    result_summa = summa(1, 2)
    assert f"Функция my_function ок. Результат: {result_summa}" == "Функция my_function ок. Результат: 3"

    def sb(x, y):
        return x - y

    result_sb = sb(2, 1)
    assert f"Функция my_function ок. Результат: {result_sb}" == "Функция my_function ок. Результат: 1"

    def division_corr(x, y):
        return x / y

    result_division_corr = division_corr(4, 2)
    assert f"Функция my_function ок. Результат: {result_division_corr}" == "Функция my_function ок. Результат: 2.0"

    def div_zero(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        div_zero(2, 0)


def test_decorator_capsys(capsys):
    """Тестирование декоратора с выходом ошибки с фикстурой capsys"""
    with pytest.raises(Exception):
        my_func = my_function()
        captured = my_func.readouterr()
        assert captured.out == Exception


@log()
def faulty_function(x, y):
    return x / y


def test_faulty_function_logs_error(capsys):
    faulty_function(1, 0)
    captured = capsys.readouterr()
    assert "faulty_function error: division by zero" in captured.out
