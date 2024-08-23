from tkinter import *
from tkinter import messagebox
import subprocess
       
       
def Ok():
     uname = e1.get()
     password = e2.get()
       
     if(uname == "" and password == "") :
           messagebox.showinfo("", "Blank Not allowed")
       
       
     elif(uname == "Admin" and password == "123"):        
           messagebox.showinfo("","Login Success")
           root.destroy()
           subprocess.run(["python", "ProjectMenu.py"])
       
     else :
           messagebox.showinfo("","Incorrent Username and Password")
root = Tk()
root.title("Login")
root.geometry("1920x1080")
global e1
global e2
       
Label(root, text="UserName").place(x=600, y=410)
Label(root, text="Password").place(x=600, y=440)
       
e1 = Entry(root)
e1.place(x=700, y=410)
       
e2 = Entry(root)
e2.place(x=700, y=450)
e2.config(show="*")
       
       
Button(root, text="Login", command=Ok ,height = 3, width = 13).place(x=650, y=500)
       
root.mainloop()