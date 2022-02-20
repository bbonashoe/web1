import time
import telepot
from telepot.loop import MessageLoop       
from telepot.namedtuple import InlineKeyboardMarkup as MU, InlineKeyboardButton as BT

token = '5003695944:AAFOz4oy4Kpv9uCBy8SxNsmqBfgRddQHHd8'
mc = '699099967'
bot = telepot.Bot(token)

def btn_show(msg):
    btn1 = BT(text = "1. Hello", callback_data = "1")
    btn2 = BT(text = "2. Bye", callback_data = "2")
    btn3 = BT(text = "3. 양식", callback_data = "3")
    btn4 = BT(text = "4. 지갑", callback_data = "4")
    mu = MU(inline_keyboard = [[btn1, btn2],[btn3, btn4]])
    bot.sendMessage(mc, "선택하세요", reply_markup = mu)

def query_ans(msg):
    query_data = msg["data"]
    if query_data == "1":
        bot.sendMessage(mc, text = "안녕하세요")
    elif query_data == "2":
        bot.sendMessage(mc, text = "안녕히 계세요")
    elif query_data == "3":
        bot.sendMessage(mc, text = "하이")
    elif query_data == "4":
        bot.sendMessage(mc, text = "헬로우")

TOKEN = "5003695944:AAFOz4oy4Kpv9uCBy8SxNsmqBfgRddQHHd8"
mc = '699099967'
bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': btn_show, "callback_query" : query_ans}).run_as_thread()

print('Listening ...')

while 1: 
    time.sleep(10)