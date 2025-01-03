from yt_dlp import YoutubeDL
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Function to download the video
def download_video():
    url = url_entry.get()
    SAVE_PATH = filedialog.askdirectory(title="Select Save Location")
    
    if not url or not SAVE_PATH:
        messagebox.showerror("Error", "Please provide a valid URL and save location!")
        return
    
    # Options for downloading
    ydl_opts = {
        'outtmpl': f"{SAVE_PATH}/%(title)s.%(ext)s",
        'format': 'best',  # Single best stream (no merging required, avoiding merging audio and video streams)
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded successfully!")
        # Show a popup message
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")
        # Show a popup message
        messagebox.showerror(("Error", f"An error occurred: {e}"))
        
        
# Create the main application window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Label for instructions
label = tk.Label(root, text="Enter YouTube Video URL:")
label.pack(pady=5)

# INput field for the URL
url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=5, padx=10)

# Download button
download_button = tk.Button(root, text="Downlaod", command=download_video)
download_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
