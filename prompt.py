import os
import requests
from PIL import Image
import io

# Prompt d'exemple
prompt = "cute chubby blue fruits icons for mobile game ui"

# Définir l'URL de l'API
url = f"https://lexica.art/api/v1/search?q={prompt}"

# Définir le dossier de destination pour les images JPEG
output_dir = "output/"

# Créer le dossier de destination s'il n'existe pas déjà
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Envoyer la requête pour télécharger les images
response = requests.get(url, stream=True)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Parser les données JSON pour récupérer les URLs des images
    image_urls = [image['src'] for image in response.json()['images']]
    # Parcourir les URLs, télécharger les images, les convertir et les enregistrer en JPEG
    for i, url in enumerate(image_urls):
        if i < 10:
            tmp = requests.get(url, stream=True)

            with open(f"{output_dir}/{i}.webp", "wb") as f:
                for chunk in tmp.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)

            with Image.open(f"{output_dir}/{i}.webp").convert("RGB") as image:
                image.save(f"{i}.jpg")

                # Récupérer la taille de l'image
                width, height = image.size

                # Calculer les ratios de redimensionnement
                width_ratio = 1080 / width
                height_ratio = 1920 / height

                # Calculer le ratio à utiliser pour remplir l'image
                fill_ratio = max(width_ratio, height_ratio)

                # Redimensionner l'image en utilisant le ratio de remplissage
                new_width = int(width * fill_ratio)
                new_height = int(height * fill_ratio)
                image = image.resize((new_width, new_height), resample=Image.LANCZOS)

                # Centrer l'image
                left = (new_width - 1080) / 2
                top = (new_height - 1920) / 2
                right = left + 1080
                bottom = top + 1920
                image = image.crop((left, top, right, bottom))

                # Enregistrer l'image
                image.save(f"{i}.jpg")


