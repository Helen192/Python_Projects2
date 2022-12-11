from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Digital CLock")
def clock():
    string = strftime('%I:%M:%S:%p')
    label.config(text = string)
    label.after(1000,clock)


label = Label(root, font=("Digital-7", 100), background='black', foreground='green')
label.pack(anchor="center")
clock()

root.mainloop()