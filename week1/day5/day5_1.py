# 크롬 드라이버 설치 ->  셀리니엄 설치 ( pip install selenium ) ->
import time
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'http://tour.interpark.com/'
driver = webdriver.Chrome('../../chromedriver') # 드라이버 객체화
# 웹 자원 로드를 위해 3초 기다리기
driver.implicitly_wait(3)
driver.get(url)
# time.sleep(10)

driver.find_element_by_id('SearchGNBText').send_keys('하와이')
driver.find_element_by_css_selector('button.search-btn').click()
time.sleep(1)

soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup.prettify())
lis = soup.select('.searchAllBox.overseaTravel.col1 li')
for li in lis:
    print(li)
lis = driver.find_elements_by_css_selector('ul.boxList li.boxItem')
for li in lis:
    print(li.get_attribute('innerHTML'))
    print(li.find_element_by_css_selector('h5.infoTitle').text)
    print(li.find_element_by_css_selector('strong').text)

driver.stop_client()
driver.close()