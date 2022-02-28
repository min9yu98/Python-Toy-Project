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
url = 'https://imnews.imbc.com/more/search/?search_kwd=%EC%BD%94%EB%A1%9C%EB%82%98#page=0'
driver.get(url)

driver.find_element(By.XPATH, '//*[@id="result"]/div[1]/div[1]/form/fieldset/div[2]/button[1]').click()

driver.find_element(By.XPATH, '//*[@id="result"]/div[1]/div[2]/form/fieldset/div[1]/ul/li[1]').click()
driver.find_element(By.XPATH, '//*[@id="result"]/div[1]/div[2]/form/fieldset/div[1]/ul/li[2]').click()
driver.find_element(By.XPATH, '//*[@id="result"]/div[1]/div[2]/form/fieldset/div[1]/ul/li[3]').click()
driver.find_element(By.XPATH, '//*[@id="result"]/div[1]/div[2]/form/fieldset/div[1]/ul/li[4]').click()
driver.find_element(By.XPATH, '//*[@id="result"]/div[1]/div[2]/form/fieldset/div[1]/ul/li[5]').click()
driver.find_element(By.XPATH, '//*[@id="result"]/div[1]/div[2]/form/fieldset/div[1]/ul/li[6]').click()

driver.find_element(By.XPATH, '//*[@id="result"]/div[1]/div[2]/form/fieldset/div[2]/ul/li[1]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="result"]/div[2]/div/div[2]/div[2]/a[2]').click()

driver.find_element(By.XPATH, '//*[@id="startDatepicker"]').click()
driver.find_element(By.XPATH, '//*[@id="startDatepicker"]').send_keys('20200101')

driver.find_element(By.XPATH, '//*[@id="endDatepicker"]').click()
driver.find_element(By.XPATH, '//*[@id="endDatepicker"]').send_keys('20200131')

driver.find_element(By.XPATH, '//*[@id="result"]/div[1]/div[2]/form/fieldset/div[3]/div/div[2]/button').click()

driver.find_element(By.XPATH, '//*[@id="result"]/div[1]/div[1]/form/fieldset/div[2]/button[1]').click()



def urls_in_page():
    source = driver.page_source
    html = BeautifulSoup(source, 'lxml')
    raw_urls = str(html.find_all('li', {'class', 'item'})).split('><')
    urls = []
    for element in raw_urls:
        if 'a href' in element:
            element = element[8:-1]
            urls.append("https://imnews.imbc.com/" + str(element))
    return urls



def article(url):
    start = requests.get(url)
    html = start.text
    source = BeautifulSoup(html, 'html.parser')
    raw_contents = source.find_all('div', {'class', 'news_txt'})
    contents = ""
    for e in raw_contents:
        contents += e.get_text()
    contents = contents.replace("     ", "")
    contents = contents.lstrip()
    title = source.find('h2', {'class', 'art_title'}).get_text()
    arti = title + "    " + contents # arti 앞에 [index] 넣어줘야함
    return arti



def total_arti():
    time.sleep(3)
    total_source = driver.page_source
    total_html = BeautifulSoup(total_source, 'lxml')
    total = int(total_html.find('strong', {'class', 'num'}).get_text().replace(",", ""))
    return total



def write_article(arti):
    with open('C:/Users/user/Desktop/', 'a', encoding='utf-8') as file: # 입력
        file.write(arti + "\n")



def next_page():
    for _ in range(3):
        time.sleep(1.5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    pyautogui.click(536, 776)



# total = total_arti()
# page = total // 5
# if total % 5 != 0:
#     page += 1
#
# idx = 0

# for i in range(page):
#     urls = urls_in_page()
#     for  url in urls:
#         # write_article(article(url))
#         print(article(url))
#     next_page()
