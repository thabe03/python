from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# Ouvrir l'image
image_path = "C:/Users/xi1le/OneDrive/Bureau/Test/20210226_184047.jpg"
image = Image.open(image_path)

# Obtenir les métadonnées EXIF
exif_data = image._getexif()

if exif_data:
    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        print(f"{tag_name}: {value}")
else:
    print("Aucune métadonnée EXIF trouvée dans cette image.")
