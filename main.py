import tkinter
import customtkinter # type: ignore
from pytube import YouTube # type: ignore


def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except:
        print("Something wrong happened")
    print("Download Completed")

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# The frame of the app
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube downloader")

# Adding UI elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10,pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx = 10, pady=10)

# Running the app as a loop
app.mainloop()