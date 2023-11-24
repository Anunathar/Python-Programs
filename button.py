from tkinter import *
from tkinter import messagebox
top=Tk()
top.geometry("400x400")

def fun(): 
    messagebox.showinfo("Hello", "Blue Button clicked")

b1=Button(top,text="BLUE", bg="black", fg="blue", width= 5, height=5)
b1.pack()

b2=Button(top,text="BLACK", bg="green", fg="red",activebackground="yellow")
b2.pack()

b3=Button(top,text="ORANGE", bg= "red", fg="white", padx=10, pady=5, command=fun)
b3.pack()

top.mainloop()

