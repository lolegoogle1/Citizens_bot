from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


mark = KeyboardButton("Повідомити про мітку")
suspicious = KeyboardButton("Повідомити про підозрілу особу")
pillage = KeyboardButton("Повідомити про випадки мародерства")

"""address = KeyboardButton("Опишіть приблизне місце події, або вкажіть адресу.")
photo = KeyboardButton("Надішліть фото з місця події, якщо таке є.")
video = KeyboardButton("Надішліть відео з місця події, якщо таке є.")
info = KeyboardButton("Надайте будь-яку додаткову інформацію, яка може нам допомогти.")
"""

main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(mark, suspicious, pillage)