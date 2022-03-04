from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.utils.markdown import text, bold

from configurations.messages import welcome_message
from controlers import mark
from configurations.create_bot import dp
from keyboards.markup import main_menu
from db import sqlite_db


async def on_startup(_):
    print("Бот працює")
    sqlite_db.sql_start()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(welcome_message, parse_mode=ParseMode.MARKDOWN, reply_markup=main_menu)


@dp.message_handler(state="*", commands='cancel')
@dp.message_handler(Text(equals="cancel", ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ви відмінили цей крок. Почніть спочатку.', reply_markup=main_menu)


mark.register_handlers_marks(dp)


@dp.message_handler()
async def menu_buttons(message: types.Message):
    """
    This handler will be called when user sends any message except the commands
    """
    if message.text == "Надати інформацію":
        await message.reply("Натисність на, або введіть самостійно команду /provide_information", reply_markup=main_menu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
