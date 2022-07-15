import pytube

link = input("Enter the link: ")
yt = pytube.YouTube(link)
yt.streams.first().download()
print("Downloaded", yt.title)
