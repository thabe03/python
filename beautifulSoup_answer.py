import spacy
import requests
from bs4 import BeautifulSoup
from collections import Counter

nlp = spacy.load("en_core_web_sm")
response = requests.get("http://lite.cnn.com/en")
soup = BeautifulSoup(response.text, "html.parser")
doc = nlp(soup.getText())

names = []
for ent in doc.ents: # ai qui reconnait des labels
    if ent.label_ == "GPE":
        names.append(ent.lemma_)

print(Counter(names).most_common(10))

response = requests.get("http://lite.cnn.com/en")
soup = BeautifulSoup(response.content, "html.parser")

def clear():
  open("cache.html", "w").close()
  open("resp.txt", "w").close()
    
def quiz():
  for i in range(1,14):
    response = requests.get("https://m2.teluq.ca/theme/adm3028/assets/quiz/quiz"+str(i)+".html")
    with open('cache.html', 'ab') as f:
      f.write(response.content)

clear()
quiz()

with open('cache.html', 'rb') as f:
  soup = BeautifulSoup(f.read(), 'html.parser')
  things = soup.find_all('li', class_='correct')
for i in things:
  print(i.text)
# open("resp.xls", "w").close()
# path='resp.xls'
# with open(path,'w') as table:
#     for row in zip(li,p):
#         for cell in row:
#             table.write(str(cell) + '\t')
#         table.write('\n')




# doc = nlp("Mr. Best flew to New York on Saturday morning.") 
# # accept seulement du text
# ents = list(doc.ents) #entité à reconnaître
# assert ents[0].label_ == "PERSON"
# assert ents[0].text == "Mr. Best"