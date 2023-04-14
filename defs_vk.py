from config import VK_TOKEN
from aiosqlite import IntegrityError
from vkbottle.bot import Bot, Message
from defs_sql import update, updates, get, get_all, create
bot = Bot(token=VK_TOKEN)


@bot.on.private_message(text='Начать')
async def start(msg: Message):
    try:
        await create(msg.peer_id)
        await msg.answer('Привет')
    except IntegrityError:
        await msg.answer('Ты уже зарегистрирован')


@bot.on.private_message(text=['Инфо', 'Инфо <id>'])
async def info(msg: Message, id: int = None):
    if id is None:
        await msg.answer(await get_all('*'))
    else:
        await msg.answer(await get(id, '*'))
