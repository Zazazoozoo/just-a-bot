from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup (resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
kb.add(b1).insert(b2)

kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/sticker')
b4 = KeyboardButton('/photo')
b5 = KeyboardButton('/location')
kb2.add(b1).insert(b2).add(b3).insert(b4).add(b5)

ikb = InlineKeyboardMarkup(row_width=2)
ib = InlineKeyboardButton(text='❤️ ', callback_data='like')
ib1 = InlineKeyboardButton(text='👎🏿  ', callback_data='dislike')
ib2 = InlineKeyboardButton(text='Следующая фотография ', callback_data='random')
ib3 = InlineKeyboardButton(text='Перейти в главное меню ', callback_data='menu')
ikb.add(ib, ib1, ib2, ib3)