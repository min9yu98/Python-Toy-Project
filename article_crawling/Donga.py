#입력 필요 : 크롬 드라이버 설치 경로, 조선일보 ID, PassWord, 키워드, 기사를 저장할 공간의 경로
import re

import pyautogui
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import random
import math
import requests



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # 브라우저 창을 띄우지 않는 옵션
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36')  # headless 옵션으로 서버에서 차단당하지 않기위해 넣는 옵션
# driver = webdriver.Chrome('C:/Users/brain/Desktop/crawling/code/chromedriver.exe', options=chrome_options) # 입력


driver = webdriver.Chrome('C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe') # 입력
driver.implicitly_wait(30)
url = 'https://www.donga.com/news/search?check_news=1&more=1&sorting=1&range=1&search_date=&v1=&v2=&query=%EC%BD%94%EB%A1%9C%EB%82%98'
driver.get(url)
driver.implicitly_wait(30)

driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/ul/li[6]/a').click()
driver.find_element(By.XPATH, '//*[@id="search_form_detail"]/div[1]/label[5]').click()
time.sleep(0.7)
driver.find_element(By.XPATH, '//*[@id="v1"]').click()
driver.find_element(By.XPATH, '//*[@id="v1"]').send_keys('20200101')
driver.find_element(By.XPATH, '//*[@id="v2"]').click()
driver.find_element(By.XPATH, '//*[@id="v2"]').send_keys('20200131')
time.sleep(0.7)
driver.find_element(By.XPATH, '//*[@id="search_form_detail"]/div[2]/input[2]').click()
time.sleep(0.7)
driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/h2/span[2]/img[3]').click()


total_html = driver.page_source
total_bs = BeautifulSoup(total_html, 'lxml')
total = int(total_bs.find('h2').get_text().split(' ')[3])

total //= 15
if total % 15 != 0:
    total += 1


def article(url, idx):
    req = requests.get(url)
    html = req.text
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('h1', {'class', 'title'}).get_text()

    raw_contents = bs.find('div', {'class', 'article_txt'}).get_text().split('\n')
    contents = []
    for e in raw_contents:
        if e == '좋아요 이미지좋아요':
            break
        if e == '\n' or e == '':
            continue
        contents.append(e)
    arti_body = ''
    for c in contents:
        if '\r' in c:
            c = c.replace('\r', '')
        arti_body += c
    arti = '[' + str(idx) + ']' + title + '     ' + arti_body
    return arti



def urls_in_page():
    html = driver.page_source
    bs = BeautifulSoup(html, 'lxml')
    raw_urls = str(bs.find_all('p', {'class', 'tit'})).split('"')
    urls = []
    for e in raw_urls:
        if 'https://www.donga.com' in e and 'pdf_viewer' not in e:
            urls.append(e)
    return urls



def next_page(page):
    mouse_dict = {11: (233, 640), 12: (264, 640), 13: (291, 640), 14: (320, 640), 15: (346, 640), 16: (374, 640)
                  , 17: (404, 640), 18: (430, 640), 19: (459, 640), 10: (493, 640), 'next1': (533, 640)
                  , 21: (225, 640), 22: (263, 640), 23: (300, 640), 24: (335, 640), 25: (370, 640), 26: (407, 640)
                  , 27: (444, 640), 28: (479, 640), 29: (516, 640), 20: (551, 640), 'next2': (592, 640)
                  , 31: (188, 640), 32: (238, 640), 33: (281, 640), 34: (322, 640), 35: (368, 640), 36: (409, 640)
                  , 37: (454, 640), 38: (499, 640), 39: (541, 640), 30: (587, 640), 'next3': (633, 640)}
    for _ in range(2):
        time.sleep(2)
        want = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[2]').location['y'] - 500
        driver.execute_script("window.scrollTo(0," + str(want) + ");")
    pyautogui.click(mouse_dict[page][0], mouse_dict[page][1])
    time.sleep(2)
    driver.implicitly_wait(30)



def write_article(arti):
    with open('C:/Users/user/Desktop/2020_1_donga.txt', 'a', encoding='utf-8') as file: # 입력
        file.write(arti + "\n")


idx = 0

for i in range(1, total + 2):
    if i == 10:
        next_page(10)
    elif i != 10 and str(i)[-1] != '1':
        next = str(len(str(i))) + str(i)[-1]
        next_page(int(next))

    urls = urls_in_page()
    for url in urls:
        try:
            write_article(article(url, idx))
            print(article(url, idx))
        except AttributeError:
            continue
        idx += 1
        time.sleep(1.3)

    if i % 10 == 0:
        if i == 10:
            next_page('next1')
        else:
            next_page('next' + str(len(str(i))))
