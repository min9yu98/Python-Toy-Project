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
driver.find_element(By.XPATH, '//*[@id="schedule2"]/div/table/tbody/tr[5]/td[6]').click()  # 일

driver.find_element(By.XPATH, '//*[@id="container"]/div[3]/div/ul/li[2]/a').click()


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



def next_page(num):
    ten_page = {'next'}