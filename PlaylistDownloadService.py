import pathlib
from pytube import Playlist
from pytube import YouTube
import os
import pytube.exceptions as ex

def downloadPlaylist(playlist: YouTube,DOWNLOAD_DIR):
    i=0
    skippedPlaylistVideos : list  = []

    for video in playlist:
        try:
            i += 1
            print('{} downloading : {} with url : {}'.format(i, video.title, video.watch_url))
            stream = video.streams.filter(type='video', progressive=True, file_extension='mp4', resolution="360p")
            stream.get_by_itag(18).download(DOWNLOAD_DIR)
        except ex.PytubeError:
            print("Pytube Error, Video Skipped")
            skippedPlaylistVideos.append(YouTube(video.watch_url))
            continue

        else:
            print('downloaded : {} with url : {}'.format(video.title, video.watch_url))

    return skippedPlaylistVideos

