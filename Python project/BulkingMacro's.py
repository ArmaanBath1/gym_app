import subprocess
from tkinter import *
import tkinter as tk
from PIL import ImageTk
root = Tk()

bg_colour = "#000000"
title = ""
ingredients = ["Bulking Macro's"]
def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)
    logo_img = ImageTk.PhotoImage(file="assets/bulkingmacropiechart.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack()

def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()
    logo_img = ImageTk.PhotoImage(file="assets/bulkingmacropiechart.png")
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)
    tk.Label(frame2, text=title, bg=bg_colour, fg="white", font=("Ubuntu", 20)).pack(pady=50, padx=50)
    for i in ingredients:
        tk.Label(frame2, text=i, bg="#000000", fg="white", font=("Shanti", 12)).pack(fill="both", padx=25)
  

def HIT():
    if(B) :
        root.destroy()
        subprocess.run(["python", "Supplements2.py"])
    
B = Button(root, text="Supplements", padx=10, pady=10, command= HIT, 
                               fg="#ffffff", bg="black") 
B.pack()

def BACK():
    if(B3) :
        root.destroy()
        subprocess.run(["python", "MuscleBuildingDiet.py"])
    
B3 = Button(root, text="Back", padx=10, pady=10, command= BACK, 
                               fg="#ffffff", bg="black") 
B3.pack()

root.title("Fitness coach")
#root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)

frame1.pack(fill="both", expand=True)
frame2.pack(fill="both", expand=True)

myLabel = Label(root, text="Prioritising Macro's for bulking:")
myLabel.pack()

myLabel2 = Label(root, text="For bulking we have to alter our macro intake to be more suitable. This means prioritising protein which is a building block for muscle development.")
myLabel2.pack()

myLabel4 = Label(root, text="Protein can be found in foods and supplements, best sources would be meat.")
myLabel4.pack()

myLabel7 = Label(root, text="In addition we can take protein powder to help increase our protein intake but shouldnt be be our main source of protein, remember to priotisie whole foods.")
myLabel7.pack()

load_frame2()

root.geometry("1920x1080")

root.mainloop()