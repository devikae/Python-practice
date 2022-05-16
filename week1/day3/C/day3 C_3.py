# pip install bs4

import requests as req
from bs4 import BeautifulSoup

url = 'http://finance.naver.com/marketindex'
res = req.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
# 파싱을 해서 가져오게 되면 객체

# a 태그
# links = soup.find('a')
# for i in links:
#   print(i.attr['href'])

links = soup.find_all('img')
for i in links:
    print(i.attrs['src'])