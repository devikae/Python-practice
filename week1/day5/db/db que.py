import json
import requests
from bs4 import BeautifulSoup

import sqlite3
conn = sqlite3.connect('stock.db')

cur = conn.cursor()


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


sql = """
    INSERT INTO stocks VALUES(?, ?, ?);
"""
cur.executemany(sql, stock_list)

conn.commit()
cur.close()
conn.close()