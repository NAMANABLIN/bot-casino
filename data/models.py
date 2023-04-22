from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import update as sqlalchemy_update
from sqlalchemy.future import select

from data.database import Base, async_db_session


class ModelAdmin:
    @classmethod
    async def create(cls, **kwargs):
        async_db_session.add(cls(**kwargs))
        await async_db_session.commit()

    @classmethod
    async def update(cls, id, **kwargs):
        query = (
            sqlalchemy_update(cls)
            .where(cls.id == id)
            .values(**kwargs)
            .execution_options(synchronize_session="fetch")
        )

        await async_db_session.execute(query)
        await async_db_session.commit()

    @classmethod
    async def get(cls, id):
        query = select(cls).where(cls.id == id)
        results = await async_db_session.execute(query)
        (result,) = results.one()
        return result


class User(Base, ModelAdmin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    nickname = Column(String, primary_key=True)
    money = Column(Integer, default=0)
    promocodes = Column(String, default="")
    sex = Column(Boolean, default=True, )

    __mapper_args__ = {"eager_defaults": True}

    def __repr__(self):
        return (
            f"<{self.__class__.__name__}("
            f"id={self.id}, "
            f"nickname={self.nickname}, "
            f"money={self.money}, "
            f"promocodes = {self.promocodes}, "
            f"sex={self.sex}"
            f")>"
        )
