from tkinter import *

root = Tk()
root.title(u'CHAPLIN')
root.geometry('745x525')
root.resizable(width=False, height=False)
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='c2.png'))
frame = Frame(bg = 'black')

chap1 = PhotoImage(file="ico.png")
Label(root, image = chap1).grid(row=0, column=0, columnspan = 4)
chap2 = PhotoImage(file="ico.png")
Label(root, image = chap2).grid(row=0, column=2, columnspan = 4)
chap3 = PhotoImage(file="ico.png")
Label(root, image = chap3).grid(row=0, column=4, columnspan = 4)

li = ["grey", "royalblue"]
def color(event):
     event.widget.configure(bg=li[0])
     li[0], li[1] = li[1], li[0]

Button(root, text = "Buy",  background="light sea green",
               foreground="white",).grid(row = 0, column = 6, columnspan = 2, ipadx = 10, padx = 3, pady = 5, sticky = E)
Button(root, text = "Book",  background="royalblue",
               foreground="white",).grid(row = 0, column = 7, columnspan = 2, ipadx = 10, padx = 3, pady = 5, sticky = E)
Button(root, text = "Мне повезет!",  background="coral",
               foreground="white",).grid(row = 0, column = 9, columnspan = 2, ipadx = 10, padx = 3, pady = 5, sticky = E)

row_name = 10
for x in range(5, 15):
    label1 = Label(root, text = "ряд "+str(row_name)).grid(row = x, column = 0)
    label2 = Label(root, text = "ряд "+str(row_name)).grid(row = x, column = 12)
    seat_name = 1
    for z in range(1, 11):
        but2 = Button(root, text = str(seat_name) + " (250р)",  background="royalblue", foreground="white")
        but2.grid(row = x, column = z, ipadx = 4, ipady = 2, padx = 2, pady = 2)
        but2.bind("<Button-1>", color)
        seat_name += 1
    row_name -= 1

but = Button(root, text = "Э К Р А Н",  bg="indigo", foreground="white",)
but.grid(columnspan = 16, padx = 18, ipady = 5, pady = 15, sticky = W+E)
but.bind("<Button-1>", color)

root.mainloop()
