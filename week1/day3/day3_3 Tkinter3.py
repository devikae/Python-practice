from tkinter import *

class moveBall:
    def __init__(self, app):
        self.canvas = Canvas(app, width=600, height=600)
        self.canvas.pack()
        self.app = app
        self.canvas.create_oval(100, 150, 150, 200, fill='blue', tag='blueball')
        self.canvas.pack()

    def move_left(self, event):
        self.canvas.move('blueball', -50 ,0)
        self.canvas.after(20)
        self.canvas.update()

    def move_right(self, event):
        self.canvas.move('blueball', 50, 0)
        self.canvas.after(20)
        self.canvas.update()

    def move_up(self, event):
        self.canvas.move('blueball', 0, -50)
        self.canvas.after(20)
        self.canvas.update()

    def move_down(self, event):
        self.canvas.move('blueball', 0, 50)
        self.canvas.after(20)
        self.canvas.update()




# 인스턴스 만들어서 실행
app = Tk()
mov = moveBall(app)
mov.canvas.bind('<Left>', mov.move_left)
mov.canvas.bind('<Right>', mov.move_right)
mov.canvas.bind('<Up>', mov.move_up)
mov.canvas.bind('<Down>', mov.move_down)
mov.canvas.focus_set()
mov.canvas.pack()
app.mainloop()