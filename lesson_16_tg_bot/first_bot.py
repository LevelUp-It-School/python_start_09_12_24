import telebot

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я умею /register')

@bot.message_handler(commands=['register'])
def register(message):
    bot.send_message(message.chat.id, 'Введите, пожалуйста, свое имя')
    bot.register_next_step_handler(message, read_name)

def read_name(message):
    name = message.text
    bot.send_message(message.chat.id, 'Введите, пожалуйста, свою фамилию')
    bot.register_next_step_handler(message, read_sname, name)

def read_sname(message, name):
    sname = message.text
    bot.send_message(message.chat.id, f'Спасибо за регистрацию {name} {sname}')


bot.infinity_polling()