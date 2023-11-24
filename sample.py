
import tkinter as tk

master_window = tk.Tk()
master_window.geometry("400x300")
master_window.title("StringVar Example")

string_variable = tk.StringVar(master_window, "Hello Everyone!!")

label = tk.Label(master_window, textvariable=string_variable, height=150)
label.pack()

master_window.mainloop()


'''
from tkinter import *
top=Tk()
top.title("StringVar Example")
top.geometry("200x200")

x= Label(top, "Hello Everyone !!!" )

l1 = Label(top, textvariable=x)
l1.pack(top)

top.mainloop()
'''