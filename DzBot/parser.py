from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import os
import time
import json
import parser_config



class Browser:
    __driver = None
    __options = None
    __chromedriver = None

    def __init__(self,chromedriver,login,password,auth_eljur_url):
        self.__chromedriver = chromedriver
        self.__auth_eljur_url = auth_eljur_url
        self.__login = login
        self.__password = password

        self.__options = Options()
        self.__options.add_argument('--headless')
        self.__options.add_argument('--disable-gpu')
        self.__driver = webdriver.Chrome(r'{}'.format(self.__chromedriver), options=self.__options)

    def GetDriver(self):
        return self.__driver

    def Quit(self):
        self.__driver.quit()

    def FindElementXpath(self,xpath):
        return Browser.__driver.find_element_by_xpath(xpath)

    def AuthBotEljur(self):
        self.__driver.get(self.__auth_eljur_url)
        # Login
        self.__driver.find_element_by_xpath('/html/body/div/div/main/div/div/div/div[1]/form/div[1]/div[1]/div/input').send_keys(self.__login)
        # Password
        self.__driver.find_element_by_xpath('/html/body/div/div/main/div/div/div/div[1]/form/div[1]/div[2]/div/input').send_keys(self.__password)
        # Process authtorization
        self.__driver.find_element_by_xpath('//*[@id="loginviewport"]/div/div[1]/form/div[2]/button').click()
        time.sleep(5)

    def UpdateEljurHomework(self):
        page = self.__driver
        def GetDays(weeknum=0):
            page.get(f"https://sch95.eljur.ru/journal-app/u.6700/week.{weeknum}")
            days = page.find_elements_by_class_name("dnevnik-day")
            return days
        def GetChildrens(webelement):
            return webelement.find_elements_by_xpath('.//*')
        def GetLessons(days):
            def GetLessonName(lesson):
                return lesson.find_element_by_xpath('.//span[@class="js-rt_licey-dnevnik-subject"]').get_attribute("innerHTML").strip('\n').strip(' ')
            def GetLessonNum(lesson):
                return lesson.find_element_by_xpath('.//div[@class="dnevnik-lesson__number dnevnik-lesson__number--time"]').get_attribute("innerHTML").strip('\n').strip(' ')
            def GetLessonHomework(lesson):
                    homeworks = lesson.find_elements_by_xpath('.//div[@class="dnevnik-lesson__task"]')
                    if not homeworks:
                        return "Нет задания"
                    homework = ""
                    for dz in homeworks:
                        homework += dz.text
                    return homework
            def GetDayTitle(day):
                return day.find_element_by_xpath('.//div[@class="dnevnik-day__title"]').get_attribute("innerHTML").strip('\n').strip(' ').strip('\n')
            def GetLessons(day):
                return day.find_elements_by_xpath('.//div[@class="dnevnik-lesson"]')
                
            
            lessons = {}
            for day in days:
                day_lessons = GetLessons(day)
                day_title = GetDayTitle(day)
                if "Суббота" not in day_title:
                    lessons[day_title] = {}
                    for lesson in day_lessons:
                        lesson_num = GetLessonNum(lesson)
                        if lesson_num != '':
                            lesson_name = GetLessonName(lesson)
                            lesson_homework = GetLessonHomework(lesson)
                            lessons[day_title][lesson_num] = {}
                            lessons[day_title][lesson_num].update({"name": lesson_name, "homework": lesson_homework})
            return lessons
        
        # Starts here
        lessons = {}
        for weeknum in ["2","1","0","-1","-2"]:
            days = GetDays(weeknum)
            lessons[weeknum]=GetLessons(days)

        self.__EljurHomework = lessons

    def GetEljurHomework(self):
        return self.__EljurHomework

    def PushEljurHomework(self):
        with open("homework.json","w", encoding='utf8') as file:
            json.dump(self.__EljurHomework,file,ensure_ascii=False)



if __name__ == '__main__':
    # setup
    browser = Browser(
        chromedriver=parser_config.chromedriver,
        login = parser_config.login,
        password = parser_config.password,
        auth_eljur_url = "https://sch95.eljur.ru/authorize"
        )
    # auth
    browser.AuthBotEljur()
    # update homework
    browser.UpdateEljurHomework()
    # push homework
    browser.PushEljurHomework()
    # quit
    browser.Quit()

