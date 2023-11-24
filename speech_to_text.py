# pip install SpeechRecognition pydub
# pip install pyautogui
import speech_recognition as sr
from pydub import AudioSegment

# Chemin du fichier audio MP3
#audio_path = "chunk167.mp3"

# Chemin du fichier audio WAV de sortie
output_wav_path = "chunk167.wav"

# Convertir le fichier MP3 en WAV
#audio = AudioSegment.from_mp3(audio_path)
#audio.export(output_wav_path, format="wav")

# Créer un objet de reconnaissance vocale
r = sr.Recognizer()

# Transcrire l'audio en texte
with sr.AudioFile(output_wav_path) as source:
    audio = r.record(source)  # Enregistrer l'audio depuis le fichier WAV
    try:
        code = r.recognize_google(audio, language='fr-CA')
        print(f"Transcription audio: {code}")
    except sr.UnknownValueError:
        print("Impossible de transcrire l'audio")
    except sr.RequestError as e:
        print(f"Erreur lors de la requête de transcription : {e}")
