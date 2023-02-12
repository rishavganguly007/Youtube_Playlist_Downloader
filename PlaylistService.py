import re
import pathlib
from pytube import Playlist
import os

def getVideosFromPlaylist(yt_link: str):
    playlist = Playlist(yt_link)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    return playlist