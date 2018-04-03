import tkinter
from tkinter import *

"""
root = Tk()

def Hello(event):
    print("Hello world")

btn = Button(root,                  #родительское окно
             text="Click me plz",       #надпись на кнопке
             width=30,height=5,     #ширина и высота
             bg="white",fg="black") #цвет фона и надписи
btn.bind("<Button-1>", Hello)       #при нажатии ЛКМ на кнопку вызывается функция Hello
btn.pack()                          #расположить кнопку на главном окне
root.mainloop()


from tkinter import tk, Canvas, Frame, BOTH"""
 
class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
        self.parent.title("Shapes")        
        self.pack(fill=BOTH, expand=1)
 
        canvas = Canvas(self)

        x_st = 15
        y_st = 15
        w = 10
        s = 10
        c = 10

        for i in range(c):
            x_curr = x_st
            y_curr = y_st + i * (w + s)
            for j in range(c):
                canvas.create_rectangle(x_curr, y_curr,
                    x_curr + w, y_curr + w,
                    outline="#004d73", fill="#007fbd", width=2)
                x_curr += w + s
        
        canvas.pack(fill=BOTH, expand=1)
        
 
def main():
    root = Tk()
    ex = Example(root)
    root.geometry("330x220+300+300")
    root.mainloop()
 
if __name__ == '__main__':
    main()
    print(123)
    main()

    print(456)
