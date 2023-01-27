import telebot
from extensions import *
from config import *
import traceback

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = "Привет! я конвертер валют. чтобы сконвертировать валюту нужно ввести:\n " \
           "имя валюты, цену которой ты хочешь узнать\n" \
           "имя валюты, в которой надо узнать цену первой валюты\n" \
           "количество первой валюты"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in keys.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise APIException('не верное колличество параметров: нужно три!!!!')

        ansver = Converter.get_price(*values)
    except APIException as e:
        bot.reply_to(message, f"Ошибка в команде \n {e}")
    else:
        bot.reply_to(message, ansver)


bot.polling()