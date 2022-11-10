import telebot
import random
from telebot import types


bot = telebot.TeleBot('5616498215:AAGTg8KhqBHIKVrrM35NysjBdl6SgQ_O6pM')

@bot.message_handler(commands=['start'])
def game_start(message):
    # Build keyboard
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Камень🤜')
    btn2 = types.KeyboardButton('Ножницы✌️')
    btn3 = types.KeyboardButton('Бумага✋')
    keyboard.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'Камень🤜, ножницы✌️, бумага✋, раз, два, три! Выберите жест:',
                          reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def game(message):
    choice = random.choice(['Камень🤜', 'Ножницы✌️', 'Бумага✋'])
    if message.text == choice:
        bot.send_message(message.chat.id, 'Боевая ничья! Для начала новой игры пишите /start')
    else:
        if message.text == 'Камень🤜':
            if choice == 'Ножницы✌️':
                bot.send_message(message.chat.id,
                                 'Поздравляю с победой! У меня была {}. Для начала новой игры пишите /start'.format(
                                     choice))
            else:
                bot.send_message(message.chat.id,
                                 'Извените, но Вы проиграли 😢. У меня был(и/a) {}. Для начала новой игры пишите /start'.format(
                                     choice))
        elif message.text == 'Ножницы✌️':
            if choice == 'Бумага✋':
                bot.send_message(message.chat.id,
                                 'Поздравляю с победой! У меня была {}. Для начала новой игры пишите /start'.format(
                                     choice))
            else:
                bot.send_message(message.chat.id,
                                 'Извените, но Вы проиграли 😢. У меня был(и/a) {}. Для начала новой игры пишите /start'.format(
                                     choice))
        elif message.text == 'Бумага✋':
            if choice == 'Камень🤜':
                bot.send_message(message.chat.id,
                                 'Поздравляю с победой! У меня была {}. Для начала новой игры пишите /start'.format(
                                     choice))
            else:
                bot.send_message(message.chat.id,
                                 'Извените, но Вы проиграли 😢. У меня был(и/a) {}. Для начала новой игры пишите /start'.format(
                                     choice))


bot.polling(none_stop=True)
