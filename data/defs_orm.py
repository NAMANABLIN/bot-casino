import asyncio

from data.database import async_db_session
from data.models import User
from os import path


async def init_app():
    await async_db_session.init()
    if not path.exists('users.sqlite'):
        await async_db_session.create_all()


async def create_user(id, **kwargs):
    await User.create(id=id, **kwargs)
    user = await User.get(id)
    return user


async def update_user(id, **kwargs):
    await User.update(id=id, **kwargs)
    user = await User.get(id)
    return user


async def get_user(id=None):
    user = await User.get(id)
    return user


loop = asyncio.get_event_loop()
task1 = loop.create_task(init_app())
loop.run_until_complete(asyncio.wait([task1]))
