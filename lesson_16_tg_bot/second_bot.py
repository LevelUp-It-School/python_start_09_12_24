import telebot
from telebot import types

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Кнопка приветствия🐯")
    markup.add(btn1)
    bot.send_message(message.from_user.id, 'Привет, я бот помощник LevelUp🤩', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "Кнопка приветствия🐯":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как проходит онлайн обучение?")
        btn2 = types.KeyboardButton("Контакты")
        btn3 = types.KeyboardButton("Расписание")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Задайте интересующий вас вопрос❓', reply_markup=markup)

    elif message.text == "Как проходит онлайн обучение?":
        bot.send_message(message.from_user.id, 'Посмотреть информацию о обучении онлайн можно по [ссылке](https://levelp.ru/courses/webinars/)', parse_mode="Markdown")
    elif message.text == "Контакты":
        bot.send_message(message.from_user.id, 'Посмотреть контактную информацию можно по [ссылке](https://levelp.ru/contacts/)', parse_mode="Markdown")
    elif message.text == "Расписание":
        bot.send_message(message.from_user.id, 'Посмотреть информацию о расписании можно по [ссылке](https://levelp.ru/courses/schedule/)', parse_mode="Markdown")

bot.infinity_polling()