from tkinter import *
import subprocess
from tkinter import messagebox
root = Tk()

message_text = StringVar()
message_text.set("What is your goal?")

message_label = Label(root, textvariable=message_text, wraplength=250)
message_label.pack()



def FatLossGuide():
    if(my_button) :
        print("Killing first.")
        root.destroy()
        subprocess.run(["python", "FatLossGuide.py"])
    
my_button = Button(root, text="Fat loss",command= FatLossGuide)
my_button.pack()


def MuscleBuildingGuide():
    if(my_button2) :
        print("Killing first.")
        root.destroy()
        subprocess.run(["python", "MuscleBuildingGuide.py"])

my_button2 = Button(root, text="Muscle building",command= MuscleBuildingGuide)
my_button2.pack()

root.geometry("1920x1080")

root.mainloop()