# -*- coding:utf8 -*-
# utf-8 로

from bs4 import BeautifulSoup


import requests

url = 'http://movie.naver.com/movie/sdb/rank/rmovie.naver'
resp = requests.get(url)
print("status: ", resp.status_code)
# 200 정상처리 선택값

soup = BeautifulSoup(resp.text, 'html.parser')
# print('resp.text', resp.text) #그냥 출력 했을 때와, 아래 bs를 이용한 출력이 다르다

# print('구분', "="*100)
# print(soup.prettify())      # 구조화 출력

div= soup.select_one('.list_ranking')

trs = div.find_all('tr')
#모든 tr가져오기
movie_list=[]
for i, v in enumerate(trs):
    if i > 1:
        # print(v)

        if v.find('a'):
            try:
                no = v.select_one('td.ac:nth-child(1) > img').attrs['alt']
            except Exception as e:
                no = 'na'
                # print(str(e))
            title = v.find('a').text
            img_url = v.find('a').attrs['href']
            upDown = v.select_one('td.ac:nth-child(3) > img').attrs['alt']
            score = v.select_one('td.range.ac').text
            movie_list.append([no, title, img_url, upDown, score])

for i in movie_list:
    print(i)

# csv 형식으로 저장하면 DB에서도 읽을 수 있음
# csv 형식은 가볍다
import csv

with open('movie.csv', 'w', encoding='utf-8') as f:
    write = csv.writer(f, delimiter='|', quotechar='"')
    # 파이프라인으로 구분, 텍스트 사이에 파이프라인이 들어오면 문자열로 묶겠다

    for i in movie_list:
        write.writerow(i)