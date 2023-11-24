import tkinter as tk
from PIL import ImageTk, Image
import cv2 
import numpy as np
 
# initialisation de la fenêtre
window = tk.Tk() 
window.title("Vidéomaker pour click-and-hold") 
window.geometry("1200x640") 
 
# Création de la chaîne de flux vidéo
cap = cv2.VideoCapture(0)  
 
def show_frame(): 
   
    _, frame = cap.read()
    frame = cv2.flip(frame, 1) 
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
    img = Image.fromarray(cv2image) 
    imgtk = ImageTk.PhotoImage(image=img) 
  
    lmain.imgtk = imgtk 
    lmain.configure(image=imgtk) 
    lmain.after(1, show_frame) 
 
# initialisation de la barre de titre
text_superieur = tk.Label(window, 
                   text="Vidéomaker pour click-and-hold", 
                   font=("Courier", 20)) 
text_superieur.pack() 

# fonction pour reconnaitre le click-et-hold 
def click_hold(event): 
    
    ret, frame = cap.read()
    
    # enregistre la vidéo  
    out = cv2.VideoWriter('recorded_video.avi', 
                       cv2.VideoWriter_fourcc(*'DIVX'), 
                       20.0, (640, 480)) 
   
    # affiche le texte "Enregistrement en cours"
    text_clique = tk.Label(window, 
                     text="Enregistrement en cours", 
                     font=("Courier", 20)) 
    text_clique.place(x=800, y=20) 

# fonction pour arreter l'enregistrement
def stop_recording(event): 
   
    out.release() 
   
    text_enregistre = tk.Label(window, 
                        text="Votre vidéo a été enregistrée", 
                        font=("Courier", 20)) 
    text_enregistre.place(x=800, y=60) 
 
    window.destroy() 

# initialisation des boutons  
rec_but = tk.Button(window,  
                    text='Cliquer & Hold pour enregistrer', 
                    width=20, command=click_hold) 
rec_but.place(x=800, y=100) 
  
stop_rec_but = tk.Button(window,  
                         text='Clicker pour arrêter l’enregistrement', 
                         width=20, command=stop_recording) 
stop_rec_but.place(x=800, y=150)  

# initialisation de l'endroit où se trouve la vidéo
lmain = tk.Label(window) 
lmain.place(x=0, y=30) 
 
# déclaration de show_frame()
show_frame() 
  
# démarrage de la fonction loop 
window.mainloop()