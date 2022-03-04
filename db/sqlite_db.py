import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('test_bot.db')
    cur = base.cursor()
    if base:
        print("Database connected OK!")
    base.execute("PRAGMA foreign_keys=ON")
    base.execute("CREATE TABLE IF NOT EXISTS"
                 " users("
                 "phone_number STRING(250), name STRING(250),"
                 " telegram_id INTEGER PRIMARY KEY)"
                 )
    base.execute("CREATE TABLE IF NOT EXISTS "
                 "records(record_id STRING(250) PRIMARY KEY,"
                 "information TEXT, address TEXT, photo_id STRING(250), video_id STRING(250),"
                 "user_id INTEGER,"
                 "FOREIGN KEY (user_id) REFERENCES users (telegram_id) ON UPDATE CASCADE ON DELETE CASCADE)")

    base.commit()


async def sql_add_user_data(data):
    telegram_id = data['user_id']

    cur.execute(f'SELECT telegram_id FROM users WHERE telegram_id == {telegram_id}')
    try:
        db_data = cur.fetchone()[0]
        if db_data == telegram_id:
            return
    except TypeError:
        print("There is no such record in the db!")

    cur.execute('INSERT INTO users VALUES (?, ?, ?)', tuple(data.values()))
    base.commit()


async def sql_add_record(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO records VALUES (?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_get_data(user_id):
    data_to_send = dict()
    cur.execute(f'SELECT '
                f'  users.name, '
                f'  users.phone_number '
                f'FROM records '
                f'JOIN users ON users.telegram_id == records.user_id '
                f'WHERE records.user_id == {user_id};')
    data_to_send["username"], data_to_send["phone_number"] = cur.fetchone()
    cur.execute(f'SELECT '
                f'  records.information, '
                f'  records.address, '
                f'  records.photo_id, '
                f'  records.video_id '
                f'FROM records '
                f'JOIN users ON users.telegram_id == records.user_id '
                f'WHERE records.user_id == {user_id};')
    records = cur.fetchall()

    data_to_send["information"], data_to_send["address"],\
    data_to_send["photo_id"], data_to_send["video_id"] = records[-1]

    return data_to_send
