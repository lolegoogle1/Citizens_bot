import uuid

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ParseMode

from configurations.create_bot import dp
from configurations.messages import cancel_message, skip_message, example_info_message
from controlers.admin import send_data
from db.sqlite_db import sql_add_user_data, sql_add_record
from keyboards.markup import main_menu


class FSMPillage(StatesGroup):
    information = State()
    address = State()
    photo = State()
    video = State()
    contacts = State()


async def pillage_start(message: types.Message):
    await FSMPillage.information.set()
    await message.reply("Надайте нам всю інформацію, у текстовому вигляді, яка може нам допомогти."
                        f"{example_info_message}"
                        f"{cancel_message}", parse_mode=ParseMode.MARKDOWN, reply_markup=main_menu)


async def load_info(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['record_id'] = str(uuid.uuid4()).replace('-', '')
        data['information'] = message.text
    await FSMPillage.next()
    await message.reply("Введіть приблизну або точну адресу, у текстовому форматі, де стався випадок."
                        f"{cancel_message}", parse_mode=ParseMode.MARKDOWN, reply_markup=main_menu)


async def load_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
    await FSMPillage.next()
    await message.reply("Завантажте фото, на якому зафіксоване місце подій."
                        f"{cancel_message}"
                        f"{skip_message}", parse_mode=ParseMode.MARKDOWN, reply_markup=main_menu)


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMPillage.next()
    await message.reply("Завантажте відео, на якому зафіксоване дане угрупування."
                        f"{cancel_message}"
                        f"{skip_message}", parse_mode=ParseMode.MARKDOWN, reply_markup=main_menu)


async def load_video(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['video'] = message.video.file_id
    await FSMPillage.next()
    await message.reply("Надайте ваші контакти для детального вияснення ситуації."
                        "Натисніть на кпопку 'Надати контактні дані'"
                        f"{cancel_message}",
                        reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(
                            KeyboardButton('Надати контактні дані', request_contact=True)
                        ))


async def contacts(message: types.Message, state: FSMContext):
    current_user_id = message.contact.to_python()['user_id']
    async with state.proxy() as data:
        data['user_id'] = current_user_id

    await sql_add_user_data(message.contact.to_python())

    await sql_add_record(state)

    await message.reply("Дякую за співпрацю."
                        " У випадку неточності наданої вами інформації - ми з вами сконтактуємось.",
                        reply_markup=main_menu)

    await state.finish()

    await send_data(current_user_id)


@dp.message_handler(state=[FSMPillage.photo, FSMPillage.video], commands='skip')
@dp.message_handler(Text(equals="skip", ignore_case=True), state=[FSMPillage.photo, FSMPillage.video])
async def skip_handler(message: types.Message, state: FSMContext):
    if await state.get_state() == "FSMMark:photo":
        async with state.proxy() as data:
            data['photo'] = ""
        await FSMPillage.next()
        await message.reply("Завантажте відео, якщо таке є"
                            f"{cancel_message}"
                            f"{skip_message}", parse_mode=ParseMode.MARKDOWN, reply_markup=main_menu)
    elif await state.get_state() == "FSMMark:video":
        async with state.proxy() as data:
            data['video'] = ""
        await FSMPillage.next()
        await message.reply("Надайте ваші контакти для детального вияснення ситуації."
                            f"{cancel_message}", parse_mode=ParseMode.MARKDOWN,
                            reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(
                                KeyboardButton('Надати контактні дані', request_contact=True)))


def register_handlers_pillages(dsp: Dispatcher):
    dsp.register_message_handler(pillage_start, commands=['pillage'], state=None)
    dsp.register_message_handler(load_info, state=FSMPillage.information)
    dsp.register_message_handler(load_address, state=FSMPillage.address)
    dsp.register_message_handler(load_photo, content_types=['photo'], state=FSMPillage.photo)
    dsp.register_message_handler(load_video, content_types=['video'], state=FSMPillage.video)
    dsp.register_message_handler(contacts, state=FSMPillage.contacts)
