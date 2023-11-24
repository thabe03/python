# Importation des dépendances
import cv2
import numpy as np

# Définition des paramètres
height, width = 768, 1024

# Déclarer la fonction pour le click-and-hold
def click_and_hold(event, x, y, flags, params): 
    # Vérifier que l'utilisateur effectue un "click and hold"
    if event == cv2.EVENT_LBUTTONDOWN: 
        # Afficher le texte au point de "click and hold"
        cv2.putText(output, 'Click and Hold', (x, y), font, 0.5, (255, 255, 0), 2)
        # Enregistrer le point d'origine (point de départ)
        origin = (x, y)
    # Vérifier que l'utilisateur maintient le "click and hold"
    elif event == cv2.EVENT_LBUTTONUP: 
        # Insérer le texte sur la partie best et l'enregistrer
        cv2.putText(output, 'Best', (x, y), font, 0.5, (255, 255, 0), 2)
        # Enregistrer le point de fin (lorsque la souris est relâchée)
        end = (x, y)
        # Tracer un rectangle en fonction des points d'origine et de fin
        cv2.rectangle(output, origin, end, (0, 255, 255), 2) 

# Créer une fenêtre pour le click-and-hold
root = np.zeros((height, width, 3)) # Initialiser à zéro avec la hauteur, la la largeur et 3 couleurs (RGB)
output = root.copy() # Copier les données de l'image initiale 
cv2.namedWindow("Window")
font = cv2.FONT_HERSHEY_SIMPLEX 
cv2.setMouseCallback("Window", click_and_hold) 
 
# Boucle tant que l'utilisateur ne 'click and hold' pas sur "Quit" 
while(1): 
           # Afficher l'image
        cv2.imshow("Window", output) 
            # Demander si l'utilisateur veut quitter
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'): 
            break

# Libérer la fenêtre
cv2.destroyAllWindows()