import json
import requests
from bs4 import BeautifulSoup




stock_list = []

# for i in range(36):
#     url = 'https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page=' + str(i + 1) + '&pageSize=20'
#     print(url)

for i in range(36):
    url = 'https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page=' + str(i+1) +'&pageSize=50'
    # url = 'https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page=' + {0} +'&pageSize=50'.format(i+1)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    jsonObj = json.loads(soup.text)
    stocks = jsonObj['stocks']

    for stock in stocks:
        stock_list.append([stock['itemCode'], stock['stockName'], stock['closePrice']])

for i, v in enumerate(stock_list):
    print(str(i+1), v)

import csv

with open('stock_list.csv', 'w', encoding='utf8') as f:
    write = csv.writer(f, delimiter='|', quotechar='"')
    for i in stock_list:
        write.writerow(i)