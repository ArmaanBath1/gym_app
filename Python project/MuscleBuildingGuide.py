import subprocess
from tkinter import *
import tkinter as tk
from PIL import ImageTk
root = Tk()

bg_colour = "#000000"
title = ""
ingredients = ["How to Build Muscle"]
def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)
    logo_img = ImageTk.PhotoImage(file="assets/davidlaid.jpg")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack()

def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()
    logo_img = ImageTk.PhotoImage(file="assets/davidlaid.jpg")
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)
    tk.Label(frame2, text=title, bg=bg_colour, fg="white", font=("Ubuntu", 20)).pack(pady=50, padx=50)
    for i in ingredients:
        tk.Label(frame2, text=i, bg="#000000", fg="white", font=("Shanti", 12)).pack(fill="both", padx=25)


def HIT():
    if(B) :
        root.destroy()
        subprocess.run(["python", "HIT.py"])
    
B = Button(root, text="High Intensity Training", padx=10, pady=10, command= HIT, 
                               fg="#ffffff", bg="black") 
B.pack()

def MBD():
    if(B2) :
        root.destroy()
        subprocess.run(["python", "MuscleBuildingDiet.py"])
    
B2 = Button(root, text="Dieting to Gain Muscle", padx=10, pady=10, command= MBD, 
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

frame1 = tk.Frame(root, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)

frame1.pack(fill="both", expand=True)
frame2.pack(fill="both", expand=True)

root.geometry("250x250")
myLabel = Label(root, text="Basics:")
myLabel.pack()

myLabel2 = Label(root, text="Building muscle requires working out with heavy loads for duration very often")
myLabel2.pack()

myLabel3 = Label(root, text="We call this High Intenstity Training (HIT)")
myLabel3.pack()

myLabel4 = Label(root, text="You must seperate muscle building into 2 seperate requirements, training & diet")
myLabel4.pack()

myLabel5 = Label(root, text="Also we divide trianing into 3 seperate factors; Intensity, Volume, Frequency.")
myLabel5.pack()

myLabel6 = Label(root, text="Your diet and training work togther so you must make sure your also maintaining your specific dietary requirements.")
myLabel6.pack()

load_frame2()

root.geometry("1920x1080")

root.mainloop()