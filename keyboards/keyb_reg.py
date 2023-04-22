from vkbottle import Keyboard, KeyboardButtonColor, Text

keyb_sex_choice = Keyboard(one_time=True, inline=False)

keyb_sex_choice.add(Text("Мужской"), color=KeyboardButtonColor.PRIMARY)
keyb_sex_choice.add(Text("Женский"), color=KeyboardButtonColor.NEGATIVE)