import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.keyboard import VkKeyboard, VkKeyboardColor, VkKeyboardButton
from vk_api.utils import get_random_id
import bot_config
import os
import re
import time
import numpy as np

class Program:
    def __init__(self):
        self.token = bot_config.token
        self.group_id = bot_config.group_id

        # Окно
        os.system("title BotConsole")
        
        # Авторизация
        Program.auth(self)
        # Прием команд
        while True:
            cmd = str(input("$"))
            if cmd != '':
                print(Program.commands(self,command=cmd))

    def auth(self):
        self.vk_session = vk_api.VkApi(token=self.token)
        self.longpoll = VkBotLongPoll(self.vk_session, self.group_id)
    
    def commands(self,command):
        CommandList = {"send": {"Syntax":"send.receivertype.id.message"},"start":{"Syntax": "start"},"stop":{"Syntax":"stop"},"update":{"Syntax":"update"},"cls":{"Syntax":"cls"},"sys":{"Syntax":"sys.systemcommand"},"pizdec":{"Syntax":"sys.systemcommand"}}
        cmd = command
        command = command.split('.')
        if command[0] in CommandList.keys():
            # send message
            if command[0] == "send":
                if len(command) == 4:
                    receiver = command[1]
                    id = int(command[2])
                    text = command[3]
                    try:
                        post =  {f'{receiver}_id': id,
                                'message': text,
                                'random_id': get_random_id()}
                        self.vk_session.method('messages.send', post)
                        return f"Success. {cmd}"
                    except Exception as e:
                        return f"Error while trying to send message. {e}"
                else:
                    return f"Incorrect args. Syntax: send.receivertype.id.message. Your comand: {cmd}"
            # start
            elif command[0] == "start":
                os.system("start bot.py")
                return f"Success. {cmd}"
            # stop
            elif command[0] == "stop":
                os.system('taskkill /f /fi "windowtitle eq achedzbot"')
                return f"Success. {cmd}"
            elif command[0] == "update":
                os.system("start parser.py")
                return f"Success. {cmd}"
            elif command[0] == "cls":
                os.system("cls")
                return ""
            elif command[0] == "pizdec":
                receiver = command[1]
                id = int(command[2])
                #words = ["алоааа518581285812"*50]
                while True:
                    text = "101010101010101010"*111
                    try:
                        post =  {f'{receiver}_id': id,
                                'message': "@all "+text,
                                'random_id': get_random_id()}
                        self.vk_session.method('messages.send', post)
                    except Exception as e:
                        return f"Error while trying to send message. {e}"
                    time.sleep(np.random.randint(1.0,4.0))
            elif command[0] == "sys":
                if len(command) == 2:
                    os.system(command[1])
                    return ""
                else:
                    return f"Type sys command after \".\". {cmd}.<systemcommand>"
        else:
            return "List of commands: send,start,stop,update,cls,sys"

if __name__ == '__main__':
    Program()