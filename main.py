import tkinter as tk
import downloader as d

def handle_download():
    saved_url = search_bar.get().strip()

    if saved_url:
        d.download_vid(saved_url)

window = tk.Tk()
window.geometry("800x600")
window.title("Video Downloader")

icon = tk.PhotoImage(file="ytvideodownloaderlogo.png")

window.iconphoto(True, icon)
window.config(background="#3a3d3b")

center_frame = tk.Frame(window, bg="#3a3d3b")
center_frame.place(relx=0.5, rely=0.6, anchor="center")

label = tk.Label(center_frame, text="Youtube Video Downloader", font=("Helvetica", 18), fg="white", bg="#3a3d3b")
label.pack(pady=(0, 20))

search_bar = tk.Entry(center_frame, font=("Arial", 14), width=50, bd=2, relief="groove")
search_bar.pack()

saved_url = ""

download_button = tk.Button(center_frame, text="Download", font=("Arial", 12), command=handle_download)
download_button.pack(pady=(10,0))

window.mainloop()

