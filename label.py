from tkinter import *
top=Tk()
top.title("Color")
top.geometry("200x200")

l1=Label(top,text=" First Name", fg="black")
l1.place(x=10, y=10)

l2=Label(top,text="Last Name", fg="black", bg="orange")
l2.place(x=10, y=30)

l3=Label(top, text="Gender", bg="purple", padx=10, pady=5)
l3.place(x=10,y=50)

l4=Button(top,text="Click Me", command=top.destroy)
l4.place(x=30, y=90)

top.mainloop()