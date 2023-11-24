import threading

# Créer un verrou
verrou = threading.Lock()

# Fonction qui utilise le verrou
def fonction_protégée():
    with verrou:  # Utilisez un bloc "with" pour verrouiller et déverrouiller automatiquement le verrou.
        # Code qui accède aux ressources partagées en toute sécurité
        print("Thread en cours :", threading.current_thread().name)
        for _ in range(5):
            print("Travail en cours...")
        print("Travail terminé.")

# Créez plusieurs threads qui exécutent la fonction_protégée
thread1 = threading.Thread(target=fonction_protégée)
thread2 = threading.Thread(target=fonction_protégée)

# Démarrez les threads
thread1.start()
thread2.start()

# Attendez que les threads se terminent
thread1.join()
thread2.join()

# Le verrou garantit que le travail est effectué en séquence, même si les threads s'exécutent en parallèle.
