#입력 필요 : 크롬 드라이버 설치 경로, 조선일보 ID, PassWord, 키워드, 기사를 저장할 공간의 경로
import re
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import random
import pyautogui




# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')  # 브라우저 창을 띄우지 않는 옵션
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument(
#     'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36')  # headless 옵션으로 서버에서 차단당하지 않기위해 넣는 옵션
# driver = webdriver.Chrome('크롬 드라이버 설치 경로', options=chrome_options) # 입력


driver = webdriver.Chrome('C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe') # 입력
driver.implicitly_wait(30)
url = 'https://www.chosun.com/subscribe/signin/'
driver.get(url)
driver.implicitly_wait(30)



# 로그인 하기
driver.find_element(By.ID, 'username').click()
driver.find_element(By.NAME, 'username').send_keys('id') # 입력
driver.find_element(By.NAME, 'subsPassword').send_keys('pwd') # 입력
driver.find_element(By.ID, 'subsSignIn').click()
time.sleep(3)

# 로그인 후 메인 html url에서 코로나 검색
# 코로나 검색 후에 1개월, 뉴스, 관련도순 설정
pyautogui.click(89, 210)
driver.find_element(By.TAG_NAME, 'input').send_keys('코로나') # 입력
pyautogui.click(245, 202)
time.sleep(2)
# 관련도순
driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[1]/div[2]/div[1]').click()
time.sleep(2)
# 기간
driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[2]/div/div[1]/button').click()
driver.find_element(By.XPATH, '//*[@id="direct"]').click()  # 기간 직접입력
time.sleep(1)
# 시작 년 / 월 / 일
driver.find_element(By.ID, 'year_2020').click() # 시작 년도
driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[3]/ul[2]/li[1]').click() # 시작 월
driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[3]/ul[3]/li[1]').click() # 시작 일
driver.find_element(By.XPATH, '//*[@id="end"]').click()
time.sleep(1)
# 끝 년 / 월 / 일
driver.find_element(By.ID, 'year_2021').click() # 끝 년도
driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[3]/ul[2]/li[12]').click() # 끝 월
driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[3]/ul[3]/li[31]').click() # 끝 일
driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[2]/div/div[1]/div/div[3]/div[2]/button[1]').click()
time.sleep(3)

# 콘텐츠 카테고리
driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[2]/div/div[2]/button').click()
driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[2]/div/div[2]/div/div/div[2]').click()
driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[2]/div/div[2]/div/button').click()

time.sleep(3)
driver.implicitly_wait(30)



# 한 페이지에 있는 기사들의 url 구하기 + 총 기사 수 구하기
def url_in_page(url):
    driver.get(url)
    driver.implicitly_wait(30)
    time.sleep(random.randrange(1, 5))
    req = driver.page_source
    bs = BeautifulSoup(req, 'lxml')
    data_html = str(bs.findAll('p')).split('>')
    data_size = data_html[-2]
    data_size = re.findall(r'\d+', data_size)
    page_size = int(int(data_size[0]) / 10)
    if int(data_size[0]) % 10 != 0:
        page_size += 1
    lst = str(bs.findAll('div', 'story-card-wrapper')).split('><')
    lst_html = [element.split(' ') for element in lst]
    lst_url = []
    for e in lst_html:
        if e[0] == 'a':
            for element in e:
                if "href" in element:
                    lst_url.append(str(element))
    lst_url_rep = []
    for e in lst_url:
        if e not in lst_url_rep:
            lst_url_rep.append(e)
    urls = []
    for e in lst_url_rep:
        if '/people/' not in e and 'https:' in e:
            urls.append(e[6: len(e) - 1])
    return urls, page_size


# 각 url을 이용해 위 함수를 이용하여 기사들을 긁어오고 파일에 저장 - (무시 encoding='utf-8')
def write_article(arti):
    with open('C:/Users/user/Desktop/', 'a', encoding='utf-8') as file: # 입력
        file.write(arti + "\n")



# 기사의 url을 타고 들어가서 기사 긁어오고 다시 뒤로가기
def article(url, idx):
    driver.get(url)
    driver.implicitly_wait(30)
    time.sleep(random.randrange(1, 5))
    req = driver.page_source
    bs = BeautifulSoup(req, 'lxml')
    to_string = bs.findAll('p')
    words = [e.get_text() for e in to_string]
    title = bs.find('h1').get_text()
    arti = '[' + str(idx) + ']' + title + "     "
    for element in words:
        arti += element
    return arti



# 페이지 넘어가는 함수 : 직접 마우스의 좌표를 줘서 클릭하도록 한다.
def next_page(page):
    for _ in range(2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.randrange(1, 5))

    # 각 페이지별 좌표 ex) 11 -> 1, 108 -> 8
    mouse_dict = {11: (208, 310), 12: (243, 310), 13: (279, 310), 14: (314, 310), 15: (350, 310), 16: (386, 310),
                  17: (422, 310), 18: (461, 310), 19: (495, 310), 10: (533, 310), 'next': (564, 310),
                  21: (206, 310), 22: (242, 310), 23: (282, 310), 24: (314, 310), 25: (351, 310), 26: (386, 310),
                  27: (424, 310), 28: (458, 310), 29: (493, 310), 20: (531, 310), 'next2': (569, 310),
                  31: (207, 310), 32: (242, 310), 33: (278, 310), 34: (317, 310), 35: (348, 310), 36: (386, 310),
                  37: (420, 310), 38: (459, 310), 39: (493, 310), 30: (529, 310), 'next3': (568, 310)}
    for _ in range(2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.randrange(1, 5))
    # 클릭
    pyautogui.click(mouse_dict[page][0], mouse_dict[page][1])



idx = 0
page_limit = url_in_page(driver.current_url)[1]



for i in range(1, page_limit + 1):
    page_first = len(str(i))
    page_second = i % 10
    page = page_first * 10 + page_second
    if i == 10:
        next_page(10)
    else:
        next_page(page)
    main_url = driver.current_url
    time.sleep(2)
    urls_list = url_in_page(main_url)[0]
    for url in urls_list:
        write_article(article(url, idx))
        time.sleep(3)
        print(article(url, idx))
        idx += 1
    time.sleep(2)
    driver.get(main_url)
    driver.implicitly_wait(30)
    if i % 10 == 0:
        if i == 10:
            next_page('next')
        else:
            next_page('next' + str(page_first))
