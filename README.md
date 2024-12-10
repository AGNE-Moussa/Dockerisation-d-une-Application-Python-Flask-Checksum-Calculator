# Dockerisation d'une Application Python Flask : Checksum Calculator

## Introduction  
La conteneurisation avec Docker a transformé le déploiement d'applications en offrant un environnement cohérent du développement à la production. Ce guide détaille le processus de dockerisation d'une application Python Flask appelée **Checksum Calculator**.  
Cette application permet aux utilisateurs de :  
- Saisir une chaîne de caractères.  
- Calculer son checksum avec un algorithme de hachage sélectionné (parmi SHA-256, SHA-1, MD5, SHA-384, SHA-512).  
- Visualiser le résultat sous forme de tableau.

---

## Qu’est-ce que Docker ?  
**Docker** est une plateforme open-source conçue pour automatiser le déploiement d’applications dans des conteneurs légers et portables. Ces conteneurs encapsulent le code de l’application, ses dépendances, ses bibliothèques et configurations, garantissant un fonctionnement homogène sur différents environnements.

---

## Fonctionnalités de l'application  
- Saisie d'une chaîne de caractères par l'utilisateur.  
- Choix parmi plusieurs algorithmes de hachage :  
  - **SHA-256**, **SHA-1**, **MD5**, **SHA-384**, **SHA-512**.  
- Calcul du checksum selon l'algorithme choisi.  
- Affichage du résultat dans un tableau interactif.

---

## Technologies utilisées  
- **Python 3.9**  
- **Flask**  
- **Docker**  
- **Docker Compose**  

---

## Configuration de l'application  

### Étape 1 : Préparer l'environnement  
1. Créez un répertoire pour le projet et accédez-y :  
   ```bash
   mkdir web-application  
   cd web-application  


  Créez un environnement virtuel et activez-le :
  

python -m venv venv  
source venv/bin/activate  

Installez Flask :

    pip install flask  

    Créez un fichier principal nommé app.py pour votre application Flask.

Étape 2 : Créer un Dockerfile

Un Dockerfile est un fichier contenant toutes les commandes nécessaires pour assembler une image Docker.

    Créez un fichier nommé Dockerfile dans le répertoire du projet.
    Créez également un fichier requirements.txt et ajoutez-y la ligne suivante :

    flask  

Construction et exécution avec Docker
Étape 1 : Construire l'image Docker

Pour construire l'image Docker, exécutez la commande suivante dans le terminal :

docker build -t web-app .  

Cela génère une image Docker nommée web-app à partir du Dockerfile dans le répertoire courant.
Étape 2 : Exécuter le conteneur Docker

Lancez l'application dans un conteneur avec la commande suivante :

docker run -d -p 5000:5000 web-app  

    L'option -d exécute le conteneur en mode détaché.
    Le port 5000 de l'hôte est mappé au port 5000 du conteneur.

Test de l'application

Ouvrez un navigateur web et accédez à l'adresse suivante :
http://localhost:5000
Gestion des dépendances avec Docker Compose

Docker Compose simplifie la gestion d'applications multi-conteneurs.

    Créez un fichier docker-compose.yml pour définir les services et leurs configurations.
    Démarrez l'application en exécutant :

    docker-compose up -d  

Conclusion

En suivant ce guide, vous aurez une application Flask fonctionnelle, containerisée avec Docker, et facilement déployable sur n'importe quel environnement. Pour toute question ou contribution, n'hésitez pas à ouvrir une issue ou soumettre une pull request.
Ressources supplémentaires

    Documentation officielle de Docker
    Documentation de Flask
    Guide Docker Compose

