import ipsec
# Définir les paramètres de la connexion IPsec
params = {
 "local_ip": "192. 168. 1. 10",
 "local_port": 500,
 "remote_ip": "192. 168. 1. 20",
 "remote_port": 500,
 "proposal": "aes256-sha1-modp1024",
 "my_id": "192. 168. 1. 10",
 "peer_id": "192. 168. 1. 20",
 "my_key": "123456",
 "peer_key": "abcdef"
}
# Établir la connexion IPsec
conn = ipsec. IPsec(params)
conn. initiate()
Ce code établit une connexion IPsec entre les adresses IP 192. 168. 1. 10 et 192. 168. 1. 20 sur les ports 500 et utilise le mode de chiffrement aes256-sha1-modp1024. Les identités et clés de chiffrement des deux points de la connexion sont également définies dans les paramètres. La connexion est ensuite initiée en appelant la méthode initiate() de l'objet IPsec. 
