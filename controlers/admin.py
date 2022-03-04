from configurations.create_bot import bot
from creds import ADMIN_CHANNEL_ID
from db.sqlite_db import sql_get_data


async def send_data(user_id):
    data = await sql_get_data(user_id)
    if not data['photo_id'] == '':
        await bot.send_photo(ADMIN_CHANNEL_ID, data['photo_id'])
    if not data['video_id'] == '':
        await bot.send_video(ADMIN_CHANNEL_ID, data['video_id'])
    await bot.send_message(ADMIN_CHANNEL_ID, f"Дані користувача:\n\n"
                                             f"Ім'я користувача: {data['username']}\n"
                                             f"Телефон користувача: {data['phone_number']}\n\n"
                                             f"--------------------------------------------\n\n"
                                             f"Інформація яку надав користувач:\n\n"
                                             f"Опис ситуації: {data['information']}\n"
                                             f"Адреса: {data['address']}\n")