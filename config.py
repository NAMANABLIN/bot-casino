from dotenv import load_dotenv
from os import getenv, getcwd
from json import load, dump
import re

load_dotenv()

VK_TOKEN = getenv("VK_MAIN")

admin_IDs = [221158750, 321346270]

sex2bool = {'Мужской': True,
            'Женский': False}

even_bets = ['чет', 'чёт', 'чётное', 'четное', 'чётный', 'четный', 'even']
odd_bets = ['нечет', 'нечёт', 'нечётное', 'нечетное', 'нечётный', 'нечетный', 'odd']
zero_bets = ['зеро', 'ноль', 'zero']
all_bets = even_bets + odd_bets + zero_bets

path = getcwd()
all_promo_codes = load(open(path + '\\' + 'promocodes.json', 'rb'))


def reformat_money(value: str) -> int:
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
