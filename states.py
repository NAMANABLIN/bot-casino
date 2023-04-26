from vkbottle import CtxStorage, BaseStateGroup
from vkbottle import BaseStateGroup, CtxStorage


# здесь будут все стейты бота

class RegState(BaseStateGroup):
    NAME = 1
    SEX = 2


ctx = CtxStorage()
