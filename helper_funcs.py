def reformat_money(value: str, full_money:int) -> int:
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


def link_handler(url: str):
    if '/' in url:
        return url[url.rfind('/'):]
    elif '|' in url:
        return url[1:url.find('|')]
    else:
        return False
