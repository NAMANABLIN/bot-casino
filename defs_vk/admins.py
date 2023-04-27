from vkbottle.bot import Blueprint, Message

from config import all_promo_codes, dump, path, admin_IDs

bp = Blueprint("For admins commands")
bp.on.vbml_ignore_case = True


# Хэндлер для добавления промокода в json файл
@bp.on.private_message(text='Добавить <name_of_promo_code> <amount_of_money:int>')
async def promo_code_add(msg: Message, name_of_promo_code: str, amount_of_money: int):
    if msg.peer_id in admin_IDs:
        try:
            print(all_promo_codes[name_of_promo_code.upper()])
            await msg.answer('Такой промокод уже существует')
        except KeyError:
            all_promo_codes[name_of_promo_code.upper()] = amount_of_money  # все промокоды пишутся в верхнем регистре
            dump(all_promo_codes, open(f'{path}//promocodes.json', 'w'), indent=2, ensure_ascii=True)
            await msg.answer('Промокод добавлен')


# показать все промокоды из json
@bp.on.private_message(text='Все промокоды')
async def show_promo_codes(msg: Message):
    if msg.from_id in admin_IDs:
        await msg.answer(all_promo_codes)
