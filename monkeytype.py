from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from pynput.keyboard import Key, Controller
import random



keyboard = Controller()

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
driver = webdriver.Chrome()
driver.get("https://monkeytype.com") 
time.sleep(4)


for i in range(5):
    print("Get ready... {}".format(5 - i))
    time.sleep(1)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
time.sleep(2)

raw = driver.page_source
soup = BeautifulSoup(raw, "html.parser")
content = soup.find_all(class_ = "word")

count = 0

for word in content:
    if len(soup) == 0:
        break
    if len(word) == 0:
        break
    newsoup = BeautifulSoup(str(word), "html.parser")
    final = (newsoup.find_all("letter"))
    for i in final:
        if count < len(word):
            scuff = random.randint(0, 100)
            if scuff == 50:
                keyboard.type(random.choice(alphabet))
                # untuk pura'' salah ketik agar tidak terdetek bot
            else:
                keyboard.type(str(i.text))
                time.sleep(random.uniform(0.08, 0.1))
            count += 1
        if count == len(word):
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            count = 0          

