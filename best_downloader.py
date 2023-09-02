import pafy
import youtube_dl


link = input("Enter the video link : ")

video = pafy.new(link)

best = video.getbest()
print(best.resolution, best.extension)
best.download()
