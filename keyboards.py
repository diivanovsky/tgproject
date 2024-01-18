from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)


menu = [
    [InlineKeyboardButton(text="Помоги найти лекарство", callback_data="find_chem")],
    [InlineKeyboardButton(text="От чего это лекарство?", callback_data="pills_for")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)

district = [
    [InlineKeyboardButton(text="Заводской", callback_data="zavod"),
     InlineKeyboardButton(text="Партизанский", callback_data="partiz")],
    [InlineKeyboardButton(text="Советский", callback_data="sovet"),
     InlineKeyboardButton(text="Центральный", callback_data="centr")],
    [InlineKeyboardButton(text="Московский", callback_data="mosk"),
     InlineKeyboardButton(text="Ленинский", callback_data="lenin")],
    [InlineKeyboardButton(text="Первомайский", callback_data="perv"),
     InlineKeyboardButton(text="Фрунзенский", callback_data="frunz")],
    [InlineKeyboardButton(text="Октябрьский", callback_data="okt"),
     InlineKeyboardButton(text="НАЗАД", callback_data="menu")]
]
district = InlineKeyboardMarkup(inline_keyboard=district)

