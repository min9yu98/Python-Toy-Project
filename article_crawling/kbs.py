import re
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import random
import pyautogui
import requests


driver = webdriver.Chrome('C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe') # 입력
driver.implicitly_wait(30)
url = 'https://news.kbs.co.kr/search/search.do?query=%EC%BD%94%EB%A1%9C%EB%82%98#1'
# url = 'https://news.kbs.co.kr/news/view.do?ncd=5401996'
driver.get(url)
driver.implicitly_wait(30)

# 기간 설정
driver.find_element(By.XPATH, '//*[@id="btn-search-opt"]').click()
time.sleep(5)

#시작년
pyautogui.click(110, 631)
pyautogui.click(110, 631)
driver.find_element(By.XPATH, '//*[@id="date-select-from"]').clear()
driver.find_element(By.XPATH, '//*[@id="date-select-from"]').send_keys('2020.01.01')
time.sleep(5)
# 끝년
pyautogui.click(178, 640)
pyautogui.click(178, 640)
driver.find_element(By.XPATH, '//*[@id="date-select-to"]').clear()
driver.find_element(By.XPATH, '//*[@id="date-select-to"]').send_keys('2020.01.31')
pyautogui.click(292, 638)



def urls_in_page(url):
    req = driver.page_source
    bs = BeautifulSoup(req, 'lxml')
    html = str(bs.find('div', {'class', 'newslist-grid4'})).split('"')
    urls = []
    for element in html:
        element = str(element)
        if 'http:' in element or 'https:' in element:
            if 'png' not in element and 'jpg' not in element:
                urls.append(str(element))
    return urls



def article(url, idx):
    req = requests.get(url)
    html = req.text
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('h5').get_text()
    raw_contents = bs.select('#cont_newstext')
    contents = process(url, raw_contents)
    arti = '[' + str(idx) + ']' + title + '     ' + contents
    return arti



def process(url, raw_contents):
    req = requests.get(url)
    html = req.text
    bs = BeautifulSoup(html, 'html.parser')
    raw_contents = str(bs.select('#cont_newstext'))
    raw_contents = re.sub('<.+?>', '', raw_contents, 0).strip('[]')
    raw_contents = raw_contents.replace('\n', "")
    contents = raw_contents.replace('\t', "")
    return contents

urls_list = urls_in_page(driver.current_url)
print(urls_list)
for url in urls_list:
    print(article(url, 1))