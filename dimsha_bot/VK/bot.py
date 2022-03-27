import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.keyboard import VkKeyboard, VkKeyboardColor, VkKeyboardButton
from vk_api.utils import get_random_id
import config


class Reply:
    help = """Бот отвечает только на сообщения, начинающиеся с <бот>
    Пример: бот места
    —————————————————
    Команды:
    - места
    - компания
    - фильтры"""

class Places:
    def __init__(self):
        with open('parser/data.json','r') as data:
            self.places = eval(data.read())
    
    def get_places_list_message(self):
        places_list = "Список заведений Железногорска:\n"
        for place in self.places.keys():
            places_list += "- " + place + '\n'
        return places_list
    
    def get_places_list(self):
        return self.places
    
    def get_place_info_message(place):
        message = ""
        for param in place.keys():
            message += param + ': ' + place[param] + '\n'
        return message

class Program:
    def __init__(self):
        self.token = config.token
        self.group_id = config.group_id

        
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
        self.keyboard_default.add_button("Бот рестарт", color=VkKeyboardColor.SECONDARY)
        self.keyboard_default.add_button("Бот места", color=VkKeyboardColor.SECONDARY)
        
        # is_bot_alive keyboard
        self.keyboard_isalive = VkKeyboard(one_time=False)
        self.keyboard_isalive.add_button("Ping", color=VkKeyboardColor.SECONDARY)
        
        # Места
        self.keyboard_places = VkKeyboard(one_time=False)
        for place in Places().get_places_list():
            self.keyboard_places.add_button(place, color=VkKeyboardColor.NEGATIVE)
        
    
    def listener(self):   
        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                text = event.object.message['text'].lower()
                
                # Беседа
                if event.from_chat:
                    id = event.chat_id
                    Program.send(self, id=id, text="Я получил ваше сообщение.", receiver='chat')
                # ЛС
                elif event.from_user:
                    id = event.object.message['from_id']
                    pl_list = Places().get_places_list()
                    
                    # Места
                    if "места" in text:
                        Program.send(self, id=id, text=Places().get_places_list_message(), keyboard=self.keyboard_places, receiver='user')
                    # Рестарт
                    elif "рестарт" in text:
                        Program.send(self, id=id, text="[INFO]: RELOAD...", keyboard=self.keyboard_isalive, receiver='user')
                        Program.restart()
                    # Получить информацию о месте
                    elif text in pl_list:
                        Program.send(self, id=id, text=Places.get_place_info_message(pl_list[text]), keyboard=self.keyboard_default, receiver='user')
                        
                    # is_bot_alive
                    elif "ping" in text:
                        Program.send(self, id=id, text="[INFO]: Pong!", keyboard=self.keyboard_default, receiver='user')
                    # default
                    else:
                        Program.send(self, id=id, text=Reply.help, keyboard=self.keyboard_default, receiver='user')
    
    def restart():
        config.is_restart = True
        import os
        program = os.getcwd() + "\\bot.py"
        os.system(f'start {program}')
        exit()

if __name__ == '__main__':
    while True:
        #try:
        Program()
        #except Exception as error:
           # print(error)
           # with open('crash_log.txt','w') as log:
           #     log.write(str(error))