import sqlite3

def create_table(name):
    conn = sqlite3.connect(f'{name}.sql')
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name varchar(50),
                day str varchar(100),
                mmr int
            )
        ''')
    conn.commit()
    cur.close()
    conn.close()
def insert_user_info(name, id, day, mmr):
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO users(name, id,day, mmr) VALUES (?, ?, ?,?)', (name, id, day, mmr))
        conn.commit()
        cur.close()
        conn.close()
        result = True
        return result
    except:
        conn.commit()
        cur.close()
        conn.close()
        result = False
        return result

def update_day(day, user_id):
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('UPDATE users SET day = ? WHERE id = ?', (day, user_id))
    conn.commit()
    cur.close()
    conn.close()

def select_days_from_base(user_id):
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('SELECT day FROM users WHERE id = ?', (user_id,))
    result = str(cur.fetchone())
    conn.commit()
    cur.close()
    conn.close()
    return result
def update_user_name(name, id):
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('UPDATE users SET name = ? WHERE id = ?', (name, id))
    conn.commit()
    cur.close()
    conn.close()
def select_users():
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users
def select_mmr(user_id):
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('SELECT mmr FROM users WHERE id = ?', user_id)
    mmr = cur.fetchone()
    cur.close()
    conn.close()
    return mmr
def update_mmr(mmr, user_id):
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('UPDATE users SET mmr = ? WHERE id = ?', (mmr, user_id[0]))
    conn.commit()
    cur.close()
    conn.close()
def all_id():
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('SELECT id FROM users')
    all_users = cur.fetchall()
    cur.close()
    conn.close()
    return all_users
def select_user_name(user_id):
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('SELECT name FROM users WHERE id = ?', user_id)
    name = cur.fetchone()
    cur.close()
    conn.close()
    return name
def select_all_mmr():
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('SELECT mmr FROM users')
    mmr = cur.fetchone()
    cur.close()
    conn.close()
    return mmr
def select__name_where_mmr(mmr):
    mmr_i = int(mmr)
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('SELECT name FROM users WHERE mmr = ?', (mmr_i,))

    name = cur.fetchone()
    cur.close()
    conn.close()
    return name
