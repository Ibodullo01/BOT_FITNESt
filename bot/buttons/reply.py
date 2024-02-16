from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def menu_btn():

    k1 = KeyboardButton(text = 'Filial 📍')
    k2 = KeyboardButton(text = 'Start ✅')
    k3 = KeyboardButton(text = '🔙 back')
    k4 = KeyboardButton(text = 'News')
    design = [
        [k1 , k2],
        [k3],
        [k4]
    ]
    return ReplyKeyboardMarkup(keyboard=design , resize_keyboard=True)

def menu_btn_start():

    k1 = KeyboardButton(text = 'Woman 🧍‍♀️')
    k2 = KeyboardButton(text = 'Men 🧍‍♂️')
    k3 = KeyboardButton(text = '🔙 back')
    design = [
        [k1 , k2],
        [k3]

    ]
    return ReplyKeyboardMarkup(keyboard=design , resize_keyboard=True)



def woman_btn():
    k1 = KeyboardButton(text='1 oy')
    k2 = KeyboardButton(text='2 oy')
    k3 = KeyboardButton(text='3 oy')
    design = [
        [k1, k2],
        [k3]

    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)