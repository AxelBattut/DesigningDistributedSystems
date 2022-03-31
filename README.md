# Bienvenue à notre projet "Designing-Distributed-Systems".

Dans ce projet, vous allez pouvoir utiliser en même temps MongoDB, Apache et Kafka Connect pour récupérer les données de l'API Binance et faire des requêtes sur celles-ci.
Tout d'abord nous obtenons notre date via notre fichier CreationTexte-BATTUT-CERIO-GUITTON.py et nous avons nos données dans notre fichier texte.
Une fois les données récupérées nous allons en effet utiliser Kafka pour les mettre dans un topic et utiliser Kafka connect avec mongodb pour effectuer des requêtes sur les données.

Le code principal (connexion Kafka et requêtes Mongodb) est situé dans **Projet-DDS-BATTUT-CERIO-GUITTON.py**. C'est le seul fichier que vous aurez besoin d'exécuter (manipulations pour savoir comment exécuter ci-dessous).

Attention, il est possible que vous deviez attendre un peu la réponse de la clé api lors du lancement de CreationTexte-BATTUT-CERIO-GUITTON.py.
## Comment exécuter

## Initialisation (dans votre terminal)

Lancez MongoDB

mongo --host 127.0.0.1:27017

Lancer Zookeeper

zookeeper-server-start.sh config/zookeeper.properties

Lancer Kafka

kafka-server-start.sh config/server.properties

Et pour l'affichage des données du topic :

bin/kafka-console-consumer.sh --topic ProjetDDS --from-beginning --bootstrap-server localhost:9092.


## Notre sujet et notre base de données 

Pour MongoDB :

Notre base de données s'appelle **"DDS "** et notre collection s'appelle **"myCollection "**.

Pour Kafka :

Notre Topic s'appelle **"ProjetDDS "**.

## Manipulation

Vous pouvez lire le code et importer les librairies que nous utilisons sur l'IDE de votre choix. L'importation des librairies est déjà faite dans notre fichier. 
Vous pouvez également installer les librairies si ce n'est pas déjà fait (pip install nom_de_votre_bibliothèque).


# Enfin

Vous devez utiliser trois fichiers, le notebook jupyter Projet-DDS-BATTUT-CERIO-GUITTON.py, fichier.txt (le fichier qui contient les données de CreationTexte-BATTUT-CERIO-GUITTON.py) 
et CreationTexte-BATTUT-CERIO-GUITTON.py (le fichier qui produit le fichier texte), vous devez placer ces trois fichiers dans le même répertoire (répertoire de votre choix).

Enfin, lorsque vous voyez cette ligne dans Projet-DDS-BATTUT-CERIO-GUITTON.py :  

```py
%run '/home/alexis/DDS/CreationTexte-BATTUT-CERIO-GUITTON.py'.
```

**Changez-le par votre chemin complet (le chemin de CreationTexte-BATTUT-CERIO-GUITTON.py).**


Travail réalisé par Alexis Cerio, Ines Guitton et Axel Battut.


Traduit avec www.DeepL.com/Translator (version gratuite)
