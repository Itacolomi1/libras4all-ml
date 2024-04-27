from pytube import YouTube
from moviepy.editor import *
# import uuid

# video_uuid = uuid.uuid4()

# YouTube video URL
video_url = "https://www.youtube.com/watch?v=M72Yj5WcxRs"
save_path = 'D:\\Data_Science-USP\\TCC\\dados\\raw'

# Download the video
yt = YouTube(video_url)
stream = yt.streams.filter(file_extension = 'mp4').first()
#stream.download(output_path = save_path, filename = f'[{yt.channel_id}]-{yt.title}.mp4')
stream.download(output_path = save_path, filename = f'[{yt.channel_id}].mp4')

# Convert the video to MP3
# video_path = stream.default_filename
# mp4_file = video_path
# mp3_file = f"{yt.title}.mp3"

# video_clip = VideoFileClip(mp4_file)
# audioclip = video_clip.audio
# audioclip.write_audiofile(mp3_file)

# Close the video file
# audioclip.close()
# video_clip.close()
