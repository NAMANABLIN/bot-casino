from vkbottle.bot import Blueprint, Message
from data.defs_orm import get_user, update_user

from sqlalchemy.exc import IntegrityError

from config import even_bets, odd_bets, \
    zero_bets, all_bets, reformat_money
from random import randint

bp = Blueprint("For games commands")
bp.on.vbml_ignore_case = True


@bp.on.message(text='Рулетка <bet> <value_of_bet>')
async def roulette(msg: Message, bet: str, value_of_bet: str):
    try:
        value_of_bet = reformat_money(value_of_bet)
        if not value_of_bet:
            await msg.answer('Не верная сумма ставки')
            return

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
        if win_or_lose:
            await update_user(msg.peer_id, money=user.money + new_money)
            await msg.answer(f'Выпало число {num_rolled}\n\n'
                             f'Вы выиграли: {new_money}\n'
                             f'У вас на счету: {user.money}')
        else:
            await update_user(msg.peer_id, money=user.money - value_of_bet)
            await msg.answer(
                f'Выпало число {num_rolled}\n\n'
                f'Вы проиграли {value_of_bet}\n'
                f'У вас на счету: {user.money}')
    except IntegrityError:
        await msg.answer('Сначала зарегистрируйтесь, напишите "Начать"')


#TODO: Кости