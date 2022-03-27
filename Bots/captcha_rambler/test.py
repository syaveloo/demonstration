from selenium import webdriver
from selenium.webdriver.common.by import By
import config
from bs4 import BeautifulSoup as bs
import requests
import time


class Session:
    def __init__(self, url):
        self.__session = webdriver.Firefox()

        # connecting site
        self.__session.get(url)

    def find_using_xpath(self, xpath="", tag="", attributes=""):
        for i in range(5):
            try:
                return self.__session.find_element(
                    By.XPATH,
                    f"{xpath}"
                    )
            except Exception as e:
                print("one more attempt...")
                time.sleep(3)

    def click(self, element):
        print(element.get_attribute("innerHTML"))
        element.click()

    def get(self):

        # getter for session
        return self.__session



if __name__ == '__main__':
    session = Session(
        url="https://mail.rambler.ru/"
        )

    session.click(
        element = session.find_using_xpath(
            xpath = '/html/body/div[1]/div/div/div[2]/footer/div/a'
        )
    )

'''
a = requests.get("https://mail.rambler.ru/")
print( bs(a.text).prettify() )

'''