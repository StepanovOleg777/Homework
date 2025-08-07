import pytest

from src.decorators import log, second_fun

from src.decorators import my_function

@log()
def test_my_function_console_output(capsys):
    my_function(2, 3)
    captured = capsys.readouterr()
    assert "Функция my_function ок." in captured.out

def test_log():
    with pytest.raises(Exception):
        second_fun(2,0)
