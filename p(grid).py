from tkinter import * 
top = Tk()
top.title("Students")
top.geometry("300x200") 

name = Label(top,text = "First Name : ")
name.grid(row = 0, column = 0,pady=10,padx=5) 
e1 = Entry(top)
e1.grid(row = 0, column = 1)

name = Label(top,text = "Middle Name : ")
name.grid(row = 1, column = 0,pady=10,padx=5) 
e2 = Entry(top)
e2.grid(row = 1, column = 1)

name = Label(top,text = "Last Name : ")
name.grid(row = 2, column = 0,pady=10,padx=5) 
e3 = Entry(top)
e3.grid(row = 2, column = 1)

top.mainloop()




