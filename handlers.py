from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message

import keyboards
import text

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=keyboards.menu)


@router.message(F.text == str())
async def menu(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=keyboards.menu)