# if side is given

from tkinter import *
top=Tk()
top.title("Blank")
top.geometry("400x200")
b1=Button(top,text="TOP")
b1.pack(side="top")
b2=Button(top,text="LEFT")
b2.pack(side="left")
b3=Button(top,text="RIGHT")
b3.pack(side="right")
b4=Button(top,text="BOTTOM")
b4.pack(side="bottom")
top.mainloop()




#if side is not given

from tkinter import *
top=Tk()
top.title("Blank")
top.geometry("400x200")
b1=Button(top,text="TOP")
b1.pack()
b2=Button(top,text="LEFT")
b2.pack()
b3=Button(top,text="RIGHT")
b3.pack()
b4=Button(top,text="BOTTOM")
b4.pack()
top.mainloop()
