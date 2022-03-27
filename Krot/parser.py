from selenium import webdriver
from webdriver.common.by import By
import random


class Grabber:
    def __init__(self, driver, outdir):
        self.__driver = driver
        self.outdir = outdir

    def start(self, url):
        self.__driver.get(url)
        count = int(input("Enter count (integer) of captchas:"))
        print("Make sure that you've fill form and it's page with captcha")
        input("Press any key to continue...")
        for _ in range(count):
            name = "%32x" % random.getrandbits(128)
            cpha = self.__driver.find(
                By.XPATH, '//img[@class="styles-mobile__captchaImage--sHzh3"]')
            #cpha.get_attribute("src").click()


if __name__ == "__main__":
    gr = Grabber()
