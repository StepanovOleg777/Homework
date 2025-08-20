import json
import logging


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def input_transaction(input_list):
    """Функция возвращает список словарей с данными о финансовых транзакциях
    из json-файла."""
    logger.info("Запуск функции `reading_json_file`")
    try:
        with open(input_list, "r", encoding="utf-8") as f:
            logger.info("открыт файл")
            transaction = json.load(f)
            logger.info("Если файл список, всё ок")
        return transaction
    except json.JSONDecodeError:
        logger.info("Возврат пустого списка, если не преобразовался файл")
        return []
    except FileNotFoundError:
        logger.info("Возврат пустого списка, если не найдёт файл")
        return []
    except TypeError:
        logger.info("Возвращаем пустой список")
        return []


