import re
import pathlib
import PlaylistService as _playlistService
import PlaylistDownloadService as _playlistDownloadService
from pytube import Playlist
from pytube import YouTube
import os


def main():
    playlist = _playlistService.getVideosFromPlaylist('https://www.youtube.com/playlist?list=PLF3cuN1QRaoTwyMUyn2tXqqdbnohucaTG')
    yt_vdos = [YouTube(x) for x in playlist.video_urls]
    DOWNLOAD_DIR = pathlib.Path("E:\Maths101")
    skipped_vdos = _playlistDownloadService.downloadPlaylist(yt_vdos,DOWNLOAD_DIR)
    while(len(skipped_vdos) != 0):
        skipped_vdos = _playlistDownloadService.downloadPlaylist(yt_vdos,DOWNLOAD_DIR)

if __name__ =="__main__":
    main()
