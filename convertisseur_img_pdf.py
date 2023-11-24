from PIL import Image
import os

# Chemin du dossier contenant les images .jpg
input_folder = 'chemin/du/dossier/'

# Liste des fichiers .jpg dans le dossier
jpg_files = [f for f in os.listdir(input_folder) if f.endswith('.jpg')]

# Trier les fichiers par ordre alphabétique
jpg_files.sort()

# Ouvrir la première image pour définir la taille du PDF
with Image.open(input_folder + jpg_files[0]) as im:
    pdf = Image.new(im.mode, (im.width, im.height*len(jpg_files)))

# Ajouter chaque image au PDF
for i, file in enumerate(jpg_files):
    with Image.open(input_folder + file) as im:
        pdf.paste(im, (0, i*im.height))

# Enregistrer le PDF
pdf.save('chemin/vers/fichier.pdf', save_all=True)
