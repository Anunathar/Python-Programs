from tkinter import *
top=Tk()
top.title("Patient")
top.geometry("600x400")

regno=Label(top,text="Regno:")
regno.grid(row = 0, column = 0 , pady=10, padx=5)
e1=Entry(top)
e1.grid(row=0, column=1)

name=Label(top,text="Name:")
name.grid(row = 1, column = 0 , pady=10, padx=5)
e2=Entry(top)
e2.grid(row=1, column=1)


mob=Label(top, text="Mobile:")
mob.grid(row=2, column = 0, pady=10, padx=5)
e3=Entry(top)
e3.grid(row=2, column=1)

gen=Label(top, text = "Gender:")
gen.grid(row=3, column=0, pady=10, padx=5)
e4=Entry(top)
e4.grid(row=3, column=1)

top.mainloop()