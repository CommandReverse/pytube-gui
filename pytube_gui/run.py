import os
import tkinter as tk
import tkinter.font as tkfont
from pytube import YouTube

basedir = os.path.dirname(os.path.realpath(__file__))

root = tk.Tk()
pic = tk.PhotoImage(file=os.path.join(basedir, "icon.png"))
root.iconphoto(False, pic)
root.title("YouTube Video Downloader")
root.geometry("400x400")
root.resizable(width=True, height=True)

cv = tk.Canvas(root, height=400, width=400, bg="#263d42")
cv.pack()

bold_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
label = tk.Label(root, text="Enter the URL", width=12, bg="#263d42")
label.config(font=bold_font)
cv.create_window(200, 100, window=label)
url_entry = tk.Entry(root)
cv.create_window(200, 140, window=url_entry)


def get_video_url():
    item = url_entry.get()
    path = os.chdir('Enter the path where you want to save your file')
    YouTube(item).streams.first().download(output_path=path)


root.mainloop()
