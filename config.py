from dotenv import load_dotenv
from os import getenv, getcwd
from json import load, dump

load_dotenv()

VK_TOKEN = getenv("VK_MAIN")

admin_IDs = [221158750, 321346270]
sex2bool = {'Мужской': True,
            'Женский': False}

even_and_odd2bool = {
    'Чётное':True,
    'Нечётное':False
}
path = getcwd()
all_promo_codes = load(open(path +'\\'+ 'promocodes.json', 'rb'))