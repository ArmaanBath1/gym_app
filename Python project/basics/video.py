from tkinter import *

 
 
from pytube import YouTube
try:

    url = input("Enter the Youtube URL: ")

    yt = YouTube(url)

    print("Title:", yt.title)
    print("Views:", yt.views)

    yd = yt.streams.get_highest_resolution()

    yd.download()

    print("Download complete.")
except Exception as e:
    print("An error occured:", str(e))