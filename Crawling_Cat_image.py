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
images = soup.select('img')

j = 1 # 넘버링을 위한 변수 

for i in range(10):
    src = images[i]['src'] #URL 받아오기 
    image_name  = "Cat" + str(j) + ".png" #저장파일 명을 안받아오면 그냥 txt 파일이므로 .png 추가
    j += 1 # 넘버링 증가 
    with open(image_name, "wb") as f :
        f.write(requests.get(src).content) # binary로 받아온다 
    
        
    
    