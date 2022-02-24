#입력 필요 : 크롬 드라이버 설치 경로, 조선일보 ID, PassWord, 키워드, 기사를 저장할 공간의 경로
import re
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import random
import math
import requests
import pyautogui


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # 브라우저 창을 띄우지 않는 옵션
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36')  # headless 옵션으로 서버에서 차단당하지 않기위해 넣는 옵션
# driver = webdriver.Chrome('C:/Users/brain/Desktop/crawling/code/chromedriver.exe', options=chrome_options) # 입력



driver = webdriver.Chrome('C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe') # 입력
driver.implicitly_wait(30)
url = 'https://account.joongang.co.kr/login?targetURL=https%3A%2F%2Fwww.joongang.co.kr%2F'
driver.get(url)
driver.implicitly_wait(30)


# 로그인 하기
driver.find_element(By.NAME, 'txtEmail').click()
driver.find_element(By.NAME, 'txtEmail').send_keys('중앙일보id') # 입력
driver.find_element(By.NAME, 'txtPasswd').send_keys('중앙일보pwd*') # 입력
driver.find_element(By.XPATH, '//*[@id="emailForm"]/div[4]/button').click()
driver.implicitly_wait(10)


driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div/nav/button[2]').click()
driver.find_element(By.CLASS_NAME, 'search_form').click()
driver.find_element(By.XPATH, '//*[@id="layer_search"]/div/div[2]/form/div/div/p').send_keys('코로나') # 입력 keyword
driver.find_element(By.XPATH, '//*[@id="layer_search"]/div/div[2]/form/div/button').click()
time.sleep(2)
driver.implicitly_wait(30)


# 년, 월 구하기 - 직접 기간 입력할 때 필요
driver.get(driver.current_url)
req = driver.page_source
bs = BeautifulSoup(req, 'lxml')
html = str(bs.find('div', 'ui-datepicker-title').get_text())
html = html.split()
year, month = int(html[0][:-1]), int(html[1][:-1]) 
# 긁을 날마다 설정
cnt_start = (year - 2020) * 12 + (month - 1) 
cnt_end = (year - 2020) * 12 + (month - 1)


# 직접 기간 입력
driver.find_element(By.XPATH, '//*[@id="sticky"]/form/div/button[2]').click()
# 매체 - 중앙일보
driver.find_element(By.XPATH, '//*[@id="detail_form"]/div[4]/ul/li[2]/label/span').click()
# 직접 설정
driver.find_element(By.XPATH, '//*[@id="detail_form"]/div[1]/ul/li[5]/span[1]/label').click()

# 번거롭지만 직접 xpath이용해서 
# 시작 년/월/일
driver.find_element(By.XPATH, '//*[@id="detail_form"]/div[1]/ul/li[5]/span[2]').click() # 시작
time.sleep(2)
for _ in range(cnt_start):
    time.sleep(0.7)
    driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[1]').click()
driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[4]/a').click()
# 끝 년/월/일
driver.find_element(By.XPATH, '//*[@id="detail_form"]/div[1]/ul/li[5]/span[3]/img').click()
time.sleep(2)
for _ in range(cnt_end):
    time.sleep(0.7)
    driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[1]').click()
driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[6]/a').click()
# 확인
driver.find_element(By.XPATH, '//*[@id="search_detail"]').click()
# 기사 전체보기
driver.find_element(By.XPATH, '//*[@id="tab1"]/button').click()

# 추가 설정 - 정확도 순
driver.find_element(By.XPATH, '//*[@id="container"]/section/div/section/header/div[2]/div/button').click()
driver.find_element(By.XPATH, '//*[@id="dropdown"]/ul/li[2]/a').click()



#총 뉴스 기사 수
req = driver.page_source
bs = BeautifulSoup(req, 'lxml')
string = ""
html = bs.findAll('span')
for i in range(1, len(html) - 1):
    if html[i - 1].get_text() == '뒤로가기' and html[i + 1].get_text() == '건':
        total_arti_cnt = int(re.sub(',', '', html[i].get_text()))

total_page_click_cnt = math.ceil(total_arti_cnt / 24) # 총 클릭할 페이지 수



# 더보기를 끝까지 눌러서 모든 기사 불러오기
for i in range(total_page_click_cnt - 1):
    if int(total_page_click_cnt / 100) == i:
        time.sleep(random.randrange(5, 10))
    last_height = driver.execute_script("return document.body.scrollHeight")
    click2height = last_height - 2000
    driver.execute_script("window.scrollTo(0, " + str(click2height) + ");")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, " + str(click2height) + ");")
    pyautogui.click(476, 710)
    driver.implicitly_wait(30)
    time.sleep(10)



# 기사 긁어오기
def article(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h1').get_text()
    title = title.replace('\n', "")
    raw_raw_content = soup.find('div', {'id': 'article_body'})
    raw_content = raw_raw_content.findAll('p', {'class': ''})
    arti = ""
    for c in raw_content:
        arti += c.get_text()
        arti = re.sub("  ", "", arti)
        arti = arti.replace('\n', "")
    return title, arti



# 각 url을 이용해 위 함수를 이용하여 기사들을 긁어오고 파일에 저장 - (무시 encoding='utf-8')
def write_article(arti):
    with open('C:/Users/user/Desktop/', 'a', encoding='utf-8') as file: # 입력
        file.write(arti + "\n")



# 동적으로 페이지를 불러온 뒤 url들을 가져온다 -> 더보기로 기사를 늘렸을 때 url을 가져올 수 있게 된다.
req = driver.page_source
soup = BeautifulSoup(req, 'lxml')
time.sleep(10)
url_html = str(soup.findAll('h2', 'headline')).split('">')
url_list_ = []
for e in url_html:
    if 'href=' in e:
        url_list_.append(e[10:])
url_list_ = url_list_[5:-5]

arti_idx = 0


# 동적 크롤링을 이용해서 긁어온 url들을 이용하여 정적으로 크롤링을 한다.
# 실행
while True:
    time.sleep(3)
    for url in url_list_:
        time.sleep(random.randrange(1, 5))
        title_, contents_ = article(url)
        total_arti = ""
        total_arti += "[" + str(arti_idx) + "]" + title_ + "   " + contents_
        print(total_arti) # 진행상황을 보기위한 코드
        write_article(total_arti)
        arti_idx += 1
    driver.quit()
    break
