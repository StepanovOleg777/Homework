def get_mask_card_number(card_numder: str) -> str:
    """Функция маскирует цифры карты и разбивает на 4 блока"""
    masked_card = card_numder[:4] + " " + card_numder[4:6] + "**" + " **** " + card_numder[-4:]
    return masked_card

print(get_mask_card_number("1596837868705199"))



def get_mask_account(account_num: str):
    """Функция маскирует цифры счета, кроме последних четырех"""
    mask = "**"
    result = str(mask + account_num[-4:])
    return result

print(get_mask_account("64686473678894779589"))
