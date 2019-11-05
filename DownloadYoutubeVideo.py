from pytube import YouTube

SAVE_PATH = "/Users/keon/Downloads"

link = "https://www.youtube.com/watch?v=3T2JgwDC9Xs"

try:
    yt = YouTube(link)
except:
    print("Connection Errorrrrrr")
stream = yt.streams.first()
stream.download(SAVE_PATH)
