import sqlite3

conn = sqlite3.connect('db/usersinfo.sqlite3', check_same_thread=False)
cursor = conn.cursor()


async def db_table_val(user_id: int, user_balance: int):
    cursor.execute('INSERT OR IGNORE INTO balance (user_id, user_balance) VALUES (?, ?)', (user_id, user_balance))
    conn.commit()


async def update_balance(us_id: int, cash: int):
    current_balance = await get_user_balance(us_id)
    cursor.execute(f'UPDATE balance SET user_balance = {str(int(current_balance)+(cash))} WHERE user_id = {str(us_id)}')
    conn.commit()


async def get_user_balance(us_id: int):
    cursor.execute(f'SELECT user_balance FROM balance WHERE user_id = "{str(us_id)}"')
    data = cursor.fetchone()
    return data[0]


async def get_user_admin(us_id: int):
    cursor.execute(f'SELECT admin FROM balance WHERE user_id = "{str(us_id)}"')
    data = cursor.fetchone()
    return data[0]


async def add_admin(us_id: int):
    cursor.execute(f'UPDATE balance SET admin = 1 WHERE user_id = {str(us_id)}')
    conn.commit()