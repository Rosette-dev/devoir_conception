# Générateur de playlists

![Drag Racing](Ressources/playlist.jpg)

## Présentation application

**Le Générateur de playlist** est une application qui développe dans un premier temps un webservice et ensuite un client. 
L'application a pour objectif de permettre à l'utilisateur de générer une playliste aléatoire de musiques de ses artistes préférés. Pour ce faire, l'utilisateur a juste besoin de renseigner les noms de ses artistes préférés. Le webservice développé fournit l'information nécéssaire en se basant sur deux API: 

* AudioDB 
* LyricsOvh 

Le client (l'utilisateur, vous par exemple) donne un fichier json avec le nom de ses artistes préférés. Lorsque l'application est lancée, le webservice requète les API et renvoit la playlist demandée.
D'autres fonctionnalitées sont implémentées afin d'assurer le bon fonctionnement du webservice, ainsi qu'une meilleure expérience d'utilisaton pour préparer vos soirées karaoké entre amis :v:.


## Quick Start
Cette application a été developpée sous Python3.8.
Pour lancer le code, vous allez suivre ces étapes simples:
### Cloner le repo
Première étape, cloner le repo via les commandes ci-dessous. Vous pouvez également simplement télécharger le projet.
```
git clone https://github.com/Rosette-dev/devoir_conception.git
```

Assurez vous que l'IDE que vous utilisez est bien configuré notamment au niveau du worksapce et PYTHONPATH.
### Installer les modules
Ensuite, il est necessaire d'installer les libraries utiles (indispensable) au fonctionnement de l'app via la commande ci-dessous.
```
pip install -r requirements.txt
```
### Configuration
Ensuite dernière étape avant de profiter pleinement de l'application, la configuration.
#### Variables d'environnement
Dans un fichier ```.env``` que vous placer dans le dossier **Client**, vous copier coller et remplissez les informations ci-dessous afin d'obtenir la playliste qui vous ravira. 
```
CLIENT_DATA= *****
url_service= "http://127.0.0.1:8000"
TARGET_PORT=8000

```
**CLIENT_DATA** doit être un json qui permet d'avoir le nom des artistes. Par exemple:
```mermaid
;;;
[{
    "artiste": "daft punk",
    "note": 18
},
{
    "artiste":"gloria gaynor",
    "note": 10
}]
;;;
```
## Utilisation de l'application
Une fois que vous avez correctement installé et configuré l'application, pour l'utiliser il suffit de lancer le fichier ```main.py``` situé à la racine.

# Bonne utilisation !


