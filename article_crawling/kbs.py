import re
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import random
import pyautogui
import requests
import selenium
from selenium.common.exceptions import ElementClickInterceptedException


driver = webdriver.Chrome('C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe') # 입력
driver.implicitly_wait(30)
url = 'https://news.kbs.co.kr/search/search.do?query=%EC%BD%94%EB%A1%9C%EB%82%98#1'
driver.get(url)
driver.implicitly_wait(30)

# 기간 설정
driver.find_element(By.XPATH, '//*[@id="btn-search-opt"]').click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="dt_cal"]').click()
driver.find_element(By.XPATH, '//*[@id="date-select-from"]').clear()
driver.find_element(By.XPATH, '//*[@id="date-select-from"]').send_keys('2020.01.01') # 시작

pyautogui.press('tab')

driver.find_element(By.XPATH, '//*[@id="date-select-to"]').clear()
driver.find_element(By.XPATH, '//*[@id="date-select-to"]').send_keys('2020.01.31') # 

pyautogui.click(291, 642)



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



def write_article(arti):
    with open('C:/Users/user/Desktop/', 'a', encoding='utf-8') as file: # 입력
        file.write(arti + "\n")



def process(url, raw_contents):
    req = requests.get(url)
    html = req.text
    bs = BeautifulSoup(html, 'html.parser')
    raw_contents = str(bs.select('#cont_newstext'))
    raw_contents = re.sub('<.+?>', '', raw_contents, 0).strip('[]')
    raw_contents = raw_contents.replace('\n', "")
    contents = raw_contents.replace('\t', "")
    return contents



def next_page():
    for _ in range(2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.randrange(1, 5))
    driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div[5]/a[2]').click()
    for _ in range(2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.randrange(1, 5))



paging_html = driver.page_source
paging_bs = BeautifulSoup(paging_html, 'lxml')
raw_total = str(paging_bs.find('em', {'class', 'num'}).get_text())
total = int(raw_total.replace(",", ""))
total_click_cnt = total // 10
if total % 10 != 0:
    total_click_cnt += 1

idx = 0

for i in range(total_click_cnt):
    urls_list = urls_in_page(driver.current_url)
    for url in urls_list:
        try:
            write_article(article(url, idx))
            print(article(url, idx))
        except requests.exceptions.InvalidSchema:
            continue
        idx += 1
        time.sleep(1)
    next_page()
    time.sleep(random.randrange(3, 7))
