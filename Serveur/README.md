# Webservice
Notre webservice permet de collecter des informations sur des artistes disponibles sur deux API: 

* AudioDB 
* LyricsOvh 

Les fonctionnalités développées sont: 
* Permet de proposer de manière aléatoire une chanson, pour un artiste donné en entrée
* Contrôle l'état de santé des api cible

Le code implémentant ce service est dans le dossier **Serveur**.
Un fichier **.env** est ausi disponible et liste les différents liens d'accès aux différentes API. Dans le cadre de ce rendu, il est accessible dans le dossier afin de permettre l'exécution du code. 

Pour lancer le webservice, exécutez la ligne de code suivante:
```
python main.py
```