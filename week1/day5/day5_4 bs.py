import json
import requests
from bs4 import BeautifulSoup

url ='https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page=1&pageSize=20'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

jsonObj = json.loads(soup.text)
stocks = jsonObj['stocks']

stock_list = []
for stock in stocks:
    # print(stock)
    # print(stock['itemCode'], stock['stockName'], stock['closePrice'] )
    # print(stock['stockName'])
    # print(stock['closePrice'])
    stock_list.append([stock['itemCode'], stock['stockName'], stock['closePrice']])