import tkinter as tk
root=tk.Tk()
root.title("Button Demo")
root.geometry('300x200')
b1=tk.Button(root, text="Click me", bg='blue', command=root.destroy)
b1.pack()
root.mainloop()