import smtplib
# Créer un serveur SMTP
server = smtplib. SMTP('localhost')
# Connecter le serveur à un port
server. connect(25)
# Authentifier le serveur avec un nom d'utilisateur et un mot de passe
server. login("username", "password")
# Définir l'expéditeur et le destinataire du message
from_address = "sender@example. com"
to_address = "recipient@example. com"
# Créer le corps du message
message = "This is a message from the server. "
# Envoyer le message
server. sendmail(from_address, to_address, message)
# Fermer la connexion avec le serveur
server. quit()
Ce code crée un serveur SMTP sur l'hôte local, se connecte à un port, authentifie le serveur avec un nom d'utilisateur et un mot de passe, puis envoie un message simple à un destinataire. 
Il est important de noter que ce code ne constitue qu'un exemple simple pour montrer comment utiliser le module smtplib pour créer un serveur de messagerie en Python. Pour créer un serveur de messagerie plus avancé, vous devrez ajouter d'autres fonctionnalités et traiter les erreurs de manière appropriée. 
