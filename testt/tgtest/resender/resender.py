import telebot
from datetime import datetime
import resender_cfg

API_TOKEN = resender_cfg.API_TOKEN
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def replier(message):
    if message.chat.id != resend_chat:  # don`t resend messages from chat for resending...
        # make stuff
        firstname = message.from_user.first_name
        lastname = message.from_user.last_name or "N/D"
        text = message.text
        time = datetime.utcfromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S')
        try:
            reply_who = message.reply_to_message.from_user.first_name
            reply_text = message.reply_to_message.text
        except AttributeError:
            reply_who = "N/D"
            reply_text = "N/D"
        id = message.from_user.id

        # send stuff
        bot.send_message(resend_chat, f'''chat: name={message.chat.title}; id={message.chat.id};
        user: Name= {firstname}; Lastname= {lastname}; id= {id};
        message= {text};
        time= {time} GMT +0;
        reply: to= {reply_who}; text= {reply_text};''')

if __name__ == "__main__":
    resend_chat = resender_cfg.resend_chat
    bot.polling()