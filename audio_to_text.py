import os
from pydub import AudioSegment
# from pydub.silence import split_on_silence
import speech_recognition as sr 
import glob
from scipy.io.wavfile import read
from pydub.utils import make_chunks
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Paramètres
audio_folder = 'audio'


def convert_mp3(file_path):
    print("Conversion " + file_path + " à WAV [INFO]")
    audio = AudioSegment.from_mp3(file_path)
    wav_path = file_path.replace(".mp3", ".wav")
    audio.export(wav_path, format="wav")
    return wav_path

def convert_m4a(file_path):
    print("Converting " + file_path + " à WAV [INFO]")
    audio = AudioSegment.from_file(file_path, format="m4a")
    wav_path = file_path.replace(".m4a", ".wav")
    audio.export(wav_path, format="wav")
    return wav_path

def convert_mp4(input_file):
    video = VideoFileClip(input_file)
    audio = video.audio
    output_file = input_file.replace(".mp4",".wav")
    audio.write_audiofile(output_file, codec='pcm_s16le')
    return output_file

def merge_convert_mp4(*video_paths):
    clips = []
    for path in video_paths:
        clip = VideoFileClip(path)
        clips.append(clip)
    
    final_clip = concatenate_videoclips(clips)
    audio = final_clip.audio
    audio.write_audiofile(audio_folder+"/merged.wav", codec='pcm_s16le')
    return "merged.wav"


def chunk_audio(file_path):
    audio = AudioSegment.from_wav(file_path)
    audio_duration = len(audio)
    
    # Vérifier si la taille de l'audio est supérieure à la limite
    if audio_duration > 60000*10 and not os.path.exists("audio/chunk1.wav"):
        print("Séparation de l'audio "+ str(audio_duration) + " [INFO]")
        # Durée d'un chunk en millisecondes (1 minute = 60 secondes = 60 000 millisecondes)
        chunk_duration = 120000

        # Diviser l'audio en chunks d'une minute
        chunks = []
        start_time = 0
        while start_time < audio_duration:
            end_time = start_time + chunk_duration
            if end_time > audio_duration:
                end_time = audio_duration
            chunk = audio[start_time:end_time]
            chunks.append(chunk)
            start_time = end_time

        # Enregistrer chaque chunk dans un fichier séparé
        for i, chunk in enumerate(chunks, start=1):
            chunk.export(os.path.join(audio_folder, f"chunk{i}.wav"), format="wav")


# def chunk_audio(file_path):
#     audio = AudioSegment.from_file(file_path)
#     duration = len(audio)
    
#     # Vérifier si la taille de l'audio est supérieure à la limite
#     if duration > 50000 and not os.path.exists("audio/chunk1.wav"):
#         print("Séparation de l'audio "+ str(duration) + " [INFO]")
#         # Load audio file with pydub
#         audio = AudioSegment.from_mp3(file_path)
#         # Split audio at silent parts with duration of 700ms or more and obtain chunks
#         audio_chunks = split_on_silence(audio, min_silence_len=700, silence_thresh=audio.dBFS-14, keep_silence=700)

#         # Create a directory to store audio chunks

#         full_text = ""
#         failed_attempts = 0
#         # Process each audio chunk
#         for i, chunk in enumerate(audio_chunks, start=1):
#             # Save chunk in the directory
#             chunk_file_name = os.path.join(audio_folder, f"chunk{i}.wav")
#             chunk.export(chunk_file_name, format="wav")

def process_audio_files():

    # Obtenir la liste des fichiers du dossier
    files = os.listdir(audio_folder)
    wav_files = [file for file in files if file.lower().endswith('.wav')]

    # Créer le fichier resultat.txt s'il n'existe pas déjà
    result_file = os.path.join(audio_folder, 'resultat.txt')
    
    # Parcourir tous les fichiers .wav et effectuer la transcription de la parole
    r = sr.Recognizer()

    with open(result_file, 'w') as f:
        for wav_file in wav_files:
            file_path = os.path.join(audio_folder, wav_file)
            audio = sr.AudioFile(file_path)
            try:
                # Transcrire l'audio en texte
                with audio as source:
                    audio = r.record(source)  # Enregistrer l'audio depuis le fichier WAV
                    try:
                        code = r.recognize_google(audio, language='fr-CA')
                        f.write(code + '\n')
                    except sr.UnknownValueError:
                        print("Impossible de transcrire l'audio " + result_file + " [ERROR]")
                    except sr.RequestError as e:
                        print(f"Erreur lors de la requête de transcription : {e} [ERROR]")
            except sr.UnknownValueError:
                print('Erreur de transcription " + result_file + " [ERROR]\n')
    print("[END]")

# Créer le dossier audio s'il n'existe pas déjà
if not os.path.exists(audio_folder):
    print("audio créé [INFO]")
    os.makedirs(audio_folder)

for file_name in glob.glob('*'):
    file_path = os.path.join(os.getcwd(), file_name)
    if file_name.lower().endswith('.wav') or file_name.lower().endswith('.mp3') or file_name.lower().endswith('.mp4') or file_name.lower().endswith('.m4a'):
        if file_name.lower().endswith('.wav'):
            # Convertir en fichier WAV si nécessaire
            print("WAV détecté [INFO]")
        elif file_name.lower().endswith('.mp3'):
            print("MP3 détecté [INFO]")
            file_path = convert_mp3(file_name)
        elif file_name.lower().endswith('.m4a'):
            print("M4A détecté [INFO]")
            file_path = convert_m4a(file_name)
        elif file_name.lower().endswith('.mp4'):
            print("MP4 détecté [INFO]")
            mp4_files = glob.glob("/*.mp4")
            count = len(mp4_files)
            if count > 1:
                # Exemple d'utilisation
                end = int(input("Fin:"))
                video_list = range(1,end+1)
                video_list = [str(x) + ".mp4" for x in video_list]
                file_path = merge_convert_mp4(*video_list)
            else:
                file_path = convert_mp4(file_name)
        chunk_audio(file_path)

# Processus des fichiers audio dans le dossier audio
process_audio_files()
