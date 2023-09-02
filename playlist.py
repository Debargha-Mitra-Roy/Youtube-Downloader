from pytube import Playlist

url = input("Enter the playlist URL : ")

print(f'Downloading : {url.title}')

for video in url.videos:
    video.streams.first().download()

print("Your video is downloaded successfully. Thanks for using our service.")
