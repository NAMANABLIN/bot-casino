from vkbottle.bot import Blueprint, Message

from config import all_promo_codes, dump, path, admin_IDs

bp = Blueprint("For admins commands")
bp.on.vbml_ignore_case = True


@bp.on.private_message(text='Добавить <name_of_promo_code> <amount_of_money:int>')
async def promo_code_add(msg: Message, name_of_promo_code: str, amount_of_money: int):
    print(2)
    if msg.peer_id in admin_IDs:
        print(1)
        try:
            print(all_promo_codes[name_of_promo_code.upper()])
            await msg.answer('Такой промокод уже существует')

        except KeyError:
            all_promo_codes[name_of_promo_code.upper()] = amount_of_money
            dump(all_promo_codes, open(f'{path}\\promocodes.json', 'w'), indent=2, ensure_ascii=True)
            await msg.answer('Промокод добавлен')
