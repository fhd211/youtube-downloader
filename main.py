from pytube import YouTube
from pytubefix import YouTube
from pytubefix.cli import on_progress
 
url = "https://www.youtube.com/watch?v=yddBiuvcaFs"
 
yt = YouTube(url, on_progress_callback = on_progress)

ys=yt.streams.filter()
# yss=yt.streams.get_by_itag(137)
ys = yt.streams.get_highest_resolution(137)
# print(yt.title)
yss=ys.download()

yss
