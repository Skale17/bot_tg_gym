import telebot
import sqlite3
from telebot import types
import time
import threading
import schedule

TOKEN = "Your token"
 
name = None
bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def comand_start(message):
    conn = sqlite3.connect('main_base.sql')
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

    bot.send_message(message.chat.id,'Гачи хуила напиши свое прозвище')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    name = message.text.strip()
    id = message.from_user.id
    mmr = int(500)
    day = ''
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    markup.add(types.InlineKeyboardButton('Выбрать дни посещения ', callback_data='day'))
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO users(name, id,day, mmr) VALUES (?, ?, ?,?)', (name, id, day, mmr))
        bot.send_message(message.chat.id,f"""Ну все ты подписался на 9 кругов ада в Gачи качалке сейчас мы зачислели тебе 500 MMR и дальше ты должен выбрать дни по которым ходишь в зал если что-то не понятно у нас есть команда /menu""", reply_markup=markup)
    except:
        bot.send_message(message.chat.id,f"""Ты уже зарегистрирован""", reply_markup=markup)
    conn.commit()
    cur.close()
    conn.close()
@bot.callback_query_handler(func=lambda query: query.data == 'day')
def user_day(query):
    bot.delete_message(chat_id=query.message.chat.id, message_id=query.message.message_id)
    user_id = (query.from_user.id,)
    day = ''
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('UPDATE users SET day = ? WHERE id = ?', (day, user_id[0]))
    conn.commit()
    cur.close()
    conn.close()
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Понедельник', callback_data='mon'))
    markup.add(types.InlineKeyboardButton('Вторник', callback_data='tue'))
    markup.add(types.InlineKeyboardButton('Среда', callback_data='wed'))
    markup.add(types.InlineKeyboardButton('Четверг', callback_data='thu'))
    markup.add(types.InlineKeyboardButton('Пятница', callback_data='fri'))
    markup.add(types.InlineKeyboardButton('Суббота', callback_data='sat'))
    markup.add(types.InlineKeyboardButton('Воскресенье', callback_data='sun'))
    markup.add(types.InlineKeyboardButton('Сохранить', callback_data='save'))
    
    bot.send_message(user_id[0],"Выбери дни по которым ходишь в зал", reply_markup=markup)

@bot.callback_query_handler(func=lambda query: query.data == 'mon')
def Mon(query):
    user_id = query.from_user.id
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('SELECT day FROM users WHERE id = ?', (user_id,))
    day = str(cur.fetchone())
    filter_day = filter_str(day)
    new_day = filter_day + ' понедельник'
    cur.execute('UPDATE users SET day = ? WHERE id = ?', (new_day, user_id))
    conn.commit()
    cur.close()
    conn.close()
@bot.callback_query_handler(func=lambda query: query.data == 'tue')
def Tue(query):
    user_id = query.from_user.id
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('SELECT day FROM users WHERE id = ?', (user_id,))
    day = str(cur.fetchone())
    filter_day = filter_str(day)
    new_day = filter_day + ' вторник'
    cur.execute('UPDATE users SET day = ? WHERE id = ?', (new_day, user_id))
    conn.commit()
    cur.close()
    conn.close()
@bot.callback_query_handler(func=lambda query: query.data == 'wed')
def Wed(query):
    user_id = query.from_user.id
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('SELECT day FROM users WHERE id = ?', (user_id,))
    day = str(cur.fetchone())
    filter_day = filter_str(day)
    new_day = filter_day + ' среда'
    cur.execute('UPDATE users SET day = ? WHERE id = ?', (new_day, user_id))
    conn.commit()
    cur.close()
    conn.close()
@bot.callback_query_handler(func=lambda query: query.data == 'thu')
def Thu(query):
    user_id = query.from_user.id
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('SELECT day FROM users WHERE id = ?', (user_id,))
    day = str(cur.fetchone())
    filter_day = filter_str(day)
    new_day = filter_day + ' четверг'
    cur.execute('UPDATE users SET day = ? WHERE id = ?', (new_day, user_id))
    conn.commit()
    cur.close()
    conn.close()

@bot.callback_query_handler(func=lambda query: query.data == 'fri')
def Fri(query):
    user_id = query.from_user.id
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('SELECT day FROM users WHERE id = ?', (user_id,))
    day = str(cur.fetchone())
    filter_day = filter_str(day)
    new_day = filter_day + ' пятница'
    cur.execute('UPDATE users SET day = ? WHERE id = ?', (new_day, user_id))
    conn.commit()
    cur.close()
    conn.close()
@bot.callback_query_handler(func=lambda query: query.data == 'sat')
def Sat(query):
    user_id = query.from_user.id
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('SELECT day FROM users WHERE id = ?', (user_id,))
    day = str(cur.fetchone())
    filter_day = filter_str(day)
    new_day = filter_day + ' суббота'
    cur.execute('UPDATE users SET day = ? WHERE id = ?', (new_day, user_id))
    conn.commit()
    cur.close()
    conn.close()
@bot.callback_query_handler(func=lambda query: query.data == 'sun')
def Sun(query):
    user_id = query.from_user.id
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('SELECT day FROM users WHERE id = ?', (user_id,))
    day = str(cur.fetchone())
    filter_day = filter_str(day)
    new_day = filter_day + ' воскресенье'
    cur.execute('UPDATE users SET day = ? WHERE id = ?', (new_day, user_id))
    conn.commit()
    cur.close()
    conn.close()

@bot.callback_query_handler(func=lambda query: query.data == 'save')
def Save(query):
    user_id = query.from_user.id
    bot.delete_message(chat_id=query.message.chat.id, message_id=query.message.message_id)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Да', callback_data='yes_save'))
    markup.add(types.InlineKeyboardButton('Нет', callback_data='day'))
    conn = sqlite3.connect('main_base.sql')
    cur = conn.cursor()
    cur.execute('SELECT day FROM users')
    day = str(cur.fetchone())
    conn.commit()
    cur.close()
    conn.close()
    filter_day = filter_str(day)
    bot.send_message(user_id,f"Дни выбраны верно?\n {filter_day}", reply_markup=markup)
    
@bot.callback_query_handler(func=lambda query: query.data == 'yes_save')
def Save_yes(query):
    bot.delete_message(chat_id=query.message.chat.id, message_id=query.message.message_id)
    bot.register_next_step_handler(query.message, comand_menu)

    

def filter_str(text):
    return ''.join(symbol for symbol in text if symbol.isspace() or symbol.isalpha())
    


    
    

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

    schedule.every().day.at("17:20").do(survey)
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

@bot.message_handler(commands=['menu'])
def comand_menu(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    markup.add(types.InlineKeyboardButton('Сменить дни посищения ', callback_data='day'))
    markup.add(types.InlineKeyboardButton('Сменить Имя', callback_data='name'))
    bot.send_message(message.chat.id, "Меню", reply_markup=markup)
    








bot.polling(non_stop=True)
