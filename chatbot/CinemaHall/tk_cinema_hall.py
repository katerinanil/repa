from tkinter import *

root = Tk()
root.title(u'Cinema Hall')
#root.geometry('381x425')
root.geometry('750x425')
root.resizable(width=False, height=False)

seat_name = 1
row_name = 10

li = ["grey", "indigo"]
def color(event):
     event.widget.configure(bg=li[0])
     li[0],li[1] = li[1],li[0]
     #li[0] = li[1]
     #li[1] = li[0]

Button(root, text = "VIP 1 (500р)",  background="cyan3",
               foreground="white",).grid(row = 0, column = 1, columnspan = 3, ipadx = 10, padx = 3, pady = 5, sticky = E)
Button(root, text = "VIP 2 (500р)",  background="cyan3",
               foreground="white",).grid(row = 0, column = 5, columnspan = 3, ipadx = 15, padx = 3, pady = 5, sticky = W)
Button(root, text = "VIP 3 (500р)",  background="cyan3",
               foreground="white",).grid(row = 0, column = 8, columnspan = 3, ipadx = 10, padx = 3, pady = 5, sticky = W)


for x in range(1, 11):
    for z in range(1, 11):
        label1 = Label( root, text = "ряд "+str(row_name)).grid(row = x, column = 0)
        but2 = Button(root, text = str(seat_name) + " (250р)",  background="royalblue", foreground="white")
        but2.grid(row = x, column = z, ipadx = 4, ipady = 2, padx = 2, pady = 2)
        but2.bind("<Button-1>", color)
        label2 = Label( root, text = "ряд "+str(row_name)).grid(row = x, column = 12)
        seat_name += 1
        #bigseat_name += 1
        if seat_name == 11:
            seat_name = 1
    row_name -= 1

but = Button(root, text = "Э К Р А Н",  bg="indigo",
       foreground="white",)
but.grid(columnspan = 14, padx = 18, ipady = 5, pady = 15, sticky = W+E)
but.bind("<Button-1>", color)

root.mainloop()

"""import Tkinter
root = Tkinter.Tk(  )
for r in range(3):
   for c in range(4):
      Tkinter.Label(root, text='R%s/C%s'%(r,c),
         borderwidth=1 ).grid(row=r,column=c)
root.mainloop(  )"""
