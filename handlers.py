from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery
from aiogram import flags
from aiogram.fsm.context import FSMContext
from states import Gen
import keyboards
import text
from database import session, District
from sites import search_and_parse, parse_pills
router = Router()


def get_district_id(name):
    similar_district = session.query(District).filter(District.district_name.ilike(f'%{name}%')).first()

    if similar_district:
        district_id = similar_district.district_id
        return district_id
    else:
        return "Увы и ах"


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=keyboards.menu)


@router.callback_query(F.data == "menu")
async def menu(clbck: CallbackQuery):
    await clbck.message.answer(text.menu, reply_markup=keyboards.menu)


@router.callback_query(F.data == "find_chem")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.find_distr)
    await clbck.message.answer(text.district)


@router.message(Gen.find_distr)
@flags.chat_action("typing")
async def process_district(message: Message, state: FSMContext):
    await state.set_state(Gen.find_chem)
    name = message.text
    similar_district = session.query(District).filter(District.district_name.ilike(f'%{name}%')).first()

    if similar_district:
        district_id = similar_district.district_id
        with open('search.txt', 'w', encoding='utf-8') as file:
            file.write(str(district_id) + ' ')
        await message.answer('Какое лекарство хочешь найти?')
    else:
        await message.answer('Ты неправильно написал. Я не могу работать в таких условиях(', reply_markup=keyboards.menu)


@router.message(Gen.find_chem)
@flags.chat_action("typing")
async def process_district(message: Message, state: FSMContext):
    chem_name = message.text
    with open('search.txt', 'r', encoding='utf-8') as file:
        distr = file.read()
    await message.answer('Ща, 5 сек, я поищу что-то для тебя')
    result = search_and_parse(chem_name, distr)
    await message.answer(f' Вот некоторые аптеки, где ты можешь купить {chem_name} \n \n {result}')
    await message.answer(text.menu, reply_markup=keyboards.menu)


@router.callback_query(F.data == "pills_for")
async def input_text_prompt(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.pills_for)
    await clbck.message.answer(text.pills)


@router.message(Gen.pills_for)
@flags.chat_action("typing")
async def process_pills(message: Message, state: FSMContext):
    pills_name = message.text
    await message.answer('Ща, 5 сек, я поищу что-то для тебя')
    result = parse_pills(pills_name)
    await message.answer(f' {pills_name} примерно от следующего: \n \n {result}')
    await message.answer(text.menu, reply_markup=keyboards.menu)
