from vkbottle.bot import Blueprint, Message
from data.defs_orm import get_user, update_user

from sqlalchemy.exc import IntegrityError

from config import dump, all_promo_codes, even_and_odd2bool
from random import randint

bp = Blueprint("For private commands")
bp.on.vbml_ignore_case = True


@bp.on.private_message(text=['Я'])
async def info(msg: Message):
    try:
        user = await get_user(msg.from_id)
        await msg.answer(f'Твой никнейм: {user.nickname}\n'
                         f'На счету у тебя: {user.money}')
    except IntegrityError:
        await msg.answer('Сначала зарегистрируйтесь, напишите "Начать"')


@bp.on.private_message(text='Промокод <name_of_promo_code>')
async def info(msg: Message, name_of_promo_code: str):
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
    except IntegrityError:
        await msg.answer('Сначала зарегистрируйтесь, напишите "Начать"')


@bp.on.private_message(text='Рулетка <bet> <value_of_bet:int>')
async def info(msg: Message, bet, value_of_bet: int):
    try:
        user = await get_user(msg.peer_id)
        if value_of_bet < user.money:
            if bet == 'Чётноё':
                pass
            elif bet == 'Нечётное':
                pass
            num_rolled = randint(0, 32)
            if bet == 'Чётное' and num_rolled % 2 == 0 and num_rolled != 0:
                new_money = value_of_bet * 2
                await msg.answer(f'Вы выиграли: {new_money}\n'
                                 f'У вас на счету: {user.money + new_money}')

    except IntegrityError:
        await msg.answer('Сначала зарегистрируйтесь, напишите "Начать"')


@bp.on.private_message(text='Помощь')
async def info(msg: Message, name_of_promo_code: str):
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
    except IntegrityError:
        await msg.answer('Сначала зарегистрируйтесь, напишите "Начать"')
