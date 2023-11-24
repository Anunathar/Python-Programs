from tkinter import * 

def f1():
    n=t1.get()
    m1=int(t2.get())
    m2=int(t3.get())
    s1.set("Hello"+ n)       #
    i1.set("Your Total are " + str((m1+m2)))

root = Tk()
root.title("StringVar Demo")
root.geometry('600x400')

s1=StringVar(root)
i1=IntVar(root)

l1 = Label(root, text="Name : ")
t1 = Entry(root)

l2 = Label(root, text="Marks 1: ")
t2 = Entry(root)

l3 = Label(root, text="Marks 2: ")
t3 = Entry(root)

b1 = Button(root,text="Click Here",command=f1)


l4 = Label(root,textvariable=i1)

l1.grid(row=0,column=0)
t1.grid(row=0,column=1)

l2.grid(row=1,column=0)
t2.grid(row=1,column=1)

l3.grid(row=2,column=0)
t3.grid(row=2,column=1)

b1.grid(row=3,column=1)
l4.grid(row=4,column=1)


root.mainloop()