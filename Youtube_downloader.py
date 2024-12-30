from yt_dlp import YoutubeDL

# Directory to save the downloaded video
SAVE_PATH = "/Users/RyanYunseokChoi/Documents/Coding"

# YouTube video URL
link = "https://www.youtube.com/watch?v=rPt79QYxXEc"

# Options for downloading
ydl_opts = {
    'outtmpl': f"{SAVE_PATH}/%(title)s.%(ext)s",
    'format': 'best',  # Single best stream (no merging required)
}

# Download the video
try:
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print("Video downloaded successfully!")
except Exception as e:
    print(f"Error occurred: {e}")

