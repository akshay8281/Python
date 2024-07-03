# pyTube
'''
For pytube First of all to install from CMD PROMPT

pip install pytube
'''

from pytube import YouTube

# Where to save
SAVE_PATH = "E:\\Coding World\\Python\\Python\\Tops Programs"

# Link of the video to be downloaded
link = "https://www.youtube.com/watch?v=zcq3fv_DJaw&list=RDzcq3fv_DJaw&start_radio=1"

try:
    # Object creation using YouTube
    yt = YouTube(link)
except Exception as e:
    print(f"Connection Error: {e}")
    exit()

# Get all streams and filter for mp4 files
mp4_streams = yt.streams.filter(file_extension='mp4')

if not mp4_streams:
    print("No mp4 streams found")
    exit()

# Get the video with the highest resolution
d_video = mp4_streams.get_highest_resolution()

try:
    # Downloading the video
    d_video.download(output_path=SAVE_PATH)
    print('Video downloaded successfully!')
except Exception as e:
    print(f"Some Error: {e}")
