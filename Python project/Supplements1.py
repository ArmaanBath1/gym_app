import subprocess
from tkinter import *
import tkinter as tk
from PIL import ImageTk
root = Tk()

bg_colour = "#000000"
title = ""
ingredients = ["Supplements"]
def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)
    logo_img = ImageTk.PhotoImage(file="assets/supplements.jpg")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack()

def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()
    logo_img = ImageTk.PhotoImage(file="assets/supplements.jpg")
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)
    tk.Label(frame2, text=title, bg=bg_colour, fg="white", font=("Ubuntu", 20)).pack(pady=50, padx=50)
    for i in ingredients:
        tk.Label(frame2, text=i, bg="#000000", fg="white", font=("Shanti", 12)).pack(fill="both", padx=25)

def BACK1():
    if(B2) :
        root.destroy()
        subprocess.run(["python", "CuttingMacro's.py"])
    
B2 = Button(root, text="Back", padx=10, pady=10, command= BACK1, 
                               fg="#ffffff", bg="black") 
B2.pack()

root.title("Fitness coach")
#root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)

frame1.pack(fill="both", expand=True)
frame2.pack(fill="both", expand=True)

root.geometry("100x100")
myLabel = Label(root, text="Supplements:")
myLabel.pack()

myLabel2 = Label(root, text="Supplements are very useful for bodybuilders, they are additional to help maximise your efficiency.")
myLabel2.pack()

myLabel4 = Label(root, text="Common supplements are protein powder, pre-workout, creatine, BCAA/amino acids.")
myLabel4.pack()

myLabel6 = Label(root, text="Supplements are not mandatory but are definetely very useful.")
myLabel6.pack()

myLabel7 = Label(root, text="Protein powder is a taken to help reach your protein intake because some people may not have eaten enough throughout the day.")
myLabel7.pack()

myLabel8 = Label(root, text="Pre-workout is taken to spike energy levels quickly with high amounts of caffeine, this is useful for if you want to feel awake or need energy to workout.")
myLabel8.pack()

myLabel9 = Label(root, text="Creatine is a natural chemical found in the body and in some foods but only a very small amount, it is taken to increase creatine in the muscles which will hold even more water in them as muscles are made of a lot of water, increasing strength and energy")
myLabel9.pack()

myLabel10 = Label(root, text="Though creatine can take a toll on the body especially for begginers, but it is totally normal as you will adjust within a couple weeks and reap the benefits quickly too.")
myLabel10.pack()

myLabel11 = Label(root, text="Sidenote: Taking creatine supplements require you to incease your water intake greatly, the more the better!")
myLabel11.pack()

myLabel12 = Label(root, text="BCAA (Branched-chain amino acids)/Amino acids are molecules that form protein, it increases recovery and is overall usefull as it is a form of protein.")
myLabel12.pack()

load_frame2()

root.geometry("1920x1080")

root.mainloop()