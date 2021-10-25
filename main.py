import os
import telebot
import yfinance as yf

API_KEY=os.environ['key']

bot = telebot.TeleBot(API_KEY)

def getcurrentprice(name,message):
  try:

    ticker=yf.Ticker(name)
    todays_data=ticker.history(period='1d')
    return todays_data['Close'][0]
  except:
    bot.send_message(message.chat.id,"Oops, conpany not found!")
    bot.polling()



def stock_request(message):
  request = message.text.split()
  if len(request) < 2 or request[0].lower() not in "price":
    return False
  else:
    return True



@bot.message_handler(func=stock_request)
def greet(message):
  request = message.text.split()[1]
  bot.reply_to(message, "Hey! the cost of one share is")
  bot.send_message(message.chat.id, getcurrentprice(request,message))
  

@bot.message_handler(commands=['hello'])
def hello(message):
  bot.send_message(message.chat.id, "Hello!,you can type any compamy abbreviation  and i will give it is value for one share. Please, write /help in ordwr to find how to use")

@bot.message_handler(commands=['help'])
def help(message):
  bot.send_message(message.chat.id, "Please, first write company abbreviation")

bot.polling()