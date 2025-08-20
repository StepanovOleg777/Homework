def mask_account_card(card_info: str) -> str:
    """Функция принимает информацию о карте и маскирует ее номер или счет"""
    card_type_list = []
    card_numb_list = []
    card_info_list = card_info.split()


    # Применяем соответствующую маскировку
    for string in card_info_list:
        if string.isalpha():
            card_type_list.append(string)
    card_type = " ".join(card_type_list)

    #Получаем замаскированый номер карты
    for i in card_info_list:
        if i.isdigit():
            card_numb_list.append(i)
    numb_type = " ".join(card_numb_list)

    for numb in card_info_list:
        if 'Счет' in card_info_list:
            return f"{card_type} {'**' + numb_type[-4:]}"
        elif 'Счет' not in card_info_list:
            return f"{card_type} {numb_type[:4] + " " + numb_type[4:6] + "**" + " **** " + numb_type[-4:]}"




def get_date(date_str: str) -> str:
    """Функция реформатирует дату"""
    date_list = date_str.split("-", 2)
    date_list[2] = date_list[2][:2]
    date_list_reverse = ".".join(date_list[::-1])
    return date_list_reverse


