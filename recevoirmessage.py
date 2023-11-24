import poplib
# Se connecter au serveur de messagerie
server = poplib. POP3('mailserver')
# Authentifier le serveur avec un nom d'utilisateur et un mot de passe
server. user('username')
server. pass_('password')
# Récupérer la liste des messages sur le serveur
messages = server. list()
# Parcourir les messages et afficher leur contenu
for message in messages:
 print(message)
# Fermer la connexion avec le serveur
server. quit()
Ce code se connecte à un serveur de messagerie, authentifie le serveur avec un nom d'utilisateur et un mot de passe, puis récupère la liste des messages sur le serveur. Il parcourt ensuite cette liste de messages et affiche leur contenu. 
Il est important de noter que ce code ne constitue qu'un exemple simple pour montrer comment utiliser le module poplib pour recevoir des messages sur un serveur de messagerie en Python. Pour créer un serveur de messagerie plus avancé, vous devrez ajouter d'autres fonctionnalités et traiter les erreurs de manière appropriée. 
