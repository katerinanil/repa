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

        x1 = 15
        x2 = 25
        
        while x1 < 300 and x2 < 300:
            canvas.create_rectangle(x1, 15, x2, 25, 
            outline="blue", fill="blue", width=2)
            x1 += 20
            x2 += 20

        x1 = 15
        x2 = 25
        
        while x1 < 300 and x2 < 300:
            canvas.create_rectangle(x1, 35, x2, 45, 
            outline="blue", fill="blue", width=2)
            x1 += 20
            x2 += 20


        x1 = 15
        x2 = 25
        
        while x1 < 300 and x2 < 300:
            canvas.create_rectangle(x1, 55, x2, 65, 
            outline="blue", fill="blue", width=2)
            x1 += 20
            x2 += 20


        x1 = 15
        x2 = 25
        
        while x1 < 300 and x2 < 300:
            canvas.create_rectangle(x1, 75, x2, 85, 
            outline="blue", fill="blue", width=2)
            x1 += 20
            x2 += 20

        x1 = 20
        x2 = 30
        
        while x1 < 295 and x2 < 290:
            canvas.create_rectangle(x1, 95, x2, 105, 
            outline="blue", fill="blue", width=2)
            x1 += 20
            x2 += 20

        canvas.create_rectangle(15, 120, 285, 130, 
            outline="blue", fill="blue", width=2)

        #root = Tk()
        #Button(root, text = "qwerty",  background="blue",foreground="white",).grid(row = 10, column = 10, rowspan = 50, sticky = S+W+E)
        canvas.pack(fill=BOTH, expand=1)
        
 
def main():
    root = Tk()
    ex = Example(root)
    root.geometry("330x220+300+300")
    root.mainloop()  
 
if __name__ == '__main__':
    main()
