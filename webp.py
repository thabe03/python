import requests
from PIL import Image
import io

url = "https://lexica-serve-encoded-images.sharif.workers.dev/md/0482ee68-0368-4eca-8846-5930db866b33"
response = requests.get(url, stream=True)

with open("image.webp", "wb") as f:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)

with Image.open("image.webp").convert("RGB") as image:
    image.save("image.jpg")
