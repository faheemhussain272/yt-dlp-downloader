import yt_dlp

url = input("Enter YouTube URL: ")

ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
