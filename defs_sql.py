import aiosqlite
from config import DATABASE, CREATE


async def update(user_id, column, content):
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute(f'UPDATE users'
                              f'  SET {column} = {content}'
                              f'    WHERE id = {user_id}') as cursor:
            await db.commit()


async def updates(user_id, columns):
    async with aiosqlite.connect(DATABASE) as db:
        for column, content in columns:
            async with db.execute(f'UPDATE users'
                                  f'  SET {column} = {content}'
                                  f'    WHERE id = {user_id}') as cursor:
                await db.commit()


async def get(user_id, column):
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute(f'SELECT {column} FROM users'
                              f'  WHERE id = {user_id}') as cursor:
            ans = await cursor.fetchone()
    return ans[0]


async def get_all(column='id', like='%'):
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute(f'SELECT {column} FROM users'
                              f'  WHERE {column} LIKE "{like}"') as cursor:
            ans = await cursor.fetchall()
    return ans


async def create(user_id):
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute(CREATE.format(user_id)) as cursor:
            await db.commit()

# async def check(user_id):
#     async with aiosqlite.connect('users_from_tg.db') as db:
#         async with db.execute(f'SELECT id FROM users'
#                               f'  WHERE id LIKE "{user_id}"') as cursor:
#             ans = await cursor.fetchone()
#     if ans is None:
#         await create(user_id)
