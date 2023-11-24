from tkinter import *
top=Tk()
top.title("RadioButtons")
top.geometry("300x200")
radio= IntVar()

rb1 = Radiobutton(top, text="Blue", bg="blue", variable=radio, value="1")
rb2 = Radiobutton(top, text="Orange", bg="orange", variable=radio, value="2")
rb3 = Radiobutton(top, text="Purple", bg ="purple",variable=radio, value="3")
rb4 = Radiobutton(top, text="Yellow", bg="yellow",variable=radio, value="4")
bt1 = Button(top,text="Click")

rb1.pack()
rb2.pack()
rb3.pack()
rb4.pack()
bt1.pack()

top.mainloop()
