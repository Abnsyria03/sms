 
import os
try:
	import requests
	import base64
	import marshal
	import zlib
	import telebot
except:
    os.system("pip install pyTelegramBotAPI")
    os.system("pip install requests")
    os.system("pip install base64")
    os.system("pip install marshal")
    os.system("pip install zlib")


Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
W="\033[1;37m" # White


insta="1234567890qwertyuiopasdfghjklzxcvbnm"
all="_._._._._."
#------------------------[@llxxx3]---------------------------#


import telebot
from telebot import *
from telebot import util
from telebot import types

token = '5569133041:AAHNfPp6rNw7hU-UR1Hj_jSpTcylEZdImPk'
#هنا خلي توكنك

bot = telebot.TeleBot(token)

def encode_files(name, file_name):
    if name == "marshal":
        en = marshal.dumps(compile(open(file_name, "r").read(), '<mostafa>', 'exec'))
        return (f"\nimport marshal\nexec(marshal.loads({en}))")
    elif name == "base64":
        en = base64.b64encode(open(file_name, "r").read().encode('UTF-8')).decode('ascii')
        return (f"\nimport base64\nexec(base64.b64decode('{en}'))")
    elif name == "lambda":
        en = repr(zlib.compress(open(file_name, "r").read().encode('utf-8')))
        return (f"#\nexec((lambda _____, ______ : ______(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(_____),'<','exec'))({en},compile))")
    elif name == "zlib":
        en = str(base64.b64encode(zlib.compress(marshal.dumps(compile(open(file_name, "r").read(), "ru", 'exec')))))
        return (f"#import zlib\nexec(marshal.loads(zlib.decompress(base64.b64decode('{en}'))))")

@bot.message_handler(commands=['start'])
def welcome(message):
    channel = types.InlineKeyboardButton(text=" قناتي ", url=f"https://t.me/llxxx3")
    start = types.InlineKeyboardButton(text=" اضغط هنا لتشفير", callback_data="Encryption")
    programmer = types.InlineKeyboardButton(text=" المطور ", url=f"https://t.me/PY_87")
    Keyboards = types.InlineKeyboardMarkup()
    Keyboards.row_width = 1
    Keyboards.add(start, programmer, channel)
    bot.send_message(message.chat.id, text=f"🖤| مرحبا {message.from_user.first_name}\n✅ بوت تشفير ادوات بايثون\n🔰| المطور⚜️ @llxxx3 ⚜️",
reply_to_message_id=(message.message_id), reply_markup=Keyboards)
def Encryption(message):
    Button1 = types.InlineKeyboardButton(text="base64 🔒", callback_data='base64')
    Button2 = types.InlineKeyboardButton(text="lambda 🔒", callback_data='lambda')
    Button3 = types.InlineKeyboardButton(text="marshal 🔒", callback_data='marshal')
    Button4 = types.InlineKeyboardButton(text="zlib 🔒", callback_data='zlib')
    Keyy = types.InlineKeyboardMarkup()
    Keyy.row_width = 1
    Keyy.add(Button1, Button2, Button3, Button4)
    bot.send_message(message.chat.id, text=f"🔰| اختار نوع التشفير ", parse_mode="markdown", reply_markup=Keyy)

def file_encode(message, name):
    bot.send_message(message.chat.id, text=f"📥| قم بارسال الملف لتشفيره  {name} ")
    @bot.message_handler(content_types=['document'])
    def save(message):
        file_input = bot.download_file(bot.get_file(message.document.file_id).file_path)
        file_name = f"@llxxx3.py"
        with open(file_name, 'wb') as f:
            f.write(file_input)
        en = encode_files(name, file_name)
        with open(file_name, 'w') as f:
            f.write(en)
        file_document = open(file_name, 'rb')
        bot.send_document(message.chat.id, file_document)
        os.system(f"rm -f {file_name}")

@bot.callback_query_handler(func=lambda call: True)
def callbacks_data(call):
    if call.data == "Encryption":
        Encryption(call.message)
    elif call.data == "base64":
        file_encode(call.message, "base64")
    elif call.data == "lambda":
        file_encode(call.message, "lambda")
    elif call.data == "marshal":
        file_encode(call.message, "marshal")
    elif call.data == "zlib":
        file_encode(call.message, "zlib")
while True:
    try:
        print("\033[1;32m تـم التشغـيل بنـجاح")
        bot.polling(True)
        break
    except Exception as ex:
        print(f"Error polling : {ex}")
        telebot.logger.error(ex)
        continue
