import pandas as pd
from sklearn. neighbors import NearestNeighbors
# Récupérer les données sur les chansons (par exemple en les lisant à partir d'un fichier CSV)
song_data = pd. read_csv('song_data. csv')
# Préparer les données en utilisant Pandas (par exemple en créant une matrice d'utilisateurs et de chansons)
song_data = song_data. pivot_table(index='user_id', columns='song_id', values='listen_count')
# Entraîner un modèle de filtrage collaboratif en utilisant scikit-learn
model = NearestNeighbors()
model. fit(song_data)
# Prédire les préférences d'un utilisateur en fonction des préférences des autres utilisateurs
user_id = 1
distances, indices = model. kneighbors(song_data. loc[user_id, :]. values. reshape(1, -1), n_neighbors=5)
# Afficher les chansons recommandées pour cet utilisateur
for i, song_id in enumerate(indices[0][1:]):
 print(f'Recommandation n°{i+1}: {song_data. columns[song_id]}')
Cet exemple utilise l'algorithme des k plus proches voisins pour prédire les préférences d'un utilisateur en fonction des préférences des autres utilisateurs. Vous pouvez utiliser d'autres algorithmes de filtrage collaboratif selon les besoins de votre implémentation. 
