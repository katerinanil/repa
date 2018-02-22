from tkinter import *

root = Tk()
root.title(u'Cinema Hall')
#root.geometry('381x425')
root.geometry('745x425')
root.resizable(width=False, height=False)

seat_name = 1
row_name = 10

li = ["grey", "royalblue"]
def color(event):
     event.widget.configure(bg=li[0])
     li[0],li[1] = li[1],li[0]
     #li[0] = li[1]
     #li[1] = li[0]

Button(root, text = "Buy",  background="light sea green",
               foreground="white",).grid(row = 0, column = 6, columnspan = 2, ipadx = 10, padx = 3, pady = 5, sticky = E)
Button(root, text = "Book",  background="royalblue",
               foreground="white",).grid(row = 0, column = 7, columnspan = 2, ipadx = 10, padx = 3, pady = 5, sticky = E)
Button(root, text = "Мне повезет!",  background="coral",
               foreground="white",).grid(row = 0, column = 9, columnspan = 2, ipadx = 10, padx = 3, pady = 5, sticky = E)


for x in range(5, 15):
    for z in range(1, 11):
        label1 = Label( root, text = "ряд "+str(row_name)).grid(row = x, column = 0)
        but2 = Button(root, text = str(seat_name) + " (250р)",  background="royalblue", foreground="white")
        but2.grid(row = x, column = z, ipadx = 4, ipady = 2, padx = 2, pady = 2)
        but2.bind("<Button-1>", color)
        label2 = Label( root, text = "ряд "+str(row_name)).grid(row = x, column = 12)
        seat_name += 1
        if seat_name == 11:
            seat_name = 1
    row_name -= 1
    

class Example(Frame):
     def __init__(self, parent):
          Frame.__init__(self, parent)   
          self.parent = parent        
          self.initUI()
        
     def initUI(self):
          self.parent.title("Shapes")        
          self.pack(fill=BOTH, expand=1)
 
          canvas = Canvas(self)
          canvas.create_rectangle(305, 35, 405, 45, outline="blue", fill="red", width=2)
          canvas.pack(fill=BOTH, expand=1)

but = Button(root, text = "Э К Р А Н",  bg="indigo",
       foreground="white",)
but.grid(columnspan = 16, padx = 18, ipady = 5, pady = 15, sticky = W+E)
but.bind("<Button-1>", color)

root.mainloop()

"""import Tkinter
root = Tkinter.Tk(  )
for r in range(3):
   for c in range(4):
      Tkinter.Label(root, text='R%s/C%s'%(r,c),
         borderwidth=1 ).grid(row=r,column=c)
root.mainloop(  )"""
