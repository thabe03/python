from pathlib import Path
import requests
filename = Path('4718.pdf')
url = 'https://www.patersonnj.gov/egov/apps/document/center.egov?view=item;id=4718'
response = requests.get(url)
filename.write_bytes(response.content)