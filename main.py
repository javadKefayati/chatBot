import os 
import telebot 
import logging
import enum
import json

from Response import Response

def logFile():
    logging.basicConfig(filename='./info.log', encoding='utf-8', level=logging.INFO)

logFile()


def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    This func give query from telegram bot and response them.
    """
    
    print(messages)
    for m in messages:
        chatid = m.chat.id #give user id for resend message 
        print("chatId=",m.chat.id)
        print("m.content_type=",m.content_type) 
        if m.content_type == 'text' and m.text!="/help" and m.text !="/start" and m.text !="/items": #check format message has text and doesn't has /help or /start 
            # s =  Similarities([])
            with open("question.json", "r") as file:
                dataQ = json.load(file)
            # logging.basicConfig(filename='./info.log', encoding='utf-8', level=logging.INFO)
            
            text = m.text
        
            r = Response()
            print(text)
            logging.info('chat Id='+str(chatid)+"---text="+text)
            response , err = r.getResponse(str(text.strip()))
            if err ==0:
                      bot.send_message(chatid, "توان فهم ورودی شما را ندارم\nلطفا واضح تر بیان کنید")
            else :
                      bot.send_message(chatid, response)

#api key for connect to telegram bot
TOKEN = "5331090152:AAHfzMVzZuiJQq9ChEsQ9ttc0pkkRfH9zXU"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands =["start"])
def start(message):
      bot.send_message(message.chat.id,"Hello \n welcome to ai chatbot ")

@bot.message_handler(commands =["help"])
def help(message):
      bot.reply_to(message,"this message for help you !!!")
      
@bot.message_handler(commands =["items"])
def items(message):
      bot.reply_to(message,"سیب - انار -گلابی- بستنی- شیر - موز")

      
# bot.polling()


bot.set_update_listener(listener) #register listener
#Use none_stop flag let polling will not stop when get new message occur error.
# Interval setup. Sleep 3 secs between request new message.
bot.polling(interval=3)

while True: # Don't let the main Thread end.
    pass