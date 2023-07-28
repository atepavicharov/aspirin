from pytube import Playlist
from pytube import YouTube as YT

DOWNLOAD_DIR = 'D:\\Downloads\\mp3'

plist = input('Enter a playlist URL: ')

# videos = list(Playlist(plist))

video = YT(plist, use_oauth=True, allow_oauth_cache=True)
# stream = video.streams.get_by_itag(140)
# stream.download(output_path=DOWNLOAD_DIR)
video.streams.filter(type='audio').order_by('abr').desc().first().download(output_path=DOWNLOAD_DIR)

# for i in range(len(videos)):
#     print(i, '-', videos[i])
#
#     video = YT(videos[i], use_oauth=True, allow_oauth_cache=True)
#     stream = video.streams.get_by_itag(140)
#     stream.download(output_path=DOWNLOAD_DIR)

print('----------done---------')

# YouTube('https://www.youtube.com/watch?v=i7NnvtjCBDI&t=424s').streams.first().download()
# video = YouTube('https://www.youtube.com/watch?v=i7NnvtjCBDI')
# video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
