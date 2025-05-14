from pytubefix import YouTube
from pathlib import Path

def download_vid(url):
    downloads_path = str(Path.home() / "Downloads")
    
    yt = YouTube(url)
    
    vid = yt.streams.get_highest_resolution()
    vid.download(output_path=downloads_path)

print(dir())