from dotenv import load_dotenv
from os import getenv
load_dotenv()

VK_TOKEN = getenv("VK_MAIN")

DATABASE = 'users.db'
CREATE = 'INSERT INTO users' \
         '(id, money, promocodes) ' \
         'VALUES({}, 0, "")'
