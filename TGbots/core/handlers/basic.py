from aiogram import Bot
from aiogram.types import Message
from core.keyboards.Reply import get_reply_keyboard


async def get_start (message: Message, bot:Bot):
    await message.answer(f'Привет <b>{message.from_user.first_name}</b>.'
                         f'\r\nЯ бот сервиса <b>FoxAuto</b>.\r\nДля дальнейшей работы необходимо зарегистрироваться'
                         f'\r\n Для этого выполни команду /form')