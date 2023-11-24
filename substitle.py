import os
from gtts import gTTS
from moviepy.editor import AudioFileClip

text = "Hello world. This is a test transcript."
path = "."

# Convert text to audio
tts = gTTS(text)
tts.save(f"{path}/audio.mp3")

# Get audio duration
audio = AudioFileClip(f"{path}/audio.mp3")
audio_duration = audio.duration

# Create subtitles
subtitles = []
lines = text.split(". ")
for i, line in enumerate(lines):
    start = i * audio_duration / len(lines)
    end = (i + 1) * audio_duration / len(lines)
    subtitle = {"start": start, "end": end, "text": line}
    subtitles.append(subtitle)

# Generate SRT file
srt = ""
for i, subtitle in enumerate(subtitles):
    srt += str(i+1) + "\n"
    srt += "{0:02d}:{1:02d}:{2:06.3f},000 --> {3:02d}:{4:02d}:{5:06.3f},000\n".format(
        0, 0, subtitle["start"], 0, 0, subtitle["end"])
    srt += subtitle["text"] + "\n\n"
with open(f"{path}/subtitles.srt", "w") as f:
    f.write(srt)
