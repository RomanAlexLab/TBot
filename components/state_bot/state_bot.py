from aiogram.fsm.state import State, StatesGroup


class StateBot(StatesGroup):
    step_zero = State()
    login = State()
    password = State()