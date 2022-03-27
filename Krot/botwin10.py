import vk_api
import botcfg
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import cv2 as cv
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import ImageGrab
import random
import time
import requests
import asyncio

'''
Try with minimization:
https://stackoverflow.com/questions/19695214/screenshot-of-inactive-window-printwindow-win32gui
'''


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
            driver.execute_script(
                'arguments[0].click();', driver.find_element(By.XPATH, xpath))

        with open("accounts.txt", "a") as log:
            log.write(driver.find_element(
                By.XPATH, '//input[@id="password"]').get_attribute("value")
                + '?')
            log.write("male?")
        print("Password, Gender were saved.")

        # fill by text
        for xpath in ['//input[@id="fname"]', '//input[@id="lname"]',
                      '//input[@id="aaa__input"]',
                      '//input[@id="extra-email"]']:
            # fill non-random email
            if xpath == '//input[@id="extra-email"]':
                driver.find_element(By.XPATH, xpath).send_keys(
                    "grow1@gmail.com"
                )
                continue

            # random data
            rndm = ("%032x" % random.getrandbits(128))[:12]
            with open("accounts.txt", "a") as log:
                log.write(rndm + '?')

            # filling
            driver.find_element(By.XPATH, xpath).send_keys(
                rndm
                )
        print("Fname, Lname, Mail, Extramail were saved")

        # fill born date
        container = driver.find_element(
            By.XPATH,
            '/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/form/'
            + 'div[5]/div[2]/div')

        day = str(random.randint(1, 25))
        year = str(random.randint(1996, 2006))
        month = "Апрель"

        with open("accounts.txt", "a", encoding="utf-8") as log:
            log.write(day + '?' + month + '?' + year + '?')

        for xpath, txt in (
                ('//div[@class="select-0-2-120 daySelect-0-2-121"]',
                 day),
                ('//div[@class="base-0-2-99"]',
                 month),
                ('//div[@class="select-0-2-120 yearSelect-0-2-122"]',
                 year
                 )
        ):
            container.find_element(By.XPATH, xpath).click()
            container.find_element(By.XPATH, f'//*[text()="{txt}"]').click()
        print("Day, Month, Year were saved.")

        # click final button
        driver.execute_script('arguments[0].click();', driver.find_element(
            By.XPATH, "/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div"
            + "/form/button"))
        print("Final button clicked!")
        time.sleep(0.5)
        print("Fully completed.")

    def grab(self):
        img = ImageGrab.grab(bbox=(523, 287, 523+162, 287+66))
        img_np = np.array(img)
        captcha = cv.cvtColor(img_np, cv.COLOR_BGR2GRAY)
        print("Captcha grabbed succesfully!")
        return captcha


class Bot:
    def __init__(self):
        self.token = botcfg.token
        self.id = botcfg.id
        self.alb = '-212014760_283443747'
        self.version = '5.95'

    def auth(self):
        self.vk = vk_api.VkApi(token=self.token)
        self.longpoll = VkBotLongPoll(self.vk, self.id)

    def send_captcha(self):
        def getcaptcha():
            return main.getgrabber().grab()

        def get_url():
            r = requests.get('https://api.vk.com/method/photos.getUploadServer',
                             params={
                                 'access-token': self.token,
                                 'album-id': self.alb,
                                 'group_id': self.id,
                                 'v': self.version
                                 }).json()
            return r['response']['upload_url']

        url = get_url()

        file = getcaptcha()
        ur = requests.post(url, files=)

    def listen(self):
        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                text = event.object.message['text'].lower()

                if event.from_user:
                    id = event.object.message['from_id']

                    if text[0] == "!":
                        text = text[1:]

                        if text == "дай":
                            main.getgrabber().grab()


class Main:
    def __init__(self):
        pass

    def startgrabber(self):
        options = webdriver.FirefoxOptions()
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("dom.webnotifications.enabled", False)
        options.set_preference("media.volume_scale", '0.0')

        self.__grabber = Grabber(
            driver=webdriver.Firefox(
                executable_path=r"C://geckodriver.exe", options=options)
                )
        print("loading grabbed page...")
        time.sleep(2)
        print("done!\ngrabber started!")

    def startbot(self):
        self.__bot = Bot()
        self.__bot.auth()
        print("bot started!")
        self.__bot.listen()

    def getbot(self):
        return self.__bot

    def getgrabber(self):
        return self.__grabber


if __name__ == "__main__":
    main = Main()
    print("Firefox must be maximized, do not open an another applications"
          + "above browser. Grabbing happens by making screenshots, so.")
    input("Make sure that screen\'s resolution is 1024x768...")

    # start
    main.startgrabber()
    main.startbot()
