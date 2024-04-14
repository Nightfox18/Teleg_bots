from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsForm
from core.middlewares.dbmeddleware import Request

async def get_form(message: Message, state:FSMContext):
    await message.answer(f'{message.from_user.first_name}. Начнем регистраци. \r\nДля начала веди свое имя')
    await state.set_state(StepsForm.GET_NAME)

async def get_name(message: Message, state: FSMContext):
    await message.answer(f'Твое имя:\r\n{message.text}\r\nТеперь введи свой номер телефона')
    await state.update_data(name=message.text)
    await state.set_state(StepsForm.GET_NUMBER)

async def get_number (message: Message, state:FSMContext):
    if len(message.text) == 11:
        await message.answer(f'Твой номер телефона :\r\n{message.text}\r\nТеперь введи свой адрес электронной почты')
        await state.update_data(number=message.text)
        await state.set_state(StepsForm.GET_MAIL)
    else:
        await message.answer('Введи коректный номер телефона')
async def get_mail (message: Message, state:FSMContext, request: Request):

    if "@" in message.text:
        await message.answer(f'Твоя электронная почта:\r\n{message.text}')
        context_data = await state.get_data()
        your_id = message.from_user.id
        your_nickname = message.from_user.first_name
        name = context_data.get("name")
        number = context_data.get(('number'))
        data_user = f'Вот твои данные\r\n' \
                    f'Твой ID: {your_id}\r\n' \
                    f'Твой никнейм: {your_nickname}\r\n' \
                    f'Имя: {name}\r\n' \
                    f'Телефон: {number}\r\n' \
                    f'Эл.почта: {message.text}'
        await message.answer(data_user)
        await request.add_data(message.from_user.id, message.from_user.first_name, name, number, message.text)
        await message.answer(f'Сохраненные данные в машине состояний:\r\n{str(context_data)}')
        await state.clear()
    else:
        await message.answer("Введи коректный адрес электронной почты")

