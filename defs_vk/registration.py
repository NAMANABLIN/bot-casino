from vkbottle.bot import Blueprint, Message

from data.defs_orm import create_user, get_user, update_user

from sqlalchemy import exc
from keyboards import keyb_reg
from states import ctx, RegState
from config import sex2bool

bp = Blueprint("Registration")
bp.on.vbml_ignore_case = True


@bp.on.private_message(text="Начать")
async def start(msg: Message):
    try:
        await bp.state_dispenser.set(msg.peer_id, RegState.NAME)
        return "Добро пожаловать!\nВведи свой никнейм"
    except exc.IntegrityError:
        await bp.state_dispenser.set(msg.peer_id, RegState.NAME)
        return "Добро пожаловать!\nВведи свой никнейм"


@bp.on.private_message(state=RegState.NAME)
async def awkward_handler(msg: Message):
    ctx.set('name', msg.text)
    await bp.state_dispenser.set(msg.peer_id, RegState.SEX)
    await msg.answer('Какой ваш пол?', keyboard=keyb_reg.keyb_sex_choice)
    return 'Принимаются только варианты на кнопках'


@bp.on.private_message(state=RegState.SEX)
async def awkward_handler(msg: Message):
    message_text = msg.text
    if message_text == 'Мужской' or message_text == 'Женский':
        await create_user(msg.peer_id, nickname=ctx.get('name'), sex=sex2bool[message_text])
        return 'Регистрация прошла успешно!'
    else:
        await msg.answer('Принимаются только варианты на кнопках', keyboard=keyb_reg.keyb_sex_choice)
        await bp.state_dispenser.set(msg.peer_id, RegState.SEX)
