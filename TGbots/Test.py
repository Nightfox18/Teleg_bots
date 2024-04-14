import asyncio
import asyncpg
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from core.settings import settings
from core.utils.commands import set_commands
from core.handlers.basic import get_start
from core.handlers import form
from core.utils.statesform import StepsForm
from core.middlewares.dbmeddleware import DbSession

bot = Bot(token=settings.bots.bot_token, parse_mode="HTML")

async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text="Бот запущен!")

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Бот остановлен")

async def create_pool():
    return await asyncpg.create_pool(
        user='postgres',
        password='123',
        database='Testbot',
        host='localhost',
        port = 5432,
        command_timeout=60
    )

async def connect_to_db():
    await asyncpg.connect(
        user='postgres',
        password='123',
        database='Testbot',
        host='localhost',
        port = 5432,
        command_timeout=60
    )

async def get_data_from_db():
    conn = await asyncpg.connect(
        user='postgres',
        password='123',
        database='Testbot',
        host='localhost'
    )
    query = "SELECT * FROM now_ativity LIMIT 3"
    photos = conn.fetchall(query)

    await conn.close()

    return photos

async def get_last_item_with_photos():
    conn = await asyncpg.connect(
        user='postgres',
        password='123',
        database='Testbot',
        host='localhost'
    )
    query = "SELECT * FROM now_ativity ORDER BY id DESK LIMIT1"

    result = await conn.fetchall(query)

    if not result:
        return "Элементы не найден в БД"

    last_item = result[0]

    photos_query = "SELECT photo_url FROM last_activity WHERE item_id = $1"
    photos = await conn.flechall(photos_query, last_item["id"])

    await conn.close()

    photos_urls = [photo['photo_url'] for photo in photos]
    return last_item, photos_urls


async def send_now_activity (bot, chat_id):
    photos = await get_data_from_db()

    for photo in photos:
        photo_id = photo.get('id')
        photo_tittle = photo.get('title')
        photo_url = photo.get('url')

        await bot.send_photo(chat_id, photo_url, caption = photo_tittle)

async def send_coupon(message:Message):
    send = await connect_to_db()
    query = "SELECT photo_url FROM photos ORDER BY random() LIMIT 1"
    photo_url = await send.fetchall(query)
    await bot.send_photo(message.chat.id, photo=photo_url)


async def start():
    bot = Bot(token=settings.bots.bot_token, parse_mode="HTML")
    dp = Dispatcher()
    pool_connect = await create_pool()

    dp.message.register(form.get_form, Command(commands="form"))
    dp.message.register(form.get_name, StepsForm.GET_NAME)
    dp.message.register(form.get_number, StepsForm.GET_NUMBER)
    dp.message.register(form.get_mail, StepsForm.GET_MAIL)
    dp.message.register(get_start, CommandStart)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())