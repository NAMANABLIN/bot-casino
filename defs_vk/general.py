from vkbottle.bot import Blueprint, Message
from data.defs_orm import get_user, update_user

from helper_funcs import reformat_money, mention_handler
from sqlalchemy.exc import NoResultFound

from config import NO_ACCOUNT, HELP

bp = Blueprint("For general commands")
bp.on.vbml_ignore_case = True


@bp.on.message(text='Я')
async def info(msg: Message):
    try:
        user = await get_user(msg.from_id)
        await msg.answer(f'Приветствую, {user.nickname}!\n'
                         f'На счету у тебя: {user.money}')
    except NoResultFound:
        await msg.answer(NO_ACCOUNT)


@bp.on.message(text='Помощь')
async def show_help(msg: Message):
    await msg.answer(HELP)


@bp.on.message(text=['Перевести <mention> <money2transfer>',
                     'Передать <mention> <money2transfer>'])
async def transfer(msg: Message, mention: str, money2transfer: str):
    try:
        who2screen_name = mention_handler(mention)
        if not who2screen_name:
            from_screen_name = (await bp.api.users.get(
                user_ids=msg.from_id,
                fields=["screen_name"]))[0].screen_name
            await msg.answer(f'Не верно указана ссылка/упоминание'
                             f'\n\n'
                             f'Пример корректного ввода:\n'
                             f'перевести @{from_screen_name} 1000\n'
                             f'передать https://vk.com/{from_screen_name} 1к\n')
            return
        user = await get_user(msg.from_id)
        if user.iswork:
            await msg.answer('Ты на работе, не отвлекайся')
            return
        money2transfer = reformat_money(money2transfer, user.money)
        if not money2transfer:
            from_screen_name = (await bp.api.users.get(
                user_ids=msg.from_id,
                fields=["screen_name"]))[0].screen_name
            await msg.answer(f'Не верная сумма перевода'
                             f'\n\n'
                             f'Пример корректного ввода:\n'
                             f'перевести @{from_screen_name} 1000\n'
                             f'передать https://vk.com/{from_screen_name} 1к\n'
                             )
            return
        who2pass = await bp.api.users.get(screen_name=who2screen_name)
        if not who2pass:
            id_who2pass = int(who2screen_name[2:])
        else:
            id_who2pass = who2pass[0].id
        try:
            user2pass = await get_user(id=id_who2pass)
        except NoResultFound:
            await msg.answer('У этого пользователя нет аккаунта в боте')
            return
        if user2pass:
            if user.money >= money2transfer:
                await update_user(msg.from_id, money=user.money - money2transfer)
                await update_user(id_who2pass, money=user2pass.money + money2transfer)
                await msg.answer('Перевод совершён')
                await bp.api.messages.send(user_id=id_who2pass,
                                           message=f'[id{user.id}|{user.nickname}] перевёл вам {money2transfer}',
                                           random_id=0)
            else:
                await msg.answer('У вас не достаточно денег для перевода')
        else:
            await msg.answer('У пользователя, которому вы хотите отправить деньги нет аккаунта в боте')
    except NoResultFound:
        await msg.answer(NO_ACCOUNT)
