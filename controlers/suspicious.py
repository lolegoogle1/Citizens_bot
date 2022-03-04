import uuid

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ParseMode

from configurations.create_bot import dp
from configurations.messages import cancel_message, skip_message, example_info_message
from db.sqlite_db import sql_add_record, sql_add_user_data
from keyboards.markup import main_menu


class FSMSuspicious(StatesGroup):
    information = State()
    address = State()
    photo = State()
    video = State()
    contacts = State()


async def persons_start(message: types.Message):
    await FSMSuspicious.information.set()
    await message.reply("Надайте нам всю інформацію, у текстовому вигляді, яка може нам допомогти."
                        f"{example_info_message}"
                        f"{cancel_message}", parse_mode=ParseMode.MARKDOWN, reply_markup=main_menu)


async def load_info(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['record_id'] = str(uuid.uuid4()).replace('-', '')
        data['information'] = message.text
    await FSMSuspicious.next()
    await message.reply("Введіть приблизну, або точну адресу розсташування підозрілого угрупування"
                        f"{cancel_message}", parse_mode=ParseMode.MARKDOWN, reply_markup=main_menu)


async def load_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
    await FSMSuspicious.next()
    await message.reply("Завантажте фото, на якому зафіксоване дане угрупування, якщо є."
                        f"{cancel_message}"
                        f"{skip_message}", parse_mode=ParseMode.MARKDOWN, reply_markup=main_menu)


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMSuspicious.next()
    await message.reply("Завантажте відео, на якому зафіксоване дане угрупування, якщо є."
                        f"{cancel_message}"
                        f"{skip_message}", parse_mode=ParseMode.MARKDOWN, reply_markup=main_menu)


async def load_video(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['video'] = message.video.file_id
    await FSMSuspicious.next()
    await message.reply("Надайте ваші контакти для детального вияснення ситуації."
                        "\n\n Для відміни натисніть, або введіть команду /cancel \n"
                        , parse_mode=ParseMode.MARKDOWN,
                        reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(
                            KeyboardButton('Надати контактні дані', request_contact=True)
                        ))


async def contacts(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.contact.to_python()['user_id']

    await sql_add_user_data(message.contact.to_python())

    async with state.proxy() as data:
        await message.reply(str(data))

    await sql_add_record(state)

    await message.reply("Дякую за співпрацю. У випадку неточності наданої вами інформації - ми з вами сконтактуємось.")

    await state.finish()


@dp.message_handler(state=[FSMSuspicious.photo, FSMSuspicious.video], commands='skip')
@dp.message_handler(Text(equals="skip", ignore_case=True), state=[FSMSuspicious.photo, FSMSuspicious.video])
async def skip_handler(message: types.Message, state: FSMContext):
    if await state.get_state() == "FSMMark:photo":
        async with state.proxy() as data:
            data['photo'] = ""
        await FSMSuspicious.next()
        await message.reply("Завантажте відео, якщо таке є"
                            f"{cancel_message}"
                            f"{skip_message}", parse_mode=ParseMode.MARKDOWN, reply_markup=main_menu)
    elif await state.get_state() == "FSMMark:video":
        async with state.proxy() as data:
            data['video'] = ""
        await FSMSuspicious.next()
        await message.reply("Надайте ваші контакти для детального вияснення ситуації."
                            f"{cancel_message}", parse_mode=ParseMode.MARKDOWN,
                            reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(
                                KeyboardButton('Надати контактні дані', request_contact=True)))


def register_handlers_persons(dp: Dispatcher):
    dp.register_message_handler(persons_start, commands=['persons'], state=None)
    dp.register_message_handler(load_info, state=FSMSuspicious.information)
    dp.register_message_handler(load_address, state=FSMSuspicious.address)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMSuspicious.photo)
    dp.register_message_handler(load_video, content_types=['video'], state=FSMSuspicious.video)
    dp.register_message_handler(contacts, content_types=['contact'], state=FSMSuspicious.contacts)
