import requests
from bs4 import BeautifulSoup

url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun="
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')
infected_count = soup.select("div.caseTable")
for i in infected_count:
	print("어제 하루 확진자 수는 : ", i.select_one("li > p.inner_value").text, sep = '')