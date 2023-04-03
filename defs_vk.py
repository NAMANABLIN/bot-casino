from config import VK_TOKEN
from defs_sql import update, updates, get, get_all, create
from aiosqlite import IntegrityError
from vkbottle.bot import Bot, Message

import sys

bot = Bot(token=VK_TOKEN)


@bot.on.private_message(text='Начать')
async def start(msg: Message):
    try:
        await create(msg.peer_id)
        await msg.answer('Привет')
    except IntegrityError:
        await msg.answer('Ты уже зарегестрирован')
