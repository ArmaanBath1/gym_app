import subprocess
from tkinter import *
import tkinter as tk
from PIL import ImageTk
root = Tk()

bg_colour = "#000000"
title = ""
ingredients = ["Muscle Building Diet"]
def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)
    logo_img = ImageTk.PhotoImage(file="assets/jaycutlereating.jpg")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack()

def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()
    logo_img = ImageTk.PhotoImage(file="assets/jaycutlereating.jpg")
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)
    tk.Label(frame2, text=title, bg=bg_colour, fg="white", font=("Ubuntu", 20)).pack(pady=50, padx=50)
    for i in ingredients:
        tk.Label(frame2, text=i, bg="#000000", fg="white", font=("Shanti", 12)).pack(fill="both", padx=25)


def HIT():
    if(B) :
        root.destroy()
        subprocess.run(["python", "BulkingMacro's.py"])
    
B = Button(root, text="Macro's", padx=10, pady=10, command= HIT, 
                               fg="#ffffff", bg="black") 
B.pack()



def BACK():
    if(B3) :
        root.destroy()
        subprocess.run(["python", "MuscleBuildingGuide.py"])
    
B3 = Button(root, text="Back", padx=10, pady=10, command= BACK, 
                               fg="#ffffff", bg="black") 
B3.pack()

root.title("Fitness coach")
#root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)

frame1.pack(fill="both", expand=True)
frame2.pack(fill="both", expand=True)

root.geometry("100x100")
myLabel = Label(root, text="Calorie Surplus:")
myLabel.pack()

myLabel2 = Label(root, text="Calorie Surplus means; Calorie: A unit of energy which we use to measure food in comparison to weight. Surplus; an excess or left over.")
myLabel2.pack()

myLabel4 = Label(root, text="In order to build the most muscle possible quickly, we have to be in a calorie surplus, meaning we must be eating more calories then required leading to an increase in weight.")
myLabel4.pack()

myLabel6 = Label(root, text="A diet consists of 3 main macronutrients (Macro's); Water is considered sepperate but still essential.")
myLabel6.pack()

myLabel7 = Label(root, text="When we follow a muscle building diet, we call this a 'Bulk' or 'Bulking'.")
myLabel7.pack()

load_frame2()

root.geometry("1920x1080")

root.mainloop()