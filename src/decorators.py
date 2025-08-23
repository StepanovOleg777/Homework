import time


def log(filename=None):
    """Декоратор логирует данные"""

    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                time_1 = time.time()
                result = func(*args, **kwargs)
                time_2 = time.time()
                name_func = func.__name__
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(
                            f"Начало: {time_1} \nФункция {name_func} ок. Результат: {result}\nКонец: {time_2}\n\n"
                        )
                        file.close()
                else:
                    print(f"Начало: {time_1} \nФункция {name_func} ок. Результат: {result}\nКонец: {time_2}")
            except Exception as e:
                name_func = func.__name__
                if filename:
                    file = open(filename, "a", encoding="utf-8")
                    file.write(f"{name_func} error: {e}. Inputs: {args}, {kwargs}")
                    file.close()
                    return f"{name_func} error: {e}. Inputs: {args}, {kwargs}"
                else:
                    print(f"{name_func} error: {e}. Inputs: {args}, {kwargs}")

        return wrapper

    return my_decorator


# @log(filename="mylog.txt")
@log()
def my_function(x, y):
    return x + y


@log()
def second_fun(x, y):
    return x / y


second_fun(5, 1)
