from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


give_info_btn = KeyboardButton("Надати інформацію")

main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(give_info_btn)
