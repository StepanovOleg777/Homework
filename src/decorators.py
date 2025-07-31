import time
from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                time_1 = time.time()
                time_2 = time.time()
                result = func(*args, **kwargs)
                name_func = func.__name__
                if filename:
                    file = open(filename, "a", encoding="utf-8")
                    file.write(f"Начало: {time_1}" + "\n")
                    file.write(f"Функция {name_func} ок. Результат: {result}" + "\n")
                    file.write(f"Конец: {time_2}" + "\n")
                    file.write("\n")
                    file.close()
                else:
                    print(f"Начало: {time_1}")
                    print(f"{name_func} ok. Результат: {func(*args, **kwargs)}")
                    print(f"Конец: {time_2}")
            except Exception as e:
                result = None
                print(f"Начало: {time_1}")
                print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                print(f"Конец: {time_2}")
            except ZeroDivisionError:
                result = None
                print(f"Начало: {time_1}")
                print(f"{func.__name__} error: ZeroDivisionError. Inputs: {args}, {kwargs}")
                print(f"Конец: {time_2}")
            return result

        return wrapper

    return decorator
