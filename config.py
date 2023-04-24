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

