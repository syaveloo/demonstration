class Driver:
    def __init__(self):
        self.__options = Options()
        self.__options.add_argument('--headless')
        self.__options.add_argument('--disable-gpu')
        self.__driver = webdriver.Chrome(r'{}'.format(self.__chromedriver), options=self.__options)

    def GetDriver(self):
        return self.__driver

    def QuitDriver(self):
        self.__driver.quit()

class Eljur:
    def __init__(self,driver,login,password,auth_eljur_url,weeknums=range(-2,3)):
        self.__driver = driver
        self.__login = login
        self.__weeknums = weeknums
        self.__password = password
        self.__auth_eljur_url = auth_eljur_url
        self.__weeks = list()

    def GetWeeknums(self):
        return Eljur.__weeknums

    def Auth(self):
        self.__driver.get(self.__auth_eljur_url)
        # Login
        self.__driver.find_element_by_xpath('/html/body/div/div/main/div/div/div/div[1]/form/div[1]/div[1]/div/input').send_keys(self.__login)
        # Password
        self.__driver.find_element_by_xpath('/html/body/div/div/main/div/div/div/div[1]/form/div[1]/div[2]/div/input').send_keys(self.__password)
        # Process authtorization
        self.__driver.find_element_by_xpath('//*[@id="loginviewport"]/div/div[1]/form/div[2]/button').click()
        time.sleep(5)

    def GoToWeek(self,weeknum):
        self.__driver.get(f"https://sch95.eljur.ru/journal-app/u.6700/week.{weeknum}")
        time.sleep(3)

class Week:
    def __init__(self,number):
        self.__number = number
        self.__days = list()

    def AddDay(self,day):
        self.__days.append(day)

    def GetDays(self):
        return self.__days

class Day:
    def __init__(self,driver):
        def DayName():
            return driver.find_element_by_xpath('.//div[@class="dnevnik-day__title"]').get_attribute("innerHTML").strip('\n').strip(' ').strip('\n')

        self.__name = DayName()
        self.__homework = homework

class Homework:
    def __init__(self,driver):
        pass


if __name__ == '__main__':
    # setup
    maindriver = Driver()
    eljur = Eljur(
        driver=maindriver.GetDriver(),
        auth_eljur_url="https://sch95.eljur.ru/authorize",
        login="aaa",
        password="bbb"
        )

    # auth
    eljur.Auth()

    #
    for weeknum in eljur.GetWeeknums():
        eljur.GoToWeek(weeknum)











'''
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
                        lessons[day_title][lesson_num].update({"name": lesson_name, "homework": lesson_homework})'''