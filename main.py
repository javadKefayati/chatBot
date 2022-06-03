import os 
import telebot 

def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    print(messages)
    for m in messages:
        chatid = m.chat.id
        print("chatId=",m.chat.id)
        print("m.content_type=",m.content_type)
        if m.content_type == 'text' and m.text!="/help" and m.text !="/start":
            print("m.txt=",m.text)
            text = m.text
            print(text)
            bot.send_message(chatid, text)


TOKEN = "5331090152:AAHfzMVzZuiJQq9ChEsQ9ttc0pkkRfH9zXU"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands =["start"])
def start(message):
      bot.send_message(message.chat.id,"Hello \n welcome to ai chatbot ")

@bot.message_handler(commands =["help"])
def help(message):
      bot.reply_to(message,"this message for help you !!!")

      
# bot.polling()


bot.set_update_listener(listener) #register listener
#Use none_stop flag let polling will not stop when get new message occur error.
# Interval setup. Sleep 3 secs between request new message.
bot.polling(interval=3)

while True: # Don't let the main Thread end.
    pass