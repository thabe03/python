from PIL import Image

# Ouvrir l'image et la convertir en mode RGB
image = Image.open("image.jpg").convert("RGB")

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
image.save("image_cropped.jpg")
