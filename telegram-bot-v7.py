import telebot
import sqlite3
from telebot import types
import time
import threading
import schedule

TOKEN = "6964314400:AAFsD07Nf5eTUOmYdzoCwTMb9beJfrfaQ-Q"
 
name = None
day = None
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def comand_start(message):
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS users (
                id int auto_increment primary key,
                name varchar(50),
                day varchar(50),
                mmr int
            )
        ''')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id,'Гачи хуила напиши свое прозвище')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id,'по каким дням ходишь в зал напиши через пробел дни недели на русском')
    bot.register_next_step_handler(message, user_day)

def user_day(message):
    global day
    day = str(message.text)
    id = message.from_user.id
    mmr = int(500)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO users(name, day, id, mmr) VALUES (?, ?, ?, ?)', (name, day, id, mmr))
        bot.send_message(message.chat.id,f"""Ну все ты подписался на 9 кругов ада в Gачи качалке сейчас мы зачислели тебе 500 MMR""", reply_markup=markup)
        
    except:
        bot.send_message(message.chat.id,f"""Ты уже зарегистрирован""", reply_markup=markup)
    conn.commit()
    cur.close()
    conn.close()

    

def survey():
    message = 'Ты сегодня идешь в зал?'
    trans_day = { 
                    'Mon':'понедельник',
                    'Tue':'вторник',
                    'Wed':'среда',
                    'Thu':'четверг',
                    'Fri':'пятница',
                    'Sat':'суббота',
                    'Sun':'воскресенье',
                }
    current_time = time.time()
    formatted_time = time.ctime(current_time)
    date = formatted_time.split()
    day_time = trans_day[date[0]]
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Да, иду', callback_data='yes'))
    markup.add(types.InlineKeyboardButton('Нет, не иду', callback_data='no'))
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    for el in users:
        el_str = str.lower(el[2])
        user_days = el_str.split()
        if day_time in user_days:
            bot.send_message(el[0], message, reply_markup=markup)
    
            

    cur.close()
    conn.close()


def schedule_survey():

    schedule.every().day.at("12:43").do(survey)
    while True:
        schedule.run_pending()
        time.sleep(1)
    
schedule_survey = threading.Thread(target=schedule_survey)
schedule_survey.start()

@bot.callback_query_handler(func=lambda query: query.data == 'no')
def count_no(query):
    bot.delete_message(chat_id=query.message.chat.id, message_id=query.message.message_id)
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    user_id = (query.from_user.id,)
    cur.execute('SELECT mmr FROM users WHERE id = ?', user_id)
    mmr = cur.fetchone()
    current_mmr = int(mmr[0])
    new_mmr = current_mmr - 150
    cur.execute('UPDATE users SET mmr = ? WHERE id = ?', (new_mmr, user_id[0]))
    cur.execute('SELECT id FROM users')
    all_users = cur.fetchall()
    cur.execute('SELECT name FROM users WHERE id = ?', user_id)
    name = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    for id in all_users:
        bot.send_message(id[0],f'{name[0]} НЕ МОЖЕТ пойти сегодня в зал', disable_notification=True)

@bot.callback_query_handler(func=lambda query: query.data == 'yes')
def count_yes(query):
    bot.delete_message(chat_id=query.message.chat.id, message_id=query.message.message_id)
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    user_id = (query.from_user.id,)
    cur.execute('SELECT mmr FROM users WHERE id = ?', user_id)
    mmr = cur.fetchone()
    current_mmr = int(mmr[0])
    new_mmr = current_mmr + 100
    cur.execute('UPDATE users SET mmr = ? WHERE id = ?', (new_mmr, user_id[0]))
    cur.execute('SELECT id FROM users')
    all_users = cur.fetchall()
    cur.execute('SELECT name FROM users WHERE id = ?', user_id)
    name = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    for id in all_users:
        bot.send_message(id[0],f'{name[0]} Пойдет сегодня в зал', disable_notification=True)


@bot.callback_query_handler(func=lambda call: call.data == 'users')
def callback(call):
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    
    info = ''
    for el in users:
        info += f'Имя: {el[1]}| Дни: {el[2]}| MMR: {el[3]}\n'
    cur.close()
    conn.close()
    bot.send_message(call.message.chat.id, info)
    

@bot.message_handler(commands=['base'])
def base_print(message):
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()
    result_str = "\n".join(map(str, rows))
    bot.send_message(message.chat.id, result_str)
    conn.commit()
    cur.close()
    conn.close()






bot.polling(non_stop=True)
