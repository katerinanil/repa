from tkinter import *

window = Tk()

def close_window(): 
    window.destroy()

frame = Frame(window)
frame.pack()
button = Button (frame, text = "Bye", command = close_window)
button.pack()

window.mainloop()
