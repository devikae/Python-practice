from tkinter import *

app = Tk()

def donoting():
    print('DO NOTING')
    filewin = Toplevel(app)
    fileclose = Button(filewin, text='DO noting button')
    fileclose.config(command=app.quit)
    fileclose.pack()

def fn_edit():
    print('수정')

def fn_saving():
    print('저장')

def fn_close():
    app.quit()

menubar = Menu(app)
filemenu = Menu(menubar, tearoff=0)
editmenu = Menu(menubar, tearoff=0)

filemenu.add_command(label='OPEN', command=donoting)
filemenu.add_command(label='SAVE', command=fn_saving)
filemenu.add_command(label='CLOSE', command=fn_close)
filemenu.add_command(label='EDIT', command=fn_edit)


editmenu.add_command(label='DELETE')
filemenu.add_command(label='EXIT', command=fn_close)

menubar.add_cascade(label='File', menu=filemenu)

app.config(menu=menubar)
app.mainloop()