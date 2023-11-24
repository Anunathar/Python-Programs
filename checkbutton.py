from tkinter import *
top=Tk()
top.geometry("400x400")

b1=Checkbutton(top, text="Blue",fg="purple",bg="yellow",width=10,height=3) 
b1.pack()

b2=Checkbutton(top,text="BLACK", fg="red", activebackground="yellow")
b2.pack()

b3=Checkbutton(top,text="ORANGE", fg="black", padx=10, pady=5)
b3.pack()

top.mainloop()
