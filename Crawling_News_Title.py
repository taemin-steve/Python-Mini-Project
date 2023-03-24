#step1.프로젝트에 필요한 패키지 불러온다.
from bs4 import BeautifulSoup as bs
import requests

query = input('검색할 키워드를 입력하세요: ')
# 네이버 뉴스 페이지 URL에, 입력받은 단어를 더해 url을 지정
url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+'%s'%query
#url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+ query >> 위에 복잡하게 할것없이 이렇게 해도 충분함 형식지정 없이도 문자열끼리 덧셈 가능

#Request를 이용ㅎ서 HTML 가져오기 
response = requests.get(url)
html_text=response.text

#html 파싱
soup = bs(html_text, 'html.parser')

#bs4 패키지의 select 함수와 선택자 개념을 이용해서 뉴스기사 제목을 모두 가져온다.
titles = soup.select('a.news_tit')

for i in titles:
    title = i.get_text()
    print(title)