from vkbottle.bot import Blueprint, Message
from data.defs_orm import get_user, update_user

from sqlalchemy.exc import NoResultFound

from config import all_promo_codes

from random import randint

from asyncio import sleep

bp = Blueprint("For private commands")
bp.on.vbml_ignore_case = True# чтобы игнорировался регистр букв


@bp.on.private_message(text='Промокод <name_of_promo_code>')
async def promo_use(msg: Message, name_of_promo_code: str):
    try:
        user = await get_user(msg.peer_id)
        if name_of_promo_code in all_promo_codes.keys():
            user_promocodes = user.promocodes.split()
            if name_of_promo_code in user_promocodes:
                await msg.answer(f'Вы уже вводили этот промокод')
            else:
                value = all_promo_codes[name_of_promo_code]
                user_promocodes.append(name_of_promo_code)
                await update_user(msg.peer_id,
                                  money=user.money + value,
                                  promocodes=' '.join(user_promocodes))
                await msg.answer(f'Поздравляю! Вы получили {value}')
        else:
            await msg.answer(f'Такого промокода не сущетсвует')
    except NoResultFound:
        await msg.answer('Сначала зарегистрируйтесь, напишите "Начать"')


@bp.on.private_message(text='Работа')
async def work_handler(msg: Message):
    try:
        user = await get_user(msg.from_id)
        if user.iswork:
            await msg.answer('Вы уже работаете, зарплата будет четь позже')
        else:
            random_salary = randint(1, 10) * 1000
            await update_user(id=msg.from_id, iswork=True)
            await msg.answer(f'Нужно будет перетаскать ящики из грузовика, после получишь {random_salary}')
            await sleep(5 * 60)
            await msg.answer(f'Перетащил, значит вот {random_salary}, всё честно!')
            await update_user(id=msg.from_id, money=user.money + random_salary, iswork=False)
    except NoResultFound:
        await msg.answer('Сначала зарегистрируйтесь, напишите "Начать"')
