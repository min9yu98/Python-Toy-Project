# 한겨레
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import random
import pyautogui
from selenium.webdriver.chrome.options import Options
import requests


driver = webdriver.Chrome(executable_path='C:/Users/kmkkm/Desktop/ChromeDriver/chromedriver_win32/chromedriver.exe')
url = 'https://www.hani.co.kr/'
driver.get(url)
time.sleep(3)

# 검색
time.sleep(3)
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
time.sleep(3)
pyautogui.click(518, 151)
driver.find_element(By.XPATH, '//*[@id="search_form"]/div/form/input[3]').send_keys('코로나')
driver.find_element(By.XPATH, '//*[@id="search_form"]/div/form/input[4]').click()

# 설정
driver.find_element(By.XPATH, '//*[@id="search-navi"]/ul/li[2]/h3/a').click()
driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/ul/li[2]/span/a').click()

driver.find_element(By.XPATH, '//*[@id="datefrom"]').click()
driver.find_element(By.XPATH, '//*[@id="datefrom"]').clear()
driver.find_element(By.XPATH, '//*[@id="datefrom"]').send_keys('20200101') # 시작 년월일
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="dateto"]').click()
driver.find_element(By.XPATH, '//*[@id="dateto"]').clear()
driver.find_element(By.XPATH, '//*[@id="dateto"]').send_keys('20200131') # 끝 년월일
driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/ul/li[5]/form/div/button').click()

time.sleep(3)
req_total = driver.page_source
bs_total = BeautifulSoup(req_total, 'lxml')
html_total = bs_total.find('span', {'class', 'total'}).get_text().split(' ')[0]
total_arti = int(html_total)



# 페이지 넘어가는 코드, 컴퓨터마다 다를 수 있습니다.
def next_page(page):
    want = driver.find_element_by_xpath('//*[@id="contents"]/div[4]').location['y'] - 760
    for _ in range(3):
        driver.execute_script("window.scrollTo(0," + str(want) + ");")
        time.sleep(2)
    mouse_dict = {11: (255, 938), 12: (284, 938), 13: (311, 938),
                  14: (342, 938), 15: (369, 938), 16: (399, 938),
                  17: (428, 938), 18: (456, 938), 19: (486, 938),
                  10: (520, 938), 'next1': (575, 938),
                  21: (225, 938), 22: (255, 938), 23: (299, 938), 24: (336, 938),
                  25: (374, 938), 26: (411, 938), 27: (446, 938), 28: (484, 938),
                  29: (522, 938), 20: (557, 938), 'next2': (639, 938),
                  31: (186, 938), 32: (237, 938), 33: (277, 938), 34: (320, 938),
                  35: (367, 938), 36: (415, 938), 37: (457, 938), 38: (503, 938),
                  39: (543, 938), 30: (588, 938), 'next3': (640, 938),}
    for _ in range(2):
        driver.execute_script("window.scrollTo(0," + str(want) + ");")
        time.sleep(2)
    pyautogui.click(mouse_dict[page][0], mouse_dict[page][1])



# 파일 저장
def write_article(arti):
    with open('C:/Users/kmkkm/Desktop/2020_1_han.txt', 'a', encoding='utf-8') as file: # 입력
        file.write(arti + "\n")



# 한 페이지에서의 url들
def urls_in_page():
    # driver.get(url)
    req = driver.page_source
    bs = BeautifulSoup(req, 'lxml')
    data_html = str(bs.find_all('dt')).split('<dt>')
    raw_urls = []
    for e in data_html:
        if 'href=' in e:
            raw_urls.append(e.split('"')[1])
    urls = []
    for e in raw_urls:
        urls.append(e.split('//')[1])
    return urls



# url에서의 기사들 긁어오기
def article(url, idx):
    url = 'https://' + url
    response = requests.get(url)
    time.sleep(1)
    html = response.text
    source = BeautifulSoup(html, 'html.parser')
    title = source.find('span', {'class': 'title'}).get_text()
    raw_contents = source.find_all('div', {'class': 'text'})[0].get_text()
    raw_contents = raw_contents.split(' ')
    arti = "[" + str(idx) + "]" + title + "     "
    for e in raw_contents:
        if '\n' in str(e):
            e = e.replace("\n", "")
        if '\r' in str(e):
            e = e.replace("\r", "")
        arti = arti + str(e) + " "
    return arti



total_page = int(total_arti / 10)
if total_page % 10 != 0:
    total_page += 1

idx = 0

for i in range(1, total_page + 1):
    page_first = len(str(i))
    page_second = i % 10
    page = page_first * 10 + page_second
    if i == 10:
        next_page(10)
    else:
        next_page(page)
    urls_list = urls_in_page()
    time.sleep(3)
    driver.implicitly_wait(30)
    for url in urls_list:
        write_article(article(url, idx))
        print(article(url, idx))
        time.sleep(2)
        idx += 1
    if i % 10 == 0:
        if i == 10:
            next_page('next1')
        else:
            next_page('next' + str(page_first))
        driver.implicitly_wait(30)
