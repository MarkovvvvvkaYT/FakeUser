#███████╗░█████╗░██╗░░██╗███████╗██╗░░░██╗░██████╗███████╗██████╗░
#██╔════╝██╔══██╗██║░██╔╝██╔════╝██║░░░██║██╔════╝██╔════╝██╔══██╗
#█████╗░░███████║█████═╝░█████╗░░██║░░░██║╚█████╗░█████╗░░██████╔╝
#██╔══╝░░██╔══██║██╔═██╗░██╔══╝░░██║░░░██║░╚═══██╗██╔══╝░░██╔══██╗
#██║░░░░░██║░░██║██║░╚██╗███████╗╚██████╔╝██████╔╝███████╗██║░░██║
#╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝

#GitHub - https://github.com/MarkovvvvvkaYT/FakeUser
#Telegram bot - @FakeUserAPI_bot (It's working)
#Hosting - https://www.pythonanywhere.com
#API - https://api-ninjas.com/api/randomuser

import requests as r
import telebot

#_______________________________________________________________________________________
TOKEN = ''
api_url = 'https://api.api-ninjas.com/v1/randomuser'
api = ''
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = telebot.types.KeyboardButton('Создать фейк личность👽')
    keyboard.add(button_1)
    bot.send_message(message.chat.id, 'Created by MarkovvvvvkaYT🥕', reply_markup=keyboard)
    bot.send_message(message.chat.id, 'Выберете действие снизу⬇️', reply_markup=keyboard)

@bot.message_handler(func=lambda m: m.text.strip().capitalize() == 'Создать фейк личность👽')
def command(message: telebot.types.Message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton('Юзернейм', callback_data="username")
    button_2 = telebot.types.InlineKeyboardButton('Адрес', callback_data="address")
    button_3 = telebot.types.InlineKeyboardButton('Имя, фамилия', callback_data="name")
    button_4 = telebot.types.InlineKeyboardButton('Электронная почта', callback_data="email")
    button_5 = telebot.types.InlineKeyboardButton('Дата рождения', callback_data="birthday")
    button_6 = telebot.types.InlineKeyboardButton('Фейк личность', callback_data="fakeuser")
    keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6)
    bot.send_message(message.chat.id, 'Выберете что вы хотите сгенерировать', reply_markup=keyboard)



@bot.callback_query_handler(func=lambda callback: callback.data.strip() in ['username', 'address', "name", "email", "birthday"])
def handle_callback(callback):
    bot.send_message(callback.message.chat.id, f'Генерирую...')
    response = r.get(api_url, headers={'X-Api-Key': api})
    if response.status_code == r.codes.ok:
        print(callback.data.strip().capitalize())
        bot.send_message(callback.message.chat.id, f"{response.json().get(callback.data.strip())}")
    else:
        bot.send_message(callback.message.chat.id, f'{response.status_code}, {response.text}')


@bot.callback_query_handler(func=lambda callback: callback.data.strip().capitalize() == 'Fakeuser')
def handle_callback(callback):
    bot.send_message(callback.message.chat.id, f'Генерирую...')
    response = r.get(api_url, headers={'X-Api-Key': api})
    print(response)
    if response.status_code == r.codes.ok:
        print(f"Юзернейм: {response.json().get('username')}\nАдрес: {response.json().get('address')}\nИмя, фамилия: {response.json().get('name')}\nЭлектронная почта: {response.json().get('email')}\nДата рождения: {response.json().get('birthday')}")
        bot.send_message(callback.message.chat.id, f"Юзернейм: {response.json().get('username')}\nАдрес: {response.json().get('address')}\nИмя, фамилия: {response.json().get('name')}\nЭлектронная почта: {response.json().get('email')}\nДата рождения: {response.json().get('birthday')}")
    else:
        bot.send_message(callback.message.chat.id, f'{response.status_code}, {response.text}')




print("Сервер запущен!")        
bot.polling(
    non_stop=True,
    interval=1 
)
