import telebot
import random
from gtts import gTTS
from telebot import types
from khayyam import JalaliDatetime
import qrcode


bot=telebot.TeleBot("5984769670:AAEG1GQLcldldaE09r0FciIl557iElj0rbY",parse_mode=None)



@bot.message_handler(commands=["start"])
def send_welcome(message):
    name=input("اسمت چیه؟")
    bot.reply_to(message, "سلام % خوش امدی.هر راهنمایی خواستی فقط HELP رو بزن" , name)





computer_number = random.randint(1,20)
@bot.message_handler(commands=["game" , "new_game"])
def start_game(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    guess = bot.reply_to(message , "یه عدد بین 1 و 20 انتخاب کن" )
    bot.register_next_step_handler[ telebot.types.Message]


@bot.message_handler(commands=["HELP"])
def menu_help(massage):
    bot.send_message(massage,"""
    /game: \n بیا بازی حدس عدد انجام بدیم\n
    /age: \nتاریخ تولدتو به شمسی بگو تا سنتو بگم \n
    /voice: \nیه جمله به انگلیسی بگو تا تلفظشو برات بفرستم\n
    /max: \n یه سری عدد بگو تا بزرگترینشو بگم بهت \n
    /argmax \nیه سری عدد بگو تا بگم بزرگترین عددش چندمیه \n
    /qrcode \n یه چیزی بگو تا برات QRcode اش رو بسازم \n
    """)    

@bot.message_handler(commands=["QRcode"])
def qrcode1(message):
    message = bot.send_message(message ,"یه چیزی بگو تا برات تبدیلش کنم به QRcode:  ")
    bot.register_next_step_handler(message,qrcode)

def qr_code(message):
    msg = message.text
    img = qrcode.make(msg)
    img.save("your_qrcode.png")
    f = open("your_qrcode.png",'rb')
    bot.send_photo(message ,f)


@bot.message_handler(commands=['age'])
def age1(message):
    message = bot.send_message(message.chat.id,"تاریخ تولد خود را وارد نمایید: مثال: 17/11/1364")
    bot.register_next_step_handler(message,age)

def age(message):
    birthday = message.text
    print(birthday)
    birth_lst = birthday.split("/")
    age=JalaliDatetime.now()-JalaliDatetime(birth_lst[0],birth_lst[1],birth_lst[2])//365
    bot.send_message(message.chat.id,"Your age: ", age)
    
@bot.message_handler(commands=['voice'])
def voice1(message):
    message = bot.send_message(message.chat.id,"یک جمله به زبان انگلیسی وارد نمایید: ")
    bot.register_next_step_handler(message,voice)

def voice(message):
    txt = message.text
    print(txt)
    s=gtts.gTTS(txt, lang="en",slow=False)
    s.save("pro.mp3")
    voice = open("pro.mp3",'rb')
    bot.send_voice(message.chat.id,voice)
