import urllib.request

url = 'https://kr.hypebeast.com/files/2022/02/nike-dunk-low-nike-sun-club-early-look-01.jpg'

saveNm = 'sun club dunk.jpg'
urllib.request.urlretrieve(url, saveNm)
print('저장 완료')

