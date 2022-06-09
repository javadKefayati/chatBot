import os 
import telebot 
import logging
import enum
import json
import re
import sys
from db import db
from Response import Response

def logFile():
    logging.basicConfig(filename='./info.log', encoding='utf-8', level=logging.INFO)

logFile()


def listener(messages):
    
    """
    When new messages arrive TeleBot will call this function.
    This func give query from telegram bot and response them.
    """
    for m in messages:
        chatid = m.chat.id #give user id for resend message 

        if m.content_type == 'text' and m.text!="/help" and m.text !="/start" and m.text !="/items" and m.text!="/allOrder": #check format message has text and doesn't has /help or /start 
            # s =  Similarities([])
            with open("question.json", "r") as file:
                dataQ = json.load(file)
            # logging.basicConfig(filename='./info.log', encoding='utf-8', level=logging.INFO)
            
            text = m.text
            username = str(m.chat.username)
            first_name = str(m.chat.first_name)
            last_name = str(m.chat.last_name)
            t= db()
            t.addUserIfNotExist(chatid,first_name,username)
            r = Response()
            print(text)
            
            logging.info('ci='+str(chatid)+"-un ="+username+"-fn:"+first_name+"-ln:"+last_name+"-t="+text)
            response, group, nearQ, err = r.getResponse(str(text.strip()))
            print("g="+group)
            # bot.send_message(chatid, t.getTempOrder(chatid))
            
            if text=="فاکتور":
                      tempOrder= t.getTempOrder(chatid)
                      
                      if tempOrder != None:
                        bot.send_message(chatid, tempOrder)
                      else:
                                bot.send_message(chatid, "سفارشی ندارید" )
                                
            elif text =="*بله":
                      t.acceptAllOrder(chatid)
                      bot.send_message(chatid, "عملیات با موفقیت انجام شد" )
            elif text =="*خیر":
                      bot.send_message(chatid, "ادامه بدهید به سفارش" )
            else :
                if err ==1 and t.getFlag(chatid)==0:
                          bot.send_message(chatid, "توان فهم ورودی شما را ندارم\nلطفا واضح تر بیان کنید")


                #normal status
                if group != "Shop" and err == 0 and t.getFlag(chatid) == 0:
                          bot.send_message(chatid, response)

                if group == "Shop" and err == 0 and t.getFlag(chatid) == 0 :
                          t.changeFlagUser(chatid,1)
                          t.setTempItem(chatid ,nearQ)
                          bot.send_message(chatid, response)

                elif   t.getFlag(chatid) == 1:
                          isNumber = re.search("\d+", text)

                          if isNumber==None:
                                    bot.send_message(chatid, " لطفا مقدار را با واحد کیلو وارد کنید ")
                          else :
                            t.changeFlagUser(chatid,0)
                            number = isNumber   
                            tempIndex = t.getTempIndexFromUser(str(chatid))
                            t.setOrder(chatid, tempIndex, number.group(), 0)
                            
                            bot.send_message(chatid, "بسیار خب سفارشتان ثبت شد ، برای نمایش لیست خرید فاکتور را تایپ کنید")

                # print("fl="+str(t.getFlag(chatid)))
                        
                        
                      

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
      
@bot.message_handler(commands =["allOrder"])
def allOrder(message):
      d = db()
      orders = d.allOrder(message.chat.id )
      if orders !=None:
        bot.reply_to(message, orders)
      else :
                bot.reply_to(message, "سفارشی ندارید")



bot.set_update_listener(listener) #register listener
#Use none_stop flag let polling will not stop when get new message occur error.
# Interval setup. Sleep 3 secs between request new message.
bot.polling(interval=3)

while True: # Don't let the main Thread end.
    pass