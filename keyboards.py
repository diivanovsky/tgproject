from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
menu = [
    [InlineKeyboardButton(text="Помоги найти лекарство", callback_data="find_chem")],
    [InlineKeyboardButton(text="Где ближайшие аптеки?", callback_data="nearest_chem")],
    [InlineKeyboardButton(text="От чего это лекарство?", callback_data="pills_for")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)

exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])