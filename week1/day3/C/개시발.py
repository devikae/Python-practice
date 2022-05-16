from operator import length_hint
from tkinter import *
import requests as req
from bs4 import BeautifulSoup
import os
import urllib.request
from urllib.request import urlopen
import time

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

        n = 0
        print('-------------------------------------------------text 함수 배열에 담기 -------------------------------------------------')
        for i in links:
            # print(i.attrs['src'])
            self.textBox.insert(INSERT, i.attrs['src']+'\n')
            k=i.attrs['src']
            # print('k 파싱 확인', k)
            list.append(k)
            # print('i의 값은??' , i)
            print('list'+str(n)+' 시발 들어갔잖아: ',list[n])
            n += 1

        return list


    def fn_save(self):
        print('-------------------------------------------------save 함수-------------------------------------------------')
        msg = self.input.get()
        print('save- msg: ', msg)

        os.mkdir("D:\coding\PyThon_workSpace\day3 Que/data")
        print('폴더생성')
        
        time.sleep(2)

        os.mkdir("D:\coding\PyThon_workSpace\day3 Que/data/imges")
        print('폴더생성2')

        print('-------------------------------------------------text 배열 호출-------------------------------------------------')
        imgList = list()
        print(type(imgList))

        for i in self.fn_text(msg):
            # a = (self.fn_text[i])
            imgList.append(i)
            print('imgList::::      ', )

            # list.append(a)
            # print('app I value : ', list[i])

        print('-------------------------------------------------담겼는지 확인-------------------------------------------------')
        
        for i in imgList:
            print('list안에 담긴 값: ', i)

        n=0
        
        print('-------------------------------------------------for문 작업 호출-------------------------------------------------')
        for i in list:
            # imgUrl = list[i]
            # with urlopen(imgUrl) as f:
            #     with open('/home/pc52/PycharmProjects/pythonProject1/week1/day3/C/data/imges/img'+ str(i) + '.jpg') as h:  # 이미지 + 사진번호 + 확장자는 jpg
            #         h.write(img)  # 이미지 저장
            saveNm = 'img' + str(n) + ".png"
            print('저장명 saveNm: ', saveNm)
            url = i
            print('url i 확인: ', url)
            urllib.request.urlretrieve(url, 'D:\coding\PyThon_workSpace\day3 Que/data/imges/'+saveNm)
            n +=1

    def fn_search(self):
        # textBox에 entry 입력 값을 가져와 함수 호출
        msg = self.input.get()
        print('msg: ',msg)
        
        self.fn_text(msg)

    def fn_del(self):
        # textBox 전체 삭제
        self.textBox.delete('1.0', 'end')

# https://www.naver.com/




app = Tk();
myApp = myApp(app)
app.mainloop()
