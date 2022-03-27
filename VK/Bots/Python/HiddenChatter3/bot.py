import vk_api
import cfg
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

class Bot:
    def __init__(self):
        self.token = cfg.token
        self.id = cfg.id

    def auth(self):
        self.vk = vk_api.VkApi(token=self.token)
        self.longpoll = VkBotLongPoll(self.vk, self.id)
    
    def listen(self):
        for event in self.longpoll.listen():
            
            if event.type == VkBotEventType.MESSAGE_NEW:
                text = event.object.message['text'].lower()
                
                if event.from_user:
                    id = event.object.message['from_id']
                    




if __name__ == "__main__":
    bot = Bot()
    bot.auth()