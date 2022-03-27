import os
import telebot
from telebot import types



class Bot:
    def __init__(self, token):
        self.__bot = telebot.TeleBot(token)

    def run(self):
        def send(id, message, markup=None):
            msg = self.__bot.send_message(id, message, reply_markup=markup)
            return msg

        def reply(messageid, message, markup=None):
            msg = self.__bot.reply_to(messageid, message, reply_markup=markup)
            return msg

        def make_keyboards():
            self.markup = types.InlineKeyboardMarkup()  # Back to main menu keyboard
            self.markup.width = 2
            self.markup.row(types.InlineKeyboardButton("Принять", callback_data="delete"),
                                 types.InlineKeyboardButton("Отклонить", callback_data="accept"))

        @self.__bot.message_handler(lambda message: True)
        def echo(message):
            bot.send(message.chat.id,
                     message.text,
                     markup=self.markup)

        @self.__bot.message_handler(commands=["stop"])
        def stop(message):
            bot.funcdoesnotexists()

        make_keyboards()
        self.__bot.polling()

if __name__ == '__main__':
    bot = Bot( token="" )
    bot.run()
