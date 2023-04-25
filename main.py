from vkbottle import Bot, load_blueprints_from_package

from config import VK_TOKEN

if __name__ == '__main__':
    bot = Bot(VK_TOKEN)

    for bp in load_blueprints_from_package('defs_vk'):
        bp.load(bot)

    bot.run_forever()
