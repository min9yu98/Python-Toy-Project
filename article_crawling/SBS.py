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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe')
url = 'https://news.sbs.co.kr/news/search/main.do?query=%EC%BD%94%EB%A1%9C%EB%82%98&pageIdx=1&searchOption=1&collection='
driver.get(url)

driver.find_element(By.XPATH, '//*[@id="searchForm"]/fieldset/div[2]/ul/li[4]/div[1]').click()

driver.find_element(By.XPATH, '//*[@id="searchStartDate"]').click()
driver.find_element(By.XPATH, '//*[@id="calendarselectYear"]').click()

driver.find_element(By.XPATH, '//*[@id="calendarselectYear"]/option[3]').click()  # 년 2021 3->2
driver.find_element(By.XPATH, '//*[@id="calendarselectMonth"]/option[1]').click()  # 일
driver.find_element(By.XPATH, '//*[@id="schedule"]/div/table/tbody/tr[1]/td[4]/button').click()  # 일

time.sleep(random.randrange(1, 3))

driver.find_element(By.XPATH, '//*[@id="searchEndDate"]').click()
driver.find_element(By.XPATH, '//*[@id="calendar2selectYear"]/option[3]').click()  # 년 2021 3->2
driver.find_element(By.XPATH, '//*[@id="calendar2selectMonth"]/option[1]').click()  # 월
driver.find_element(By.XPATH, '//*[@id="schedule2"]/div/table/tbody/tr[5]/td[6]/button').click()  # 일

driver.find_element(By.XPATH, '//*[@id="searchBt"]').click()

driver.find_element(By.XPATH, '//*[@id="container"]/div[3]/div/ul/li[2]/a').click()

source_total = driver.page_source
html_total = BeautifulSoup(source_total, 'lxml')
raw_total = str(html_total.find('strong', {'class', 'psr_num'}).get_text()).split('/')
total = raw_total[-1][:-1]
if ',' in total:
    total = total.replace(",", "")
page_total = int(total) // 10
if page_total % 10 != 0:
    page_total += 1

def url_in_page():
    req = driver.page_source
    html = BeautifulSoup(req, 'lxml')
    element = str(html.find_all('a', {'class', 'psil_link'})).split(' ')
    urls = []
    for e in element:
        if "href" in str(e):
            urls.append(str(e)[6:-1])
    return urls



def article(url, idx):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find_all('h3')
    for e in title:
        if "vmNewsTitle" in str(e):
            title = e.get_text()
            break
    contents = soup.find('div', {'class', 'text_area'}).get_text().replace("\n", "")
    contents = contents.replace("   ", "")
    arti = "[" + str(idx) + "]" + title + "     " + contents
    return arti



def next_page(page):
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    mouse_dict = {'next1': (622, 253), 11: (359, 253), 12: (388, 253), 13: (415, 253), 14: (441, 253), 15: (463, 253)
        , 16: (492, 253), 17: (518, 253), 18: (543, 253), 19: (568, 253), 10: (595, 253)
                , 'next2': (621, 253), 21: (362, 253), 22: (388, 253), 23: (414, 253), 24: (441, 253), 25: (467, 253)
        , 26: (493, 253), 27: (516, 253), 28: (543, 253), 29: (570, 253), 20: (598, 253)
                , 'next3': (656, 253), 31: (331, 253), 32: (364, 253), 33: (394, 253), 34: (427, 253), 35: (457, 253)
        , 36: (496, 253), 37: (532, 253), 38: (561, 253), 39: (594, 253), 30: (628, 253)}
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    pyautogui.click(mouse_dict[page][0], mouse_dict[page][1])



def write_article(arti):
    with open('C:/Users/user/Desktop/', 'a', encoding='utf-8') as file: # 입력
        file.write(arti + "\n")


idx = 0

for i in range(1, page_total + 1):
    if i == 10:
        next_page(10)
    elif i != 10 and str(i)[-1] != '1':
        next = str(len(str(i))) + str(i)[-1]
        next_page(int(next))

    urls = url_in_page()
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

