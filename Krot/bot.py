import vk_api
import botcfg
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import cv2 as cv
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import ImageGrab
import random
import time


class Grabber:
    def __init__(self, driver):
        self.__driver = driver

        # open captcha page
        self.__driver.get("https://account.mail.ru/signup")
        driver = self.__driver
        time.sleep(5)

        # fill forms by click
        for xpath in ['/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/'
                      + 'form/div[14]/span/a',
                      '/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/'
                      + 'form/div[17]/span/a',
                      '/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div'
                      + '/form/div[8]/div[2]/div/label[1]/div[1]/div[2]']:
            driver.find_element(By.XPATH, xpath).click()

        # fill by text
        for xpath in ['//input[@id="fname"]', '//input[@id="lname"]',
                      '//input[@id="aaa__input"]',
                      '//input[@id="extra-email"]']:
            # fill non-random email
            if xpath == '//input[@id="extra-email"]':
                driver.find_element(By.XPATH, xpath).send_keys(
                    "grow142@gmail.com"
                )
                continue

            # random data
            rndm = "%032x" % random.getrandbits(128)

            # filling
            driver.find_element(By.XPATH, xpath).send_keys(
                rndm[:12]
                )

        # fill born date
        container = driver.find_element(
            By.XPATH,
            '/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/form/'
            + 'div[5]/div[2]/div')
        for xpath, txt in (
                ('//div[@class="select-0-2-120 daySelect-0-2-121"]',
                 random.randint(1, 25)),
                ('//div[@class="base-0-2-99"]',
                 "Апрель"),
                ('//div[@class="select-0-2-120 yearSelect-0-2-122"]',
                 random.randint(1996, 2006)
                 )
        ):
            container.find_element(By.XPATH, xpath).click()
            container.find_element(By.XPATH, f'//*[text()="{txt}"]').click()

        # click final button
        driver.find_element(By.XPATH, "/ html/body/div[1]/div[3]/div[3]/div[4]"
                            + "/div/div/div/div/form/button").click()

        time.sleep(0.5)

        return

    def grab(self):
        img = ImageGrab.grab(bbox=(523, 287, 162, 66))
        img_np = np.array(img)
        captcha = cv.cvtColor(img_np, cv.COLOR_BGR2GRAY)
        return captcha


class Bot:
    def __init__(self):
        self.token = botcfg.token
        self.id = botcfg.id

    def auth(self):
        self.vk = vk_api.VkApi(token=self.token)
        self.longpoll = VkBotLongPoll(self.vk, self.id)

    def listen(self):
        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                text = event.object.message['text'].lower()

                if event.from_user:
                    id = event.object.message['from_id']

                    if text[0] == "!":
                        text = text[1:]

                        if text == "дай":
                            pass


if __name__ == "__main__":
    bot = Bot()
    bot.auth()

    options = webdriver.FirefoxOptions()
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference("dom.webnotifications.enabled", False)
    options.set_preference("media.volume_scale", '0.0')

    grab = Grabber(
        driver=webdriver.Firefox(
            executable_path=r"geckodriver", options=options)
            )

    captcha = grab.grab()
    cv.imshow("captcha", captcha)
    cv.waitKey(0)
