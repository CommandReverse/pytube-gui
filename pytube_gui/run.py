import os
import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from pytube import YouTube

basedir = os.path.dirname(os.path.realpath(__file__))


class YtGui:
    HEIGHT = 800
    WIDTH = 800

    def __init__(self, master):
        ICON = tk.PhotoImage(file=os.path.join(basedir, "icon.png"))
        self.master = master
        master.title("YouTube Video Downloader")
        master.iconphoto(False, ICON)
        master.geometry("800x800")

        self.label_1 = tk.Label(self.master, text="Enter the URL")
        self.label_1.pack()
        self.url_entry = tk.Entry(self.master)
        self.url_entry.pack()
        self.label_2 = tk.Label(self.master, text="Enter file name")
        self.label_2.pack()
        self.file_name = tk.Entry(self.master)
        self.file_name.pack()
        self.download = tk.Button(text="Download",
                                  padx=5,
                                  pady=5,
                                  fg="white",
                                  bg="DeepSkyBlue",
                                  command=self.get_video_url)
        self.download.pack()

    def get_video_url(self):
        item = self.url_entry.get()
        fn = self.file_name.get()
        path = askdirectory(initialdir="/", title="Select Directory")
        if fn is not None or not fn == "":
            YouTube(item).streams.first().download(output_path=path,
                                                   filename=fn)
        else:
            YouTube(item).streams.first().download(output_path=path)
        messagebox.showinfo("Success", "Video Downloaded")


root = tk.Tk()
gui = YtGui(root)
root.mainloop()
