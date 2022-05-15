# 크롬드라이버 > 미니브라우저 
# 셀레니움 > 미니브라우저 조작을 위한 파이썬 lib

# python 으로 자동화 시킬 수 있는 영역 
# 1. 페이지이동
# 2. 키 입력
# 3. click
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# 페이지 이동 
# 크롬드라이버의 경로 같은 경로에 있어서 파일명 작성
driver = webdriver.Chrome('chromedriver.exe') 

# driver.get > 해당 페이지로 이동 , 웹페이지 주소 전체를 적어줘야함 https. 
# driver.get('https://naver.com')
driver.get('https://instagram.com')

# 자동화 시킬 때 중요함 4초간 코드를 잠깐 정지 
# 페이지 이동 시 로딩시간을 고려 해야한다. 
time.sleep(4)

# 로그인 구현하기. > 아이디와 비밀번호 입력 해야함 키 입력할 요소를 찾고 키 입력 

# 입력할 요소를 찾자
# ID 입력 : input tag > class="_2hvTZ pexuQ zyHYP" 
# id = driver.find_element(By.CLASS_NAME, ('_2hvTZ')[0])
id = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')
id.click()
id.send_keys('계정 명 ')

# PW 입력 : input tag > _2hvTZ pexuQ zyHYP id 와 중복이 되는 요소가 있으니 두번째 클래스명을 사용하거나 리스트 인덱싱
# pw = driver.find_element_by_class_name('_2hvTZ')[1]
pw = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
pw.send_keys('계정 비')


# find_element(by=By.CLASS_NAME, value=name)를 사용하세요.
