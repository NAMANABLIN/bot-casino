from vkbottle.bot import Blueprint, Message

bp = Blueprint("For chat commands")
bp.on.vbml_ignore_case = True

@bp.on.chat_message(text='Привет')
async def start(msg: Message):
    await msg.answer('Ку')

