from postgresql import Connection
from parser import Page, By
from time import sleep


class Xpaths:
    threads = '''/html/body/div[1]
                 /div[4]/div/div[2]
                 /div/div/div/div[2]
                 /div[2]/div'''

    cookies_button = '/html/body/div[2]/ul/li/div/div[2]/a[1]/span'

    thread_title = '/div[2]/div[1]/a[2]'


class Parser:
    def __init__(self):
        driver = Page().getdriver()

        def thread(text):
            """ Interact with threads on forum """
            thread = driver.find_element(
                    By.XPATH, f'//a[text()={text}]'
                )
            return thread

        def click3(elem):
            """ Click + wait 3 secs """
            elem.click()
            sleep(3)

        def accept_cookies():
            """ To hide trash button obscured by """
            try:
                driver.find_element(
                    By.XPATH, Xpaths.cookies_button
                ).click()
            except Exception:
                pass

        """ Executing """
        driver.get('https://forum.grand-rp.su/')    # load page
        sleep(3)

        # no comments
        accept_cookies()

        # go thread about server #2
        click3(
            thread(
                text="\"Игровой сервер II\""
                )
        )

        # go thread with leader offers
        click3(
            thread(
                text="\"Заявления на пост лидера\""
                )
        )

        # it`ll be all offers
        threads = driver.find_elements(
            By.XPATH, '//*[contains(text(), "Заявление на пост лидера")]'
        )

        # create offers list
        offers = []
        for i in range(0, len(threads)):
            offers[i] = threads[i].get_attribute("href")


class Main:
    def __init__(self):
        """ Stuff """
        self.__dbase = Connection(
                host='0000.0000.000',
                dbname='postgres',
                user='postgres',
                passwd='000',
                port=5432
            )
        Parser()


if __name__ == '__main__':
    Main()
