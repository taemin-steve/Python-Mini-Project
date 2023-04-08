from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urllib.request import urlretrieve
import time
# get keyword
query = input('검색할 키워드를 입력하세요: ')

#access to url by chrome driver
url = 'https://www.naver.com/'
driver = webdriver.Chrome('/Users/EHmin/Desktop/chromedriver') #/! where is chromedriver? I can't find it >> 
driver.get(url)


#find search box, and put keyword 
search_box = driver.find_element(By.CSS_SELECTOR, "input#query")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)


#click news tab by using xPath
driver.find_element(By.XPATH,'//*[@id="lnb"]/div[1]/div/ul/li[2]').click()
# time.sleep(10)
## XPath is a language used for querying and selecting specific elements within an XML or HTML document

time.sleep(5) #/! If you move on to the next code without delay, there are often cases where find_elements runs before reading all of it.

images = driver.find_elements(By.CLASS_NAME,"_image._listImage")

j = 1 # numbering variable 

for i in range(10):
    print(i)
    link = images[i].get_attribute("src")
    urlretrieve(link, str(i)+".jpg")
    
        
