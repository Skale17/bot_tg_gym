import telebot
import time
import threading
from datetime import datetime
from telebot import types

TOKEN = "your-token"



bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'привет {message.from_user.first_name}, я Gачи бот')

def send_message_all(text):
    chats = bot.get_updates()
    for chat in chats:
        chat_id = chat.message.chat.id
        bot.send_message(chat_id, text)
        time.sleep(3)


@bot.message_handler()
def text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'привет {message.from_user.first_name}') 
    elif message.text.lower() == 'иди нахуй':
        bot.send_message(message.chat.id, f'сам иди уебок')


def survey():
    message = 'ты сегодня идешь в зал?'
    current_time = time.time()
    formatted_time = time.ctime(current_time)
    date = formatted_time.split()
    day = date[0]
    if day == 'Wed':
        bot.send_message(your_chat_id, message)

    elif day == 'Sat':
        bot.send_message(your_chat_id, message)

    elif day == 'Sun':
        bot.send_message(your_chat_id, message)
        
 

def schedule_survey():

    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == "19:01":
            threading.Thread(target=survey).start()
            time.sleep(86400)
        else:
            time.sleep(1)

schedule_survey = threading.Thread(target=schedule_survey)
schedule_survey.start()

bot.polling(non_stop=True)
time.sleep(1)






 

    


    



    
    

