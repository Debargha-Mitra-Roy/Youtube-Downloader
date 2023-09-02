from pytube import YouTube
from pytube import Playlist

link = input("Enter the Link : ")

youtube_1 = YouTube(link)

print(youtube_1.title)  # Title of the YouTube Video
print(
    youtube_1.thumbnail_url
)  # Thumnail of the YouTube Video (Click the link to open the thumbnail)

videos = youtube_1.streams.all()  # All formats
# videos = youtube_1.streams.filter(only_audio=True) # Only Audio files

vid = list(enumerate(videos))

for i in vid:
    print(i)


strm = int(input("Enter the index no. "))

videos[strm].download()

print("Your video is downloaded successfully. Thanks for using our service.")
