import requests
from bs4 import BeautifulSoup

url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun="
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')
div = soup.select_one('div.caseTable')
infected_count = div.select('li>p.inner_value')

print("전날 총 확진자수는 : ", infected_count[0].text, sep='')
print("전날 국내 총 확진자수는 : ", infected_count[1].text, sep='', end = '  +  ')
print("전날 해외유입 총 확진자수는 : ", infected_count[2].text, sep='')