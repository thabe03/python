import os
import random
from PIL import Image
from moviepy.editor import *
import pysrt

# chemin du dossier contenant les images
image_folder = "D:/Tiktok/Case/"

# chemin du fichier audio
audio_file =  "D:/Tiktok/1/1.mp3"

if not os.path.isfile("D:/Tiktok/1/1.mp4"):

    # création d'une liste des noms des fichiers images
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]

    # sélection aléatoire des images
    random.shuffle(image_files)

    # calcul de la durée de l'audio
    audio_duration = AudioFileClip(audio_file).duration

    # création d'une liste des clips vidéos avec durée aléatoire entre 5 et 10 secondes
    clips = []
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        image = Image.open(image_path)
        duration = random.uniform(5, 10)
        clip = ImageClip(image_path).set_duration(duration)
        clips.append(clip)

    # création de la vidéo avec les clips et l'audio
    video = concatenate_videoclips(clips)
    video = video.set_audio(AudioFileClip(audio_file))

    # ajustement de la durée de la vidéo si elle est plus longue que l'audio
    if video.duration > audio_duration:
        video = video.subclip(0, audio_duration)

    # enregistrement de la vidéo
    video.fps = 24
    video.write_videofile('D:/Tiktok/1/1.mp4')
