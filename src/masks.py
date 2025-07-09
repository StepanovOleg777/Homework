def get_mask_card_number(card_numder: str) -> str:
    """Функция маскирует цифры карты и разбивает на 4 блока"""
    if not card_numder.isdigit():
        return 'Счет содержит недопустимые символы'
    if len(card_numder) != 16:
        return "Недопустимая длина счета"
    masked_card = card_numder[:4] + " " + card_numder[4:6] + "**" + " **** " + card_numder[-4:]
    return masked_card

print(get_mask_card_number("1596837868705199"))
print(get_mask_card_number("1596837868705"))
print(get_mask_card_number("15968378 68705199"))
print(get_mask_card_number("1596837868705yrt"))


def get_mask_account(account_num: str):
    """Функция маскирует цифры счета, кроме последних четырех"""
    if len(account_num) != 20:
        return "Недопустимая длина счета"
    if not account_num.isdigit():
        return "Счет содержит недопустимые символы"
    mask = "**"
    result = str(mask + account_num[-4:])
    return result

print(get_mask_account("64686473678894779589"))
