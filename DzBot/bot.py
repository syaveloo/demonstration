import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.keyboard import VkKeyboard, VkKeyboardColor, VkKeyboardButton
from vk_api.utils import get_random_id
import bot_config
import os
import re
import time

class Homework:
    def __init__(self):
        def ReadHomework():
            with open('homework.json','r',encoding='utf-8') as file:
                return eval(file.read())
        
        # read homework
        self.homework = ReadHomework()
    def GetFilter(text,noperms):
        # noperms: 1 => text format @achedz ачедз <text>; we need to drop @achedz
        message = text.split(" ")
        days = {"пн": "Понедельник","вт": "Вторник","ср": "Среда","чт": "Четверг","пт": "Пятница"}
        filt = []
        for day in message:
            if day in days.keys():
                filt.append(days[day])
        return filt
    def GetWeek(text):
        weeks = {"н-2":"2","н-1":"1","н0":"0","н1":"-1","н2":"-2"}
        message = text.split(" ")
        for week in message:
            if week in weeks.keys():
                return weeks[week]
        return "0"
        
    def Get(self, text, noperms):
        week = Homework.GetWeek(text)
        week_message = {"-2": "2 недели вперед","-1": "1 неделя вперед","0": "Текущая неделя","1": "1 неделя назад","2": "2 недели назад"}[week]
        filt = Homework.GetFilter(text,noperms)
        homework = self.homework['Homework'][week]
        message = f"{self.homework['UpdateTime']}\n{week_message}\n"
        for day in homework.keys():
            if re.sub('[ ,1234567890.]',"",day) in filt or not filt: # day pass filter or filter is none
                message += f"{day}:\n"
                for lesson_num in homework[day].keys():
                    if homework[day][lesson_num]['homework'] != 'Нет задания':
                        message += f"    - {homework[day][lesson_num]['name']}: {homework[day][lesson_num]['homework']}\n"
                message += '\n'
        return message

class Program:
    last_update_time = time.time()
    last_message_time = time.time()
    
    def __init__(self):
        self.token = bot_config.token
        self.group_id = bot_config.group_id

        # Название окна
        os.system("title achedzbot")
        
        # Статус заморозки
        Program.freeze = False

        # Стоп-код
        Program.freezecode = get_random_id()
        print("Freezecode:",Program.freezecode)
        # Килл-код
        Program.killcode = get_random_id()
        print("Killcode:",Program.killcode)
        
        # Авторизация
        Program.auth(self)
        # Создание клавиатур
        Program.create_keyboards(self)
        # Слушаем
        Program.listener(self)
    
    def auth(self):
        self.vk_session = vk_api.VkApi(token=self.token)
        self.longpoll = VkBotLongPoll(self.vk_session, self.group_id)
    
    def send(self, id, text, keyboard=None, receiver='user'): 
        post =  {f'{receiver}_id': id,
                'message': text,
                'random_id': get_random_id()}
        if keyboard != None:
            post['keyboard'] = keyboard.get_keyboard()
        self.vk_session.method('messages.send', post)
    
    def create_keyboards(self):
        # default keyboard
        self.keyboard_default = VkKeyboard(one_time=False)
        self.keyboard_default.add_button("ачедз", color=VkKeyboardColor.NEGATIVE)
        self.keyboard_default.add_button("обнови", color=VkKeyboardColor.SECONDARY)
        
        # default chat keyboard
        self.keyboard_default_chat = VkKeyboard(one_time=False)
        self.keyboard_default_chat.add_button("виталя вы знаете меня? нет? ну ладно", color=VkKeyboardColor.NEGATIVE)
        self.keyboard_default_chat.add_button("витаалий", color=VkKeyboardColor.SECONDARY)
        

        # is_bot_alive keyboard
        self.keyboard_isalive = VkKeyboard(one_time=False)
        self.keyboard_isalive.add_button("Ping", color=VkKeyboardColor.SECONDARY)
    
    def listener(self): 
        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                text = event.object.message['text'].lower()
                
                # Выход по килл-коду
                if str(Program.killcode) in text:
                    exit()
                elif str(Program.freezecode) in text:
                    Program.freeze = not Program.freeze
                # Беседа
                if event.from_chat and '@all' not in text and not Program.freeze:
                    id = event.chat_id
                    print(text, "in chat:", id)
                    Program.send(self,id=id,text="a",keyboard=self.keyboard_default_chat,receiver='chat')
                    exit()
                    if time.time()-Program.last_message_time > 5.0:
                        Program.last_message_time = time.time()
                        # дз
                        if "обнови" in text:
                            if time.time()-Program.last_update_time > 300.0:
                                print(time.time()-Program.last_update_time)
                                Program.last_update_time = time.time()
                                os.system(f"start {os.getcwd()}\\parser.py")
                                Program.send(self, id=id, text="Обновляю...", keyboard=None, receiver='chat')
                            else:
                                Program.send(self, id=id, text=f"на абнову ищо {300-(time.time()-Program.last_update_time)}", keyboard=None, receiver='chat')
                        else:
                            Program.send(self, id=id, text=Homework().Get(text,noperms=1), keyboard=self.keyboard_default_chat, receiver='chat')
                    else:
                        Program.send(self, id=id, text=f"на месэдж ищо {5-(time.time()-Program.last_message_time)}", keyboard=None, receiver='chat')
                # ЛС
                elif event.from_user and not Program.freeze:
                    id = event.object.message['from_id']
                    print(text, 'from user:', id)
                    # дз
                    if time.time()-Program.last_message_time > 5.0:
                        Program.last_message_time = time.time()
                        if "ачедз" in text:
                            Program.send(self, id=id, text=Homework().Get(text,noperms=0), keyboard=self.keyboard_default, receiver='user')
                        elif "обнови" in text:
                            if time.time()-Program.last_update_time > 300.0:
                                print(time.time()-Program.last_update_time)
                                Program.last_update_time = time.time()
                                os.system(f"start {os.getcwd()}\\parser.py")
                                Program.send(self, id=id, text="Обновляю...", keyboard=None, receiver='user')
                            else:
                                Program.send(self, id=id, text=f"на абнову ищо {300-(time.time()-Program.last_update_time)}", keyboard=None, receiver='user')
                        else:
                            Program.send(self, id=id, text=Homework().Get(text,noperms=1), keyboard=None, receiver='user')
                    else:
                        Program.send(self, id=id, text=f"на месэдж ищо {5-(time.time()-Program.last_message_time)}", keyboard=None, receiver='user')
    

if __name__ == '__main__':
    while True:
        #try:
        Program()
        #except Exception as error:
           # print(error)
           # with open('crash_log.txt','w') as log:
           #     log.write(str(error))