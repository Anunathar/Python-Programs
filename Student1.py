from tkinter import *
import sqlite3 
con=sqlite3.connect('Student1.db')
cur=con.cursor()
cur.execute('create table if not exists student1(roll number number ,name text, marks number)')

def insertdata():
    roll = txtroll.get()
    name = txtname.get()
    marks = txtmarks.get()
    t1 = (roll,name,marks)
    cur.execute('insert into student1 values(?,?,?)',t1)
    con.commit()
    lbldata.config(text='Record inserted successfully')

def showdata():
    cur.execute('select * from student1')
    rs = cur.fetchall()
    x="\nRoll    Name      Marks \n"
    for record in rs:
        #x=x+"\n"+str(record[0]) +"  "+ record[1] +"  "+ record[2]
        x=x+"%10d%15s%15s\n"%(record[0],record[1],record[2])
    
    lbldata.config(text=x)

def deletedata():
    id=txtroll.get()
    cur.execute('delete from student1 where id=?',(id,))
    lbldata.config(text="Record deleted successfully")

root = Tk()
root.title("Student Management System")
root.geometry('600x400')
# Created widgets
lblroll = Label(root,text="Roll number ")
txtroll = Entry(root)
lblname = Label(root, text="Enter the student Name ")
txtname = Entry(root)
lblmarks = Label(root,text="Enter the Student Marks")
txtmarks= Entry(root)
btninsert = Button(root,text="Insert",command=insertdata)
btnshow = Button(root,text="Show all records", command=showdata)
lbldata = Label(root)
btndelete = Button(root,text="Delete",command=deletedata)

lblroll.grid(row=0,column=0)
txtroll.grid(row=0,column=1)
lblname.grid(row=1,column=0)
txtname.grid(row=1,column=1)
lblmarks.grid(row=2,column=0)
txtmarks.grid(row=2,column=1)
btninsert.grid(row=3,column=1)
btnshow.grid(row=3,column=3)
btndelete.grid(row=3,column=2)
lbldata.grid(row=4,column=1)

root.mainloop()