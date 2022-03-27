class Homework:
    def __init__(self):
        def RunBrowser(self):
            cd = os.getcwd() + r'chromedriver.exe'
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            self.driver = webdriver.Chrome(r'{}'.format(cd), options=options)
        def Auth(login,password):
            """ Authtorization """
            cd = os.getcwd() + r'\chromedriver.exe'
            self.driver = webdriver.Chrome(r'{}'.format(cd))
            self.driver.minimize_window()
            self.driver.get("https://sch95.eljur.ru/authorize")
            time.sleep(3)
            login_form = self.driver.find_element_by_xpath('/html/body/div/div/main/div/div/div/div[1]/form/div[1]/div[1]/div/input').send_keys("DimshutniK")
            password_form = self.driver.find_element_by_xpath('/html/body/div/div/main/div/div/div/div[1]/form/div[1]/div[2]/div/input').send_keys("MeKoNG1389")
            button = self.driver.find_element_by_xpath('//*[@id="loginviewport"]/div/div[1]/form/div[2]/button').click()
            time.sleep(5)
            return "ok"
        def AddUpdateTime(homework):
            return {"UpdateTime": time.strftime("%c"), "Homework": homework}
        def SaveHomework(homework):
            with open("homework.json","w", encoding='utf8') as file:
                json.dump(homework,file,ensure_ascii=False)
            return "ok"
        # run browser
        RunBrowser(self)
        # auth
        print("Auth:",Auth(login=parser_config.login, password=parser_config.password))
        # get homework
        homework = Homework.GetHomework(self)
        # add update time
        homework = AddUpdateTime(homework)
        print("UpdateTime:",homework["UpdateTime"])
        # save homework
        print("SaveHomework:",SaveHomework(homework))
    
    def GetHomework(self):
        page = self.driver
        
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
        
        lessons = {}
        for weeknum in ["2","1","0","-1","-2"]:
            days = GetDays(weeknum)
            lessons[weeknum]=GetLessons(days)

        return lessons