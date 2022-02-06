# 크롤링을 통해 커뮤니티 핫딜 게시판에서 원하는 물품 유무? 확인

import requests
from bs4 import BeautifulSoup
import time

# FM Korea 핫딜 게시판
url_fm = "https://www.fmkorea.com/hotdeal"
def fm(url):
	webpage = requests.get(url)
	soup = BeautifulSoup(webpage.content, "html.parser")
	lst_fm = [soup.select(".li_best2_pop0")[x].get_text() for x in range(20)] # 클래스를 이용하여 핫딜 게시판 물품 정보 긁어오기
	for e in lst_fm:
		if "탭" in e and "s7" in e and "fe" in e: print("YES!!!!!!!!!!!!"); print("형한테 연락하기!!!") # 원하는 제품 키워드를 통한 확인 절차

# PpomPpu 핫딜 게시판
url_ppom = "https://bbs.ruliweb.com/market/board/1020"
def ppom(url):
	webpage = requests.get(url)
	soup = BeautifulSoup(webpage.content, "html.parser")
	lst_ppom = [soup.select(".subject")[x].get_text() for x in range(35)] # 클래스를 이용하여 핫딜 게시판 물품 정보 긁어오기
	for e in lst_ppom:
		if "탭" in e and "s7" in e and "fe" in e: print("YES!!!!!!!!!!!!"); print("형한테 연락하기!!!") # 원하는 제품 키워드를 통한 확인 절차

# 실행
while True:
	url_fm = "https://www.fmkorea.com/hotdeal"
	url_ppom = "https://bbs.ruliweb.com/market/board/1020"
	fm(url_fm)
	ppom(url_ppom)
	
	time.sleep(1800) #30분 간격으로 update
