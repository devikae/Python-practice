from tkinter import *
from tkinter import messagebox as alert
def fn_click():
    name = txt.get()
    alert.showinfo('이름', name)

# 객체 생성
app = Tk()
lbl = Label(app, text='연락처')
lbl.pack()
txt = Entry(app)
txt.pack()
btn = Button(app, text='ok', command=fn_click())
btn.pack()
app.mainloop()