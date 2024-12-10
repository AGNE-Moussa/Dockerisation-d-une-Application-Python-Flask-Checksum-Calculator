#Introduction
La conteneurisation avec Docker a révolutionné la manière dont les développeurs déploient des applications, en offrant un environnement cohérent du développement à la production.Ce guide vous expliquera le processus de dockerisation d’une application Python Flask en utilisant Docker.L'application web (Checksum Calculator) construite avec Python et Flask va permettre à l'utilisateur de saisir une chaîne de caractères et d'obtenir son checksum SHA-256 ou tout autre algorithme de hachage sélectionné

#Qu’est-ce que Docker?
Docker est une plateforme open-source conçue pour automatiser le déploiement d’applications dans des conteneurs légers et portables. Ces conteneurs regroupent le code de l’application avec toutes ses dépendances, bibliothèques et configurations, garantissant qu’elle fonctionne de manière homogène sur différents environnements informatiques.

#Fonctionnalités de l'application
Saisie d'une chaîne de caractères par l'utilisateur
Choix de l'algorithme de hachage (SHA-256, SHA-1, MD5, SHA-384, SHA-512)
Calcul du checksum de la chaîne de caractères selon l'algorithme sélectionné
Affichage du résultat dans un tableau

#Technologies utilisées
Python 3.9
Flask
Docker
Dockerfile
Docker Compose
