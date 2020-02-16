############################
## my first telegram bots ##
## © Mikhayil Martirosyan ##
############################
# import Libraryes 
import telebot
from telebot import types
# create varbitals
photo = open('data/tmp/MPG_logo.png', 'rb')
# connect database and select content type
bot = telebot.TeleBot("913422442:AAFJVGlf_TZL_mPNTYiipFcVi1B6IZUYoMQ")
# all code
@bot.message_handler(commands=["start"])
def start(message):
	# Keyboard with start
	KSMark  = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("💻 products")
	item2 = types.KeyboardButton("🏢 adress")
	item3 = types.KeyboardButton("😕 about")
	item4 = types.KeyboardButton("💼 can I work in your office")
	KSMark.add(item1,item2,item3,item4)
	bot.send_photo(message.chat.id, photo)
	bot.send_message(message.chat.id, " 👋 Hi Can i halp You?", reply_markup = KSMark)
@bot.message_handler(content_types=['text'])
def onlySelect(message):
	if message.text == "💼 can I work in your office":
		bot.send_message(message.chat.id, "Sorry No 😂 \n You it's noob")
	if message.text == "💻 products":
		PSMark  = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item5 = types.KeyboardButton("👍 OK")
		item6 = types.KeyboardButton("👎 No see me this is moment")
		PSMark.add(item6,item5)
		bot.send_message(message.chat.id,"I write to you later 👌",reply_markup = PSMark)
	if message.text == "🏢 adress":
		bot.send_message(message.chat.id,"This  office is located in the Gyumri Armenia, Mush 2, build 3/2 15 house")
	if message.text == "😕 about":
		bot.send_message(message.chat.id,"This office is the best of its kind for progressive \n technology, robotics, and programming 😱😉🧐😎")
	if message.text == "👍 OK":
		bot.send_message(message.chat.id, "😊😊 thanks for understanding",reply_markup = None)
	if message.text == "👎 No see me this is moment":
		bot.send_message(message.chat.id, "փախի այ հայվան բռնելեմ ոդներդ կջարդեմ 🤬😈",reply_markup = None)
#open Cicle
bot.polling( none_stop=True )