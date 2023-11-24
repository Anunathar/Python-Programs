from tkinter import *
top=Tk()
top.title("Book")
top.geometry("400x300")

name=Label(top,text="Book Name:")
name.place(x=30, y=50)
e1=Entry(top)
e1.place(x=110,y=50)

name=Label(top,text="Author Name:")
name.place(x=30, y =100)
e2=Entry(top)
e2.place(x=110, y =100)

b1=Button(top,text="Ok")
b1.place(x=160, y=150)
top.mainloop()
