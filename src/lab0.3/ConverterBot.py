import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('7228308700:AAFSmWU9qks1pr1IMteGEra_R0Gu_98pa3E')
currency = CurrencyConverter()

amount = 0


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, введите сумму')
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат! Введите сумму')
        bot.register_next_step_handler(message, summa)
        return

    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add((types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')),
                   (types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')),
                   (types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')),
                   (types.InlineKeyboardButton('USD/JPY', callback_data='usd/jpy')),
                   (types.InlineKeyboardButton('Другое значение', callback_data='else'))
                   )
        bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Число должно быть больше 0! Введите сумму')
        bot.register_next_step_handler(message, summa)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values_of_currency = call.data.upper().split('/')
        res = currency.convert(amount, values_of_currency[0], values_of_currency[1])
        bot.send_message(call.message.chat.id, f'Получается: {round(res, 2)}. Можете заново ввести сумму')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'Введите пару значений через слэш ("/")')
        bot.register_next_step_handler(call.message, my_currency)


def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'Получается: {round(res, 2)}. Можете заново ввести сумму')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'Что-то не так. Введите значение заново')
        bot.register_next_step_handler(message, my_currency)


bot.polling(none_stop=True)
