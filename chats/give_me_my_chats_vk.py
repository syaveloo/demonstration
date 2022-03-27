from selenium import webdriver
from time import sleep
import json

driver = webdriver.Chrome(r'C:\\chromedriver_95.0.4638.54.exe')
driver.get("https://vk.com")

auth = input("Press any key when you have login to your page...")
count = int(input("Enter how a lot of chats you wanna check (number): "))
keyword = input("Enter keyword to find if you want: ")

chats = {}
for x in range(1, count+1):
    try:
        driver.get(f"https://vk.com/im?sel=c{x}")
        sleep(2)
        
        element = driver.find_element_by_xpath('//a[@class="im-page--title-main-inner _im_page_peer_name"]')
        chatname = element.get_attribute("innerHTML").replace("&nbsp;","")
        chats[x]=chatname
        
        if keyword in chatname:
            exit()
        
        x+=1
    except Exception:
        pass
with open("chats.json","w", encoding='utf8') as file:
    json.dump(chats,file,ensure_ascii=False)