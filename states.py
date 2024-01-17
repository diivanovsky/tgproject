from aiogram.fsm.state import StatesGroup, State


class Gen(StatesGroup):
    find_distr = State()
    find_chem = State()
    pills_for = State()
    nearest_chem = State()