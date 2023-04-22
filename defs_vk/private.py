from vkbottle.bot import Blueprint, Message
from data.defs_orm import get_user, update_user

from sqlalchemy.exc import IntegrityError

from config import dump, all_promo_codes, even_bets, odd_bets, zero_bets, all_bets
from random import randint

bp = Blueprint("For private commands")
bp.on.vbml_ignore_case = True


@bp.on.private_message(text=['Я'])
async def info(msg: Message):
    try:
        user = await get_user(msg.from_id)
        await msg.answer(f'Приветствую, {user.nickname}!\n'
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
async def roulette(msg: Message, bet: str, value_of_bet: int):
    try:
        user = await get_user(msg.peer_id)
        num_rolled = randint(0, 36)
        win_or_lose = False
        if value_of_bet > user.money:
            await msg.answer('У вас не достаточно средств')
            return
        try:
            bet = int(bet)
            if num_rolled not in range(0, 37):
                await msg.answer(f'Такой ставки не существует\n'
                                 f'Чтобы поставить на чётное число вы должны прописать (x2):\n'
                                 f'{(", ".join(even_bets)).capitalize()}\n\n'
                                 f'На нечетное (x2):\n'
                                 f'{(", ".join(odd_bets)).capitalize()}\n\n'
                                 f'Так же вы можеть поставить на число (x32):\n'
                                 f'От 0 до 36, писать нужно цифрами, но так же можно написать "зеро"')
                return
            elif num_rolled == bet:
                new_money = bet * 36
                win_or_lose = True

        except ValueError:
            bet = bet.lower()
            if bet not in all_bets:
                await msg.answer(f'Такой ставки не существует\n'
                                 f'Чтобы поставить на чётное число вы должны прописать (x2):\n'
                                 f'{(", ".join(even_bets)).capitalize()}\n\n'
                                 f'На нечетное (x2):\n'
                                 f'{(", ".join(odd_bets)).capitalize()}\n\n'
                                 f'Так же вы можеть поставить на число (x32):\n'
                                 f'От 0 до 36, писать нужно цифрами, '
                                 f'но при ставке на 0 так же можно написать: {(", ".join(odd_bets))}')
                return
            if num_rolled == 0:
                if bet in zero_bets:
                    new_money = bet * 36
                    win_or_lose = True
            elif bet in even_bets:
                if num_rolled % 2 == 0:
                    new_money = value_of_bet * 2
                    win_or_lose = True
            elif bet in odd_bets:
                if num_rolled % 2 != 0:
                    new_money = value_of_bet * 2
                    win_or_lose = True
        print(user.money, type(user.money))
        if win_or_lose:

            await update_user(msg.peer_id, money=user.money + new_money)
            await msg.answer(f'Выпало число {num_rolled}\n\n'
                             f'Вы выиграли: {new_money}\n'
                             f'У вас на счету: {user.money + new_money}')
        else:
            await update_user(msg.peer_id, money=user.money - value_of_bet)
            await msg.answer(
                f'Выпало число {num_rolled}\n\n'
                f'Вы проиграли {value_of_bet}\n'
                f'У вас на счету: {user.money - value_of_bet}')
    except IntegrityError:
        await msg.answer('Сначала зарегистрируйтесь, напишите "Начать"')


@bp.on.private_message(text='Помощь')
async def info(msg: Message, name_of_promo_code: str):
    try:
        user = await get_user(msg.peer_id)
        if name_of_promo_code in all_promo_codes.keys():
            promo_codes_used_by_user = user.promocodes.split()
            if name_of_promo_code in promo_codes_used_by_user:
                await msg.answer(f'Вы уже вводили этот промокод')
            else:
                value = all_promo_codes[name_of_promo_code]
                promo_codes_used_by_user.append(name_of_promo_code)
                await update_user(msg.peer_id,
                                  money=user.money + value,
                                  promocodes=' '.join(promo_codes_used_by_user))
                await msg.answer(f'Поздравляю! Вы получили {value}')
        else:
            await msg.answer(f'Такого промокода не сущетсвует')
    except IntegrityError:
        await msg.answer('Сначала зарегистрируйтесь, напишите "Начать"')
