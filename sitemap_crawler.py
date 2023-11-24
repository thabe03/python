import requests
from bs4 import BeautifulSoup

# Fonction pour extraire les URLs d'un sitemap XML
def extract_sitemap_urls(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'xml')
            return [loc.text for loc in soup.find_all('loc')]
        else:
            print(f"Erreur lors de la récupération du sitemap : {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête : {e}")
        return []

# Fonction principale du crawler
def sitemap_crawler(base_url, sitemap_url):
    sitemap_urls = extract_sitemap_urls(sitemap_url)
    if sitemap_urls:
        for url in sitemap_urls:
            # Traitez chaque URL ici
            print(f"URL trouvée : {url}")
            # Vous pouvez ajouter votre logique de traitement ici

if __name__ == "__main__":
    base_url = input(">>")  # Remplacez par l'URL de base de votre site
    sitemap_url = f"{base_url}/sitemap.xml"  # Assurez-vous que l'URL du sitemap est correcte
    sitemap_crawler(base_url, sitemap_url)
