import asyncio

from data.database import async_db_session
from data.models import User
from sqlalchemy import exc


async def init_app():
    await async_db_session.init()


async def create_user(id, nickname):
    await User.create(id=id, nickname=nickname)
    user = await User.get(id)
    return user.id


async def update_user(id, money=None, promocodes=None, nickname=None):
    await User.update(id, nickname=nickname)
    user = await User.get(id)
    return user.nickname


async def get_user(id=None):
    try:
        info = await User.get(id)
        return info
    except exc.NoResultFound:
        return "Пользователь не зарегистрирован"


loop = asyncio.get_event_loop()
task1 = loop.create_task(init_app())
loop.run_until_complete(asyncio.wait([task1]))
