from pytube import YouTube
from sys import argv


def progress_function(stream, chunk, bytes_remaining):
    size = stream.filesize
    percent = round((1 - bytes_remaining / size) * 100, 2)
    print(f"\rDownloading... {percent}%", end="")


try:
    link = argv[1]
    yt = YouTube(link, on_progress_callback=progress_function)

    print("Title:", yt.title)
    print("View:", yt.views)

    # download
    try:
        print("Downloading... Wait")
        yd = yt.streams.get_highest_resolution()
        # PASS THE PATH WHERE YOU WANT SAVE THE DOWNLOADED VIDEOS
        yd.download(r'C:\Users\Lucas\Documents\downloadsyoutube')
        print("\nDownload successful")
    except Exception as error:
        print(f"Download failed: {error}")

except Exception as e:
    print(f"Error: {e}")
