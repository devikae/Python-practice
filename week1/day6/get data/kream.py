from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import os
from PIL import Image
import urllib.request

# 스크롤 다운
# 선택자 찾기 (대표 이미지, 아이디, 피드내용, 좋아요 수, 태그사진, 이름, 가격)
#


url = 'https://kream.co.kr/social/trending'
driver = webdriver.Chrome('../../../chromedriver')
# resp = requests.get(url)
# soup = BeautifulSoup(resp.text, 'html.parser')

driver.implicitly_wait(3)

driver.get(url)
num = 1

# TODO 통합파일만들기
try:
    os.mkdir("kream")
    print('kream 폴더 생성')
except Exception as e:
    print('폴더가 존재 합니다.')
    pass

try:
    cnt = 5
    pagedowns = 1
    body = driver.find_element_by_tag_name('body')
    while pagedowns < cnt:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        pagedowns += 1
except Exception as e:
    print(str(e))
soup = BeautifulSoup(driver.page_source,'html.parser')
cardBox = soup.select('.card_box')

for i in cardBox:
    print('=' * 200)
    user_name = i.select_one('p.user_name').text
    print('유저명:', user_name)
    try:
        content = i.select_one('p.text_box').text
        print('내용',content)
    except Exception as e:
        print('no have feed text')
    user_like = i.select_one('span.like_count').text
    print('좋아요:',user_like)

    # TODO 개별 폴더, 파일 만들기
    # path = 'kream/' + str(num) + '+' + str(i.select_one('p.user_name').text)
    path = 'kream/' + str(num) + '+' + str(i.select_one('p.user_name').text)
    os.mkdir(path)
    filePath = path + '/' + str(i.select_one('p.user_name').text)
    print('저장경로', filePath)
    f = open(filePath + '.txt', 'w')

    # TODO 개별파일 안에 텍스트로 작성
    f.write('유저명:')
    f.write(user_name + '\n')
    f.write('내용: ')
    f.write(content + '\n')
    f.write('좋아요: ')
    f.write(user_like + '\n')

    setitem = i.select('ul.product_list')

    f.write('\n\n 착용 아이템: \n')

    for z in setitem:
        try:
            itemList = z.select('p.product_name')
            itemPrice = z.select('.price_box > span.amount')
            print('++++++착용 아이템++++++')

            for j in range(len(itemList)):
                print(j+1, itemList[j].text, itemPrice[j].text+ '원')
                f.write(itemList[j].text + ': ')
                f.write(itemPrice[j].text + '원 \n')

        except Exception as e:
            pass

    f.close()

    img_url = i.select_one('div> img.social_img').attrs['src']
    print('img',img_url)
    print('=' * 200)

    print()

    num += 1
    urllib.request.urlretrieve(img_url, filePath+".jpeg")