from tkinter import *

def f1():
    n=e1.get()
    m1=int(e2.get())
    m2=int(e3.get())
    m3=int(e4.get())
   
    s1.set("Hello"+ n)
    i1.set("Total" + str((m1+m2+m3)))

top = Tk()
top.title("Bill")
top.geometry("500x400")

s1=StringVar(top)
i1=IntVar(top)

l1 = Label(top, text = "Dry fruits")
e1 = Entry(top)

l2 = Label(top, text = "Biscuit")
e2 = Entry(top)

l3 = Label(top, text = "Pepsi")
e3 = Entry(top)

l4 = Label(top, text = "Bread")
e4 = Entry(top)

b1 = Button(top, text = "Ckick", command=f1)

l8 = Label(top, textvariable = i1)

l1.grid(row=0, column=0)
e1.grid(row=0, column=1)

l2.grid(row=1, column=0)
e2.grid(row=1, column=1)

l3.grid(row=2, column=0)
e3.grid(row=2, column=1)

l4.grid(row=3, column=0)
e4.grid(row=3, column=1)

b1.grid(row=7, column=1)
l8.grid(row=7, column=1)

top.mainloop()


