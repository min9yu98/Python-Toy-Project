#입력 필요 : 크롬 드라이버 설치 경로, 조선일보 ID, PassWord, 키워드, 기사를 저장할 공간의 경로
# pip install bs4, lxml, selenium, pyautogui, requests, tqdm 

import re
import pyautogui
import tqdm
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import random
import math
import requests
from selenium.common.exceptions import NoSuchElementException as NSEE




chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # 브라우저 창을 띄우지 않는 옵션
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36')  # headless 옵션으로 서버에서 차단당하지 않기위해 넣는 옵션
# driver = webdriver.Chrome('C:/Users/brain/Desktop/crawling/code/chromedriver.exe', options=chrome_options) # 입력


driver = webdriver.Chrome('C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe') # 입력
driver.implicitly_wait(30)
url = 'https://www.instagram.com/explore/tags/cat/'
driver.get(url)
driver.implicitly_wait(30)
time.sleep(4)

driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button').click()


def login(): # 로그인
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').click()
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('insta ID') #ID
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').click()
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('insta PWD') #PWD
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
    time.sleep(5)
    pyautogui.click(472, 642)
    time.sleep(5)
#     pyautogui.click(487, 719)
#     time.sleep(5)



def insta_urls(): # 페이지에 url 긁어오기
    html = driver.page_source
    bs = BeautifulSoup(html, 'lxml')
    source = str(bs.find_all('div')).split('"')
    insta_urls_ = []
    for e in source:
        if '/p/' in e:
            insta_urls_.append('https://www.instagram.com' + e)
    return insta_urls_



def insta_contents(url): # 긁어온 url에서 내용 빼오기
    driver.get(url)
    time.sleep(1.2)
    contents_html = driver.page_source
    contents_bs = BeautifulSoup(contents_html, 'lxml')
    contents = contents_bs.find('div', {'class', 'C4VMK'}).get_text()
    return contents



def waiting(): # 스크롤해서 데이터 더 불러오기
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(7)



time.sleep(3)
login()

rep = []

while True:
    waiting()
    urls = insta_urls()
    urls = tqdm.tqdm(urls)
    for e in urls:
        if e not in rep:
            rep.append(e)
    print(len(rep))
    if len(rep) >= 300:
        break

print(rep)
idx = 0
for url in rep:
    try:
        print(str(idx) + "----------" + insta_contents(url))
        time.sleep(random.randrange(1, 2))
        idx += 1
    except AttributeError:
        continue


# https://www.instagram.com/explore/tags/cat/
# driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
#
# time.sleep(5)
#
# pyautogui.click(472, 642)
#
# time.sleep(5)
#
# pyautogui.click(487, 719)
#
# time.sleep(5)
#
# driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').click()
# driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys('#cat')
