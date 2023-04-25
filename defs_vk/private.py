from vkbottle.bot import Blueprint, Message
from data.defs_orm import get_user, update_user

from sqlalchemy.exc import IntegrityError

from config import all_promo_codes

bp = Blueprint("For private commands")
bp.on.vbml_ignore_case = True


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
    except IntegrityError:
        await msg.answer('Сначала зарегистрируйтесь, напишите "Начать"')
