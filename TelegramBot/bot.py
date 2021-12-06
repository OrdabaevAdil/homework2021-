import telebot
import config
import random
from telebot import types
from mg import get_map_cell
bot = telebot.TeleBot(config.TOKEN)

#НЕ РАБОТАЕТ (Как дела?)

cols, rows = 8, 8
@bot.message_handler(commands=['labirint'])
def play_message(message):
	map_cell = get_map_cell(cols, rows)

	user_data = {
		'map': map_cell,
		'x': 0,
		'y': 0
	}

	maps[message.chat.id] = user_data

	bot.send_message(message.from_user.id, get_map_str(map_cell, (0, 0)), reply_markup=keyboard)


keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row( telebot.types.InlineKeyboardButton('←', callback_data='left'),
			  telebot.types.InlineKeyboardButton('↑', callback_data='up'),
			  telebot.types.InlineKeyboardButton('↓', callback_data='down'),
			  telebot.types.InlineKeyboardButton('→', callback_data='right') )

maps = {}

def get_map_str(map_cell, player):
	map_str = ""
	for y in range(rows * 2 - 1):
		for x in range(cols * 2 - 1):
			if map_cell[x + y * (cols * 2 - 1)]:
				map_str += "⬛"
			elif (x, y) == player:
				map_str += "🔴"
			else:
				map_str += "⬜"
		map_str += "\n"

	return map_str




@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
	user_data = maps[query.message.chat.id]
	new_x, new_y = user_data['x'], user_data['y']

	if query.data == 'left':
		new_x -= 1
	if query.data == 'right':
		new_x += 1
	if query.data == 'up':
		new_y -= 1
	if query.data == 'down':
		new_y += 1

	if new_x < 0 or new_x > 2 * cols - 2 or new_y < 0 or new_y > rows * 2 - 2:
		return None
	if user_data['map'][new_x + new_y * (cols * 2 - 1)]:
		return None

	user_data['x'], user_data['y'] = new_x, new_y

	if new_x == cols * 2 - 2 and new_y == rows * 2 - 2:
		bot.edit_message_text( chat_id=query.message.chat.id,
							   message_id=query.message.id,
							   text="Вы выиграли" )
		return None

	bot.edit_message_text( chat_id=query.message.chat.id,
						   message_id=query.message.id,
						   text=get_map_str(user_data['map'], (new_x, new_y)),
						   reply_markup=keyboard )


@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\n... {1.first_name} -бот ,выполняющий различные функции. Подробнее с функциями вы ознакомится по команде /help.".format(
                         message.from_user, bot.get_me()))

@bot.message_handler(commands=['menu'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("😊 Как дела?")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Пожалуйста {0.first_name} нажмите на одну из появившихся кнопок ниже".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "/start - вызов начальной информации о боте и его функций." \
                 "     /help - вызов поясняющей строки, содержащей основные команды(или информацию)."\
                 "     /settings — (по возможности) возвращает список возможных настроек и команды для их изменения."\
                 "     /chatcommands - возвращает список всевозможных комманд для общения с ботом(как с собеседником)."\
                 "     /games - возвращает список игр, в которые вы можете сыграть."\
				 "     /menu - возвращает кнопки, каждая из которых имеет свою функцию"


                 )


@bot.message_handler(commands=['settings'])
def send_welcome(message):
	bot.reply_to(message, "Извините, в данный момент нет способов изменения настроек, ждите обновлений! :В" )


@bot.message_handler(commands=['chatcommands'])
def send_welcome(message):
	bot.reply_to(message, "Извините,на данный момент команда не поддерживается, ждите обновлений! :В" )


@bot.message_handler(commands=['games'])
def send_welcome(message):
	bot.reply_to(message, "/labirint - игра, в которой вы должны выбраться из лабиринта(попасть из правого верхнего угла, в крайний левый нижний угол" )




@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == '😊 Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢. Напишите /start-чтобы начать диалог заново или /help-если не знаете что делать ')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                                  reply_markup=None)

            # show alert
            #bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      #text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True, interval=0)
