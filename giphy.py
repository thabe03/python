import requests
import os

# Clé API Giphy
api_key = "P3F8sB8n36mWYn4JoN15GioCgezn8yW6"

# Recherche de GIF avec l'API Giphy
search_term = "Réseau Sécurité"
endpoint = f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={search_term}&limit=10"
response = requests.get(endpoint)
response_json = response.json()

# Téléchargement des 10 premiers GIF
for i, gif in enumerate(response_json["data"]):
    url = gif["images"]["original"]["url"]
    filename = f"gif_{i}.gif"
    filepath = os.path.join("D:/", filename)
    with open(filepath, "wb") as f:
        f.write(requests.get(url).content)
    print(f"GIF {i+1} téléchargé : {filename}")
