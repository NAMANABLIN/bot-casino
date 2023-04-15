from vkbottle.bot import Blueprint, Message
from data.defs_orm import create_user, update_user, get_user
from aiosqlite import IntegrityError

bp = Blueprint("For private commands")
bp.on.vbml_ignore_case = True


@bp.on.private_message(text='Начать')
async def start(msg: Message):
    try:
        await create_user(msg.peer_id)
        await msg.answer('Добро пожаловать')
    except IntegrityError:
        await msg.answer('Ты уже зарегистрирован')


@bp.on.private_message(text=['Инфо', 'Инфо <id>'])
async def info(msg: Message, id: int = None):
    if id in None:
        await msg.answer(get_user(msg.peer_id))
    else:
        await msg.answer(get_user(id))
