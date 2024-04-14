from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    GET_NAME= State()
    GET_NUMBER=State()
    GET_MAIL =State()
