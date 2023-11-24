import tkinter 

window = tkinter.Tk()
window.title("My Registration Form ")
window.geometry('600x500')

label1=tkinter.Label(window,text="Enter your name ")
label1.pack(side="left")
label2=tkinter.Label(window,text="Enter your mobile number ")
label2.pack(side="left")
btn1=tkinter.Button(window,text="Ok")
btn1.pack(side="left")

window.mainloop()