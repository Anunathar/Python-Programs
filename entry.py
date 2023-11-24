from tkinter import *
top=Tk()
top.title("Box")
top.geometry("300x200")

e1=Entry(top,bg="orange")
e1.place(x=100, y=50)

e2=Entry(top,fg="black")
e2.place(x=100, y=100)

e3=Entry(top,width=40, show="*")
e3.place(x=100, y=150)

top.mainloop()