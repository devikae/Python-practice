# url or url 정보 둘중 하나로 저장하는 app 생성

# 1. url 입력 + 수집 버튼 클릭시
# img 저장 경로 출력 + (저장 /data/image...)

# 2. 삭제버튼 클릭시 저장한 정보 삭제

from tkinter import *
import requests as req
from bs4 import BeautifulSoup
import os
import urllib.request
from urllib.request import urlopen

class myApp:

    def __init__(self, app):
        self.app = app
        self.app.title('수집')
        # self.app.geometry('640x400')
        self.app.resizable(False, False)
        self.input = Entry(self.app)
        self.textBox = Text(self.app, relief=SUNKEN)
        self.input.grid(row =0 , column=0)
        self.textBox.grid(row =1, columnspan=100)
        self.btn = Button(self.app, text='검색', command=self.fn_search).grid(row=0, column=1)
        self.btnDel = Button(self.app, text='삭제',command=self.fn_del).grid(row=0, column=2)
        self.btnSave = Button(self.app, text='저장',command=self.fn_save).grid(row=0, column=3)

    def fn_text(self,msg):
        #  Text위젯에 입력
        url = msg

        res = req.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.find_all('img')

        list = []

        for i in links:
            # print(i.attrs['src'])
            self.textBox.insert(INSERT, i.attrs['src']+'\n')
            list.append(i.attrs['src'])

        return list


    def fn_save(self):
        msg = self.input.get()
        os.mkdir("/home/pc52/PycharmProjects/pythonProject1/week1/day3/C/data")
        os.mkdir("/home/pc52/PycharmProjects/pythonProject1/week1/day3/C/data/imges")

        list = self.fn_text(msg)
        print(list)


        n=0
        for i in list:
            # imgUrl = list[i]
            # with urlopen(imgUrl) as f:
            #     with open('/home/pc52/PycharmProjects/pythonProject1/week1/day3/C/data/imges/img'+ str(i) + '.jpg') as h:  # 이미지 + 사진번호 + 확장자는 jpg
            #         h.write(img)  # 이미지 저장
            saveNm = 'img' + str(n) + ".png"
            urllib.request.urlretrieve(list[n], '/home/pc52/PycharmProjects/pythonProject1/week1/day3/C/data/imges/'+saveNm)
            n +=1



    def fn_search(self):
        # textBox에 entry 입력 값을 가져와 함수 호출
        msg = self.input.get()
        self.fn_text(msg)

    def fn_del(self):
        # textBox 전체 삭제
        self.textBox.delete('1.0', 'end')






app = Tk();
myApp = myApp(app)
app.mainloop()


