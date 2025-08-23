import logging
import datetime


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_numder: str) -> str:
    """Функция маскирует цифры карты и разбивает на 4 блока"""
    if not card_numder.isdigit():
        logger.info(f"Счет содержит недопустимые символы")
        return "Счет содержит недопустимые символы"
    if len(card_numder) != 16:
        logger.info(f"Недопустимая длина счета")
        return "Недопустимая длина счета"
    masked_card = card_numder[:4] + " " + card_numder[4:6] + "**" + " **** " + card_numder[-4:]
    logger.info(f"Корректный номер")
    return masked_card


print(get_mask_card_number("1596837868705199"))


def get_mask_account(account_num: str):
    """Функция маскирует цифры счета, кроме последних четырех"""
    if len(account_num) != 20:
        logger.info(f"Недопустимая длина счета")
        return "Недопустимая длина счета"
    if not account_num.isdigit():
        logger.info(f"Счет содержит недопустимые символы")
        return "Счет содержит недопустимые символы"
    mask = "**"
    result = str(mask + account_num[-4:])
    logger.info(f"Корректный номер")
    return result


print(get_mask_account("64686473678894779589"))
