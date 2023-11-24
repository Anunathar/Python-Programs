from tkinter import *
root=Tk()
root.title("Button Demo")
root.geometry('300x200')
b1=Button(root, text="Click me", bg='blue', command=root.destroy)
b1.pack()
root.mainloop()


import tkinter

root=tkinter.Tk()
root.title("Button Demo")
root.geometry('300x200')

b1=tkinter.Button(root, text="Click me", bg='blue', command=root.destroy)

b1.pack()

root.mainloop()