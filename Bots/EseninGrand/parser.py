from selenium import webdriver
from selenium.webdriver.common.by import By


class Page:
    def __init__(self):
        self.__driver = webdriver.Firefox(executable_path=r'geckodriver')

    def getdriver(self):
        return self.__driver
