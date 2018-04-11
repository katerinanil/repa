from tkinter import *
from tkinter import messagebox
from db import Seat

#when click buy or book
#call callback with seats nums
def create_gui(seats, callback):
    #0=free, 1=busy|book, 2=selected 
    colors = ['royalblue', 'grey', 'light sea green']
    selected_seats = []

    def process_seat_click(event):
        color = event.widget.cget('bg')
        if color == colors[0]:
            event.widget.configure(bg=colors[2])
            selected_seats.append(event.widget.seat_index)
        elif color == colors[2]:
            event.widget.configure(bg=colors[0])
            selected_seats.remove(event.widget.seat_index)

    def process_order_click(event):
        if len(selected_seats) != 0:
            callback(selected_seats, event.widget.is_book)
            root.destroy()
        else: messagebox.showwarning('Упс..', 'Не выбраны места')

    root = Tk()
    root.title('CHAPLIN')
    root.geometry('745x525')
    root.resizable(width=False, height=False)
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='c2.png'))
    frame = Frame(bg='black')

    chap1 = PhotoImage(file="ico.png")
    Label(root, image=chap1).grid(row=0, column=0, columnspan=4)
    chap2 = PhotoImage(file="ico.png")
    Label(root, image=chap2).grid(row=0, column=2, columnspan=4)
    chap3 = PhotoImage(file="ico.png")
    Label(root, image=chap3).grid(row=0, column=4, columnspan=4)

    buttonBuy = Button(root, text="Buy", background=colors[2], foreground="white")
    buttonBuy.grid(row=0,column=6,columnspan=2,ipadx=10,padx=3,pady=5,sticky=E)
    buttonBuy.is_book = False
    buttonBuy.bind("<ButtonRelease-1>", process_order_click)
    buttonBook = Button(root, text="Book", background=colors[0], foreground="white")
    buttonBook.grid(row=0,column=7,columnspan=2,ipadx=10,padx=3,pady=5,sticky=E)
    buttonBook.is_book = True
    buttonBook.bind("<ButtonRelease-1>", process_order_click)
    Button(root, text="Мне повезет!", background="coral",
        foreground="white").grid(row=0,column=9,columnspan=2,ipadx=10,padx=3,pady=5,sticky=E)

    for i in range(5, 15):
        label1 = Label(root, text = "ряд "+str(15 - i)).grid(row = i, column = 0)
        label2 = Label(root, text = "ряд "+str(15 - i)).grid(row = i, column = 12)
        for j in range(1, 11):
            index = 10 * (14 - i) + j - 1
            price = str(seats[index].price)
            color = colors[0] if seats[index].state == Seat.FREE else colors[1]
            but2 = Button(root, text = str(j) + " (" + price + "р)",  background=color, foreground="white")
            but2.grid(row = i, column = j, ipadx = 4, ipady = 2, padx = 2, pady = 2)
            but2.seat_index = index
            but2.bind("<Button-1>", process_seat_click)

    but = Button(root, text = "Э К Р А Н",  bg="indigo", foreground="white",)
    but.grid(columnspan = 16, padx = 18, ipady = 5, pady = 15, sticky = W+E)
    but.bind("<Button-1>", lambda e: None)

    root.mainloop()
