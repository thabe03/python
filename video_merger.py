from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

# Path to the folder containing the videos to merge
folder_path = "C:/Users/xi1le/Box/Adobe photoshop"

# List all the video file names in the folder
videos = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]

# Sort the video file names in alphabetical order
videos.sort()

# Create an array of video clips from the files in the folder
clips = [VideoFileClip(os.path.join(folder_path, v)) for v in videos]

# Concatenate the video clips
final_clip = concatenate_videoclips(clips)

# Write the final concatenated video to a file
final_clip.write_videofile("output.mp4")
