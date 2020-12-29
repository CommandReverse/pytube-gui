import os
import tkinter as tk
import tkinter.font as tkfont
from tkinter.filedialog import askdirectory
from pytube import YouTube

basedir = os.path.dirname(os.path.realpath(__file__))


def get_video_url():
    item = url_entry.get()
    path = askdirectory(initialdir="/", title="Select Directory")
    YouTube(item).streams.first().download(output_path=path)


root = tk.Tk()
pic = tk.PhotoImage(file=os.path.join(basedir, "icon.png"))
root.iconphoto(False, pic)
root.title("YouTube Video Downloader")
root.geometry("400x400")
root.resizable(width=True, height=True)

cv = tk.Canvas(root, height=400, width=400, bg="#263d42")
cv.pack()

bold_font_1 = tkfont.Font(family="Helvetica", size=12, weight="bold")
label_1 = tk.Label(root, text="Enter the URL", width=12, bg="#263d42")
label_1.config(font=bold_font_1)
cv.create_window(200, 100, window=label_1)
url_entry = tk.Entry(root)
cv.create_window(200, 140, window=url_entry)

bold_font_2 = tkfont.Font(family="Helvetica", size=10, weight="bold")
label_2 = tk.Label(root, text="Video Downloaded", width=20, bg="#263d42")
label_2.config(font=bold_font_2)
cv.create_window(200, 300, window=label_2)

download = tk.Button(text="Download", padx=5, pady=5,
                     fg="white", bg="DeepSkyBlue",
                     command=get_video_url)
cv.create_window(200, 200, window=download)


root.mainloop()
