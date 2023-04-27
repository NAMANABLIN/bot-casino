# здесь будут все функции которые помогают улучшить работу скриптов

def reformat_money(value: str, full_money: int) -> int:
    if value in ['всё', 'все']:
        return full_money
    try:
        value = int(value)
        return value
    except ValueError:
        value = list(value)

        for i, x in enumerate(value):
            if x in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'k', 'к']:
                if x.lower() in ['k', 'к']:
                    value[i] = '000'
            else:
                return False
        return int(''.join(value))


def mention_handler(mention: str):
    if '/' in mention:  # определяет упоминание пользователя ссылка ли
        return mention[mention.rfind('/') + 1:]
    elif '|' in mention:  # определяет упоминание пользователя упоминание в чате ли
        return mention[1:mention.find('|')]
    else:
        return False
