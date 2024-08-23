from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="I Clicked a button")
    myLabel.pack()

myButton = Button(root, text="Click me", padx=10, pady=10, command=myClick,
                  fg="#FFFFFF", bg="blue")

myButton.pack()
root.mainloop()