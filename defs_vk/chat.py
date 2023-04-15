import sqlite3

from vkbottle.bot import Blueprint, Message
from data.defs_orm import create_user, update_user, get_user

bp = Blueprint("For chat commands")
bp.on.vbml_ignore_case = True


@bp.on.chat_message(text='Привет')
async def start(msg: Message):
    await msg.answer('Ку')


@bp.on.chat_message(text=['Передать <url> <money:int>', 'Передать <url>', 'Передать'])
async def other(msg: Message, url: str = None, money: int = 0):
    id = url[3:url.index('|')]
    print(msg.peer_id)
    money_user = (await get_user(id)).money
    print(money_user)