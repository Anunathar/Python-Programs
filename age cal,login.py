from tkinter import *
from sqlite3 import * 

con = connect('project.db')
cur=con.cursor()
cur.execute('create table if not exists users(name text,email text ,username text, password text)')

def agecalculator():
    root=Tk()
    root.title("Age Calculator ")
    root.geometry('400x300')

    root.mainloop()

def login():

    def verify():
        u=txtusername.get()
        p=txtpassword.get()
        cur.execute('select * from users where username=? and password=?',(u,p))
        rs=cur.fetchall()
        if len(rs)==0:
            print("Invalid")
        else:
            agecalculator()
        
    root=Tk()
    root.title("Login Page ")
    root.geometry('400x300')
    lblusername = Label(root,text="Enter user name ")
    txtusername = Entry(root)

    lblpassword=Label(root, text="Enter password")
    txtpassword=Entry(root,show="*")

    btnLogin = Button(root,text="Login",command=verify)

    lblusername.grid(row=0,column=0)
    txtusername.grid(row=0,column=1)

    lblpassword.grid(row=1,column=0)
    txtpassword.grid(row=1,column=1)

    btnLogin.grid(row=2,column=1)

    root.mainloop()

def signup():

    def adddata():
        n=txtname.get()
        e=txtemail.get()
        un=txtusername.get()
        p=txtpassword.get()

        cur.execute('insert into users values(?,?,?,?)',(n,e,un,p))
        con.commit()
        print("Ok")

    root=Tk()
    root.title("Registration Page ")
    root.geometry('400x300')
    lblname = Label(root, text="Enter Name ")
    txtname = Entry(root)
    lblemail = Label(root,text="Enter Email Id ")
    txtemail = Entry(root)
    lblusername = Label(root,text="Enter user name ")
    txtusername = Entry(root)
    lblpassword=Label(root, text="Enter password")
    txtpassword=Entry(root,show="*")
    btnLogin = Button(root,text="Sign Up",command=adddata)
    lblname.grid(row=0,column=0)
    txtname.grid(row=0,column=1)
    lblemail.grid(row=1,column=0)
    txtemail.grid(row=1,column=1)

    lblusername.grid(row=2,column=0)
    txtusername.grid(row=2,column=1)
    lblpassword.grid(row=3,column=0)
    txtpassword.grid(row=3,column=1)

    btnLogin.grid(row=5,column=1)
    root.mainloop()

root=Tk()
root.title("Project Page ")
root.geometry('400x300')

btnLogin = Button(root,text="Login",command=login)
btnSignUp = Button(root,text="SignUp",command=signup)

btnLogin.grid(row=0,column=0)
btnSignUp.grid(row=0,column=1)
root.mainloop()