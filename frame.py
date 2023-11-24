from tkinter import *
top=Tk()
top.title("Blank")
top.geometry("400x400")

f1=Frame(top, bg="yellow", width=100, height=100)
f1.pack()

f2=Frame(top, bg="purple", width=100, height=100)
f2.pack()

f3=Frame(top, bg="blue", width=100, height=100)
f3.pack()

f4=Button(f2, text="CLICK",command=top.destroy)
f4.place(x=30,y=40)

top.mainloop()