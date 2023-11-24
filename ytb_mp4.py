from pytube import YouTube
import os
  
# url input from user
yt = YouTube(
    str(input("Enter the URL of the video you want to download: \n>> ")))
  
# extract only audio
video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
  
# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = os.getcwd()
  
# download the file
out_file = video.download(output_path=destination)
  
# save the file
base, ext = os.path.splitext(out_file)
  
# result of success
print(yt.title + " has been successfully downloaded.")