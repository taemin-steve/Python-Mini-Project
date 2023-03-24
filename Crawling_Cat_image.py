#step1.프로젝트에 필요한 패키지 불러온다.
from bs4 import BeautifulSoup as bs
import requests
import cv2 as cv

url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B3%A0%EC%96%91%EC%9D%B4'
#url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+ query >> 위에 복잡하게 할것없이 이렇게 해도 충분함 형식지정 없이도 문자열끼리 덧셈 가능

#Request를 이용ㅎ서 HTML 가져오기 
response = requests.get(url)
html_text = response.text

#html 파싱
soup = bs(html_text, 'html.parser')
#bs4 패키지의 select 함수와 선택자 개념을 이용해서 뉴스기사 제목을 모두 가져온다.
images = soup.select('img._image._listImage')


for i in images:
    src = i.get('src')
    print(src)
        
    