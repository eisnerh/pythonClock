from tkinter import *
import tkinter
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime("%H:%M:%S")
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("Helvetica", 100), background="black", foreground="white")

label.pack(anchor=CENTER)

time()

mainloop()
