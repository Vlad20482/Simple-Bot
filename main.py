import telebot
from telebot import types
import time

bot = telebot.TeleBot('6510072795:AAEIWB_l17iuVdQC2G_F84uSZRcmY4JYKcs')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('info')
    button2 = types.KeyboardButton('Odmierz czas')
    markup.row(button1, button2)
    bot.send_message(message.chat.id, f'Witaj {message.from_user.first_name}', reply_markup=markup)

@bot.message_handler()
def info(message):
    if message.text.lower() == 'info':
        bot.send_message(message.chat.id, '<b>Autor:</b> Vladyslav Svishevskyi\n\n\nDostępne komandy:\n 🔸info\n 🔸odmierzanie czas')
    if message.text.lower() == 'odmierz czas':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('1 min', callback_data='1min')
        button2 = types.InlineKeyboardButton('3 min', callback_data='3min')
        button3 = types.InlineKeyboardButton('5 min', callback_data='5min')
        markup.row(button1, button2, button3)
        button4 = types.InlineKeyboardButton('10 min', callback_data='10min')
        button5 = types.InlineKeyboardButton('30 min', callback_data='30min')
        markup.row(button4, button5)
        button6 = types.InlineKeyboardButton('1 h', callback_data='1h')
        markup.row(button6)
        bot.send_message(message.chat.id, 'Ile czasu odmierzyć?', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == '1min':
        bot.send_message(callback.message.chat.id, 'Napiszę za 1 minutę!')
        time.sleep(60)
        bot.send_message(callback.message.chat.id, 'Minęła 1 minuta!')
    if callback.data == '3min':
        bot.send_message(callback.message.chat.id, 'Napiszę za 3 minuty!')
        time.sleep(180)
        bot.send_message(callback.message.chat.id, 'Minęło 3 minuty!')
    if callback.data == '5min':
        bot.send_message(callback.message.chat.id, 'Napiszę za 5 minut!')
        time.sleep(300)
        bot.send_message(callback.message.chat.id, 'Minęło 5 minut!')
    if callback.data == '10min':
        bot.send_message(callback.message.chat.id, 'Napiszę za 10 minut!')
        time.sleep(600)
        bot.send_message(callback.message.chat.id, 'Minęło 10 minut!')
    if callback.data == '30min':
        bot.send_message(callback.message.chat.id, 'Napiszę za 30 minut!')
        time.sleep(1800)
        bot.send_message(callback.message.chat.id, 'Minęło 30 minut!')
    if callback.data == '1h':
        bot.send_message(callback.message.chat.id, 'Napiszę za 1 godzinę!')
        time.sleep(3600)
        bot.send_message(callback.message.chat.id, 'Minęła 1 godzina!')

bot.polling(none_stop=True)
