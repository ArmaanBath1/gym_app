import subprocess
from tkinter import *
import tkinter as tk
from PIL import ImageTk
root = Tk()

bg_colour = "#000000"
title = ''
ingredients = ["How to Lose Fat"]

def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)
    logo_img = ImageTk.PhotoImage(file="assets/jeffseidbulkvscut.jpg")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack()

def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()
    logo_img = ImageTk.PhotoImage(file="assets/jeffseidbulkvscut.jpg")
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)
    tk.Label(frame2, text=title, bg=bg_colour, fg="white", font=("Ubuntu", 20)).pack(pady=50, padx=50)
    for i in ingredients:
        tk.Label(frame2, text=i, bg="#000000", fg="white", font=("Shanti", 12)).pack(fill="both", padx=25)


def FLD():
    if(B2) :
        root.destroy()
        subprocess.run(["python", "FatLossDiet.py"])
    
B2 = Button(root, text="Planning your Cut", padx=10, pady=10, command= FLD, 
                               fg="#ffffff", bg="black") 
B2.pack()

def BACK():
    if(B3) :
        root.destroy()
        subprocess.run(["python", "ProjectMenu.py"])
    
B3 = Button(root, text="Back", padx=10, pady=10, command= BACK, 
                               fg="#ffffff", bg="black") 
B3.pack()

root.title("Fitness coach")
#root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)

frame1.pack(fill="both", expand=YES)
frame2.pack(fill="both", expand=YES)

root.geometry("50x50")
myLabel = Label(root, text="Basics:")
myLabel.pack()

myLabel2 = Label(root, text="Fat loss can not be targeted, when you lose fat it peels away like layers.")
myLabel2.pack()

myLabel3 = Label(root, text=" We divide Fat loss into 2 seperate requirements; Cardio & Diet")
myLabel3.pack()

myLabel4 = Label(root, text="Any form of cardio works, running, biking, etc. Some are more efficient then others but it is also largely dependant on your effort.")
myLabel4.pack()

myLabel5 = Label(root, text="When we follow a fat loss diet, we call this a 'Cut' or 'Cutting'.")
myLabel5.pack()

load_frame2()

root.geometry("1920x1080")

root.mainloop()