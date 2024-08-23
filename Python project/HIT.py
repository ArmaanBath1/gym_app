import subprocess
from tkinter import *
import tkinter as tk
from PIL import ImageTk

bg_colour = "#808080"
title = ""
ingredients = ["High Intensity Training"]
def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)
    logo_img = ImageTk.PhotoImage(file="assets/tomplatz.jpg")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack()

def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()
    logo_img = ImageTk.PhotoImage(file="assets/tomplatz.jpg")
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack(pady=10)
    tk.Label(frame2, text=title, bg=bg_colour, fg="white", font=("Ubuntu", 20)).pack(pady=50, padx=50)
    for i in ingredients:
        tk.Label(frame2, text=i, bg="#28393a", fg="white", font=("Shanti", 12)).pack(fill="both", padx=25)

root = Tk()
root.geometry("1920x1080")

def BACK():
    if(B3) :
        root.destroy()
        subprocess.run(["python", ".py"])
    
B3 = Button(root, text="Back", padx=10, pady=10, command= BACK, 
                               fg="#ffffff", bg="black") 
B3.pack()

root.title("Fitness coach")
#root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)

frame1.pack(fill="both", expand=True)
frame2.pack(fill="both", expand=True)

myLabel1 = Label(root, text="High intensity training is key for muscle growth, we have to push our limits.")
myLabel1.pack()

myLabel2 = Label(root, text="There are 3 key components, Intensity, volume & frequency.")
myLabel2.pack()

myLabel3 = Label(root, text="Intensity means how hard you are pushing yourself as you should be training till failure in order to maximise growth.")
myLabel3.pack()

myLabel4 = Label(root, text="Volume means how many sets and reps per muscle group are you doing in your split? (training plan/schedule)")
myLabel4.pack()

myLabel5 = Label(root, text="Frequency means how often are you training your muscle groups in your split.")
myLabel5.pack()

myLabel6 = Label(root, text="In your split you should be targeting your muscle groups in between 1-3 times, a split is refered as in a weekly basis. This is frequency.")
myLabel6.pack()

myLabel7 = Label(root, text="You should be training upto 20 sets maximum per muscle group in your split. This is subjective though so you need to play around with working sets for yourself to decide what feels best.")
myLabel7.pack()

myLabel8 = Label(root, text="Within sets you should be aiming for a rep range between 6-12, this is the best rep range for hypertrophy (increase in muscle mass through resistance training). This is volume.")
myLabel8.pack()

myLabel9 = Label(root, text="Sets should be taken to failure, meaning that you only stop when you physically cannot, not mentally. You should be fighting for the last few reps of each set which is a sign of muscular failure which increases hypertrophy. This is Intensity.")
myLabel9.pack()

myLabel10 = Label(root, text="It is also important to remember that your reps should be full rang of motion (ROM), meaning that you are not cheating or half-arsing. The deeper the stretch/ROM of the rep the more hypertrophic it is.")
myLabel10.pack()

myLabel11 = Label(root, text="Make sure you are going slow on the eccentric/negative and exploding on the concentric/poitive.")
myLabel11.pack()

load_frame2()

root.mainloop()