from tkinter import *
top= Tk()
top.title("Student Registration Form")
top.geometry("800x400")

stu=Label(top,text="Student Information")
stu.grid(row=0,column=0, pady=10, padx=10)

name=Label(top,text="First Name:")
name.grid(row=1,column=0, pady=10, padx=5)
e1=Entry(top)
e1.grid(row=1, column=1)

name=Label(top,text="Middle Name:")
name.grid(row=1,column=2, pady=10, padx=5)
e2=Entry(top)
e2.grid(row=1, column=3)

name=Label(top,text="Last Name:")
name.grid(row=1,column=4, pady=10, padx=5)
e3=Entry(top)
e3.grid(row=1, column=5)

dob=Label(top,text="Date Of Birth:")
dob.grid(row=2,column=0, pady=10, padx=5)
e4=Entry(top)
e4.grid(row=2, column=1)

ms=Label(top,text="Marital Status:")
ms.grid(row=2, column=2, pady=10,padx=5)
e5=Entry(top)
e5.grid(row=2, column=3)

sid=Label(top,text="Student ID :")
sid.grid(row=2, column=4, pady=10,padx=5)
e6=Entry(top)
e6.grid(row=2, column=5)

mail=Label(top,text="Email:")
mail.grid(row=3, column=0, pady=10,padx=5)
e7=Entry(top)
e7.grid(row=3, column=1)

add1=Label(top,text="Street Address:")
add1.grid(row=5, column=0, pady=10,padx=5)
e8=Entry(top)
e8.grid(row=5, column=1)

city=Label(top,text="City:")
city.grid(row=6, column=0, pady=10,padx=5)
e9=Entry(top)
e9.grid(row=6, column=1)

state=Label(top,text="State/Provision:")
state.grid(row=6, column=2, pady=10,padx=5)
e10=Entry(top)
e10.grid(row=6, column=3)

c=Label(top,text="Country:")
c.grid(row=7, column=0, pady=10,padx=5)
e11=Entry(top)
e11.grid(row=7, column=1)

pin=Label(top,text="Pin Code:")
pin.grid(row=7, column=2, pady=10,padx=5)
e12=Entry(top)
e12.grid(row=7, column=3)

b1=Button(top,text="Submit", command=top.destroy)
b1.grid(row= 10, column=3)

top.mainloop()


