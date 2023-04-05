from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
import time

# tip CTRL + Shift + C 
# get keyword
query = '코로나'

#access to url by chrome driver
url = 'https://www.google.com/'
driver = webdriver.Chrome('/Users/EHmin/Desktop/chromedriver') #/! where is chromedriver? I can't find it 
driver.get(url)
time.sleep(5)


search_box = driver.find_element(By.CLASS_NAME, "gLFyf")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(5)

#click news tab by using xPath
driver.find_element(By.XPATH,'//*[@id="hdtb-msb"]/div[1]/div/div[4]/a').click()
time.sleep(5)


video_links = driver.find_elements(By.CLASS_NAME,"VYkpsb")

j = 0

for link in video_links:
    src = link.get_attribute('data-url')
    if (src != None):
        urllib.request.urlretrieve(src, "video" + str(j) + ".mp4")
        j+= 1
        
        