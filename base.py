import sqlite3
def connect():
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    return conn, cur 
def close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()
def create_table():
    conn, cur = connect()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name varchar(50),
                day str varchar(100),
                mmr int,
                role str varchar(50)
            )
        ''')
    close(conn, cur)
def insert_user_info(name, id, day, mmr, role):
    conn, cur = connect()
    try:
        cur.execute('INSERT INTO users(name, id, day, mmr, role) VALUES (?, ?, ?, ?, ?)', (name, id, day, mmr, role))
        close(conn, cur)
        result = True
        return result
    except:
        close(conn, cur)
        result = False
        return result

def update_day(day, user_id):
    conn, cur = connect()
    cur.execute('UPDATE users SET day = ? WHERE id = ?', (day, user_id))
    close(conn, cur)

def select_days_from_base(user_id):
    conn, cur = connect()
    cur.execute('SELECT day FROM users WHERE id = ?', (user_id,))
    result = str(cur.fetchone())
    close(conn, cur)
    return result
def update_user_name(name, id):
    conn, cur = connect()
    cur.execute('UPDATE users SET name = ? WHERE id = ?', (name, id))
    close(conn, cur)
def select_users():
    conn, cur = connect()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    close(conn, cur)
    return users
def select_mmr(user_id):
    conn, cur = connect()
    cur.execute('SELECT mmr FROM users WHERE id = ?', user_id)
    mmr = cur.fetchone()
    close(conn, cur)
    return mmr
def update_mmr(mmr, user_id):
    conn, cur = connect()
    cur.execute('UPDATE users SET mmr = ? WHERE id = ?', (mmr, user_id[0]))
    conn.commit()
    close(conn, cur)
def all_id():
    conn, cur = connect()
    cur.execute('SELECT id FROM users')
    all_users = cur.fetchall()
    close(conn, cur)
    return all_users
def select_user_name(user_id):
    conn, cur = connect()
    cur.execute('SELECT name FROM users WHERE id = ?', user_id)
    name = cur.fetchone()
    close(conn, cur)
    return name
def select_all_mmr():
    conn, cur = connect()
    cur.execute('SELECT mmr FROM users')
    mmr = cur.fetchone()
    close(conn, cur)
    return mmr
def select__name_where_mmr(mmr):
    mmr_i = int(mmr)
    conn, cur = connect()
    cur.execute('SELECT name FROM users WHERE mmr = ?', (mmr_i,))
    name = cur.fetchone()
    close(conn, cur)
    return name
def select_role(user_id):
    conn, cur = connect()
    cur.execute('SELECT role FROM users WHERE id = ?', (user_id,))
    role = cur.fetchone()
    close(conn, cur)
    return role[0]
def add_role(user_id):
    role = 'admin'
    conn, cur = connect()
    cur.execute('UPDATE users set role = ? WHERE id = ?',(role, user_id))
    close(conn, cur)
