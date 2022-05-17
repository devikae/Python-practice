from bs4 import BeautifulSoup
import requests

movie_list = []
for j in range(40):
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20220516&page='+str(j+1)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    div = soup.select_one('.list_ranking')
    trs = div.find_all('tr')

    trs = div.find_all('tr')
    for i, v in enumerate(trs):
        if i > 1:
            # print(v)

            if v.find('a'):
                try:
                    no = v.select_one('td.ac:nth-child(1) > img').attrs['alt']
                except Exception as e:
                    no = v.select_one('td.order').text
                try:
                    title = v.select_one('td.title > div.tit5 > a').text
                except Exception as e:
                    title = 'none'
                img_url = v.find('a').attrs['href']
                score = v.select_one('td.point').text
                movie_list.append([no, title, img_url, score])

for i in movie_list:
    print(i)
# DB에서도 읽을수 있는 형식
import csv
with open('movie.csv', 'w', encoding='utf8') as f:
    write = csv.writer(f, delimiter='|', quotechar='"')
    for i in movie_list:
        write.writerow(i)

