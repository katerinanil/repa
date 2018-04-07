from tkinter import *

#when click buy or book
#call callback with seats nums
def create_gui(seats, callback):
    #0=free, 1=busy|book, 2=selected 
    colors = ["royalblue", "grey", "light sea green"]
    selected_seats = []

    def process_seat_click(event):
        event.widget.configure(bg=colors[2])
        print(event.widget.seat_index)

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

    Button(root, text="Buy", background="light sea green",
        foreground="white",).grid(row=0,column=6,columnspan=2,ipadx=10,padx=3,pady=5,sticky=E)
    Button(root, text="Book", background="royalblue",
        foreground="white",).grid(row=0,column=7,columnspan=2,ipadx=10,padx=3,pady=5,sticky=E)
    Button(root, text="Мне повезет!", background="coral",
        foreground="white",).grid(row=0,column=9,columnspan=2,ipadx=10,padx=3,pady=5,sticky=E)

    for i in range(5, 15):
        label1 = Label(root, text = "ряд "+str(15 - i)).grid(row = i, column = 0)
        label2 = Label(root, text = "ряд "+str(15 - i)).grid(row = i, column = 12)
        for j in range(1, 11):
            index = 10 * (14 - i) + j - 1
            price =  str(seats[index].price)
            but2 = Button(root, text = str(j) + " (" + price + "р)",  background="royalblue", foreground="white")
            but2.grid(row = i, column = j, ipadx = 4, ipady = 2, padx = 2, pady = 2)
            but2.seat_index = index
            but2.bind("<Button-1>", process_seat_click)

    but = Button(root, text = "Э К Р А Н",  bg="indigo", foreground="white",)
    but.grid(columnspan = 16, padx = 18, ipady = 5, pady = 15, sticky = W+E)
    but.bind("<Button-1>", lambda x: print("Vot kto pridumal knopke ekran?"))

    root.mainloop()
