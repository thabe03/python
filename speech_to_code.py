import speech_recognition as sr

# Définir le récepteur pour le microphone par défaut
r = sr.Recognizer()

# Démarrer le microphone pour écouter l'utilisateur
with sr.Microphone() as source:
    print("Dites quelque chose...")
    audio = r.listen(source)

# Transcrire la parole de l'utilisateur en texte
try:
    code = r.recognize_google(audio, language='en-CA')
    print(f"Vous avez dit: {code}")
except sr.UnknownValueError:
    print("Impossible de comprendre ce que vous avez dit")
except sr.RequestError as e:
    print("Impossible d'accéder à la reconnaissance vocale Google ; {0}".format(e))

# Importer pyautogui après la transcription de la parole
import pyautogui as pg

# Simuler les frappes de clavier pour écrire le code transcrit
pg.typewrite(code)
