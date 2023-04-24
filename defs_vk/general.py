from vkbottle.bot import Blueprint, Message
from data.defs_orm import get_user, update_user

from config import reformat_money, link_handler
from sqlalchemy.exc import IntegrityError

bp = Blueprint("For games commands")
bp.on.vbml_ignore_case = True


@bp.on.message(text='Помощь')
async def info(msg: Message):
    try:
        pass
    except IntegrityError:
        await msg.answer('Сначала зарегистрируйтесь, напишите "Начать"')


@bp.on.message(text='Я')
async def info(msg: Message):
    try:
        user = await get_user(msg.from_id)
        await msg.answer(f'Приветствую, {user.nickname}!\n'
                         f'На счету у тебя: {user.money}')
    except IntegrityError:
        await msg.answer('Сначала зарегистрируйтесь, напишите "Начать"')


@bp.on.message(text=['Перевести <url> <money2transfer>',
                     'Передать <url> <money2transfer>'])
async def transfer(msg: Message, url: str, money2transfer: str):
    try:
        screen_name = link_handler(url)
        from_screen_name = (await bp.api.users.get(user_ids=msg.from_id, fields=["screen_name"]))[0].screen_name
        if not screen_name:
            await msg.answer(f'Не верно указана ссылка/упоминание'
                             f'\n\n'
                             f'Пример:\n'
                             f'перевести @{from_screen_name} 1000\n'
                             f'передать @{from_screen_name} 1к\n')
            return
        money2transfer = reformat_money(money2transfer)
        if not money2transfer:
            await msg.answer(f'Не верная сумма перевода'
                             f'\n\n'
                             f'перевести @{from_screen_name} 1000\n'
                             f'передать @{from_screen_name} 1к\n'
                             )
            return
        who2pass = (await bp.api.users.get(screen_name=screen_name))[0].id
        user2pass = await get_user(id=who2pass)
        user = await get_user(msg.from_id)
    except IntegrityError:
        await msg.answer('Сначала зарегистрируйтесь, напишите "Начать"')
