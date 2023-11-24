import pytesseract
from PIL import Image

# Chemin vers le fichier image à OCRiser
chemin_fichier = "C:/Users/xi1le/OneDrive/Bureau/static/fichier.jpg"

# Charger l'image avec PIL
image = Image.open(chemin_fichier)

# OCRiser l'image avec Pytesseract
texte = pytesseract.image_to_string(image)

# Afficher le texte OCRisé
print(texte)