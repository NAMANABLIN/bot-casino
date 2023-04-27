from vkbottle.bot import Blueprint, Message
from data.defs_orm import get_user, update_user

from sqlalchemy.exc import NoResultFound

from config import even_bets, odd_bets, \
    zero_bets, all_bets, images, NO_ACCOUNT, WRONG_BET
from helper_funcs import reformat_money
from random import randint

bp = Blueprint("For games commands")
bp.on.vbml_ignore_case = True


@bp.on.message(text='Рулетка <bet> <value_of_bet>')
async def roulette(msg: Message, bet: str, value_of_bet: str):
    try:
        user = await get_user(msg.from_id)
        if user.iswork:
            await msg.answer('Ты на работе, не отвлекайся')
            return

        value_of_bet = reformat_money(value_of_bet, user.money)
        if value_of_bet <= 0:
            await msg.answer('Не верная сумма ставки')
            return

        num_rolled = randint(0, 36)
        win_or_lose = False  # если равен True, то игрок победил
        if value_of_bet > user.money:
            await msg.answer('У вас не достаточно средств')
            return
        try:  # если ставка - число, то выполняется этот блок кода
            bet = int(bet)
            if bet not in range(0, 37):
                await msg.answer(WRONG_BET)
                return
            elif num_rolled == bet:
                new_money = bet * 36
                win_or_lose = True

        except ValueError:  # если ставка - не число, то выполняется этот блок кода
            bet = bet.lower()
            if bet not in all_bets:
                await msg.answer(WRONG_BET)
                return
            if bet in zero_bets and num_rolled == 0:
                new_money = bet * 36
                win_or_lose = True
            elif bet in even_bets and num_rolled % 2 == 0:
                new_money = value_of_bet * 2
                win_or_lose = True
            elif bet in odd_bets and num_rolled % 2 != 0:
                new_money = value_of_bet * 2
                win_or_lose = True
        if win_or_lose:
            await update_user(msg.from_id, money=user.money + new_money)
            await msg.answer(f'Выпало число {num_rolled}\n\n'
                             f'Вы выиграли: {new_money}\n'
                             f'У вас на счету: {user.money}', attachment=images['win'][num_rolled])
        else:
            await update_user(msg.from_id, money=user.money - value_of_bet)
            await msg.answer(
                f'Выпало число {num_rolled}\n\n'
                f'Вы проиграли {value_of_bet}\n'
                f'У вас на счету: {user.money}', attachment=images['lose'][num_rolled])
    except NoResultFound:
        await msg.answer(NO_ACCOUNT)
