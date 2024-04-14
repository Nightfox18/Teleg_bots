from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text="Зарегистрироваться")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup(resize_keyboard = True, one_time_keyboard=True,
                               input_field_placeholder="Выбери дейтсвие")

def get_work_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text="Актуальные работы")
    keyboard_builder.button(text="Последняя выполненная работа")
    keyboard_builder.button(text="Забрать скидку")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup(resize_keyboard = True, one_time_keyboard=True,
                               input_field_placeholder="Выбери дейтсвие")