from vkbottle.bot import Blueprint, Message

bp = Blueprint("Last check")


@bp.on.private_message(text='<msg>')
async def last_check(msg: Message):
    await msg.answer('Такой команды нет!')
