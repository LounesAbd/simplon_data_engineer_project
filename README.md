# Simplon Data Engineer Entry Project

## Projet pour la préparation à la journée de sélection pour le parcours de formation Data Engineer.

## 🎯 Objectifs visés :
- Créer et mettre en œuvre une architecture avec deux services : un d’exécution de scripts et un
autre de stockage de données
- Explorer et qualifier un jeu de données et en expliquer ses caractéristiques
- Créer une base de données cohérente avec les données qualifiées
- Importer des données à partir de fichiers distants
- Réaliser un premier niveau d’analyses de données avec SQL
- Stocker les résultats des analyses

## 📝 Brief :

_Scénario_

Vous êtes technicien·ne système et vous assistez un⸱e data engineer, au sein d’une PME de services
numériques. Un client de votre entreprise souhaite mieux comprendre la dynamique de ses ventes afin
d’améliorer leur prise de décision stratégique.

Dans un premier temps, votre responsable data engineer vous demande de :
- réaliser une analyse préalable afin de mieux cadrer le projet final. Pour cela, le client vous a fourni
un extrait de leur jeu de données des ventes sur 30 jours et des données relatives à ses produits
et à ses magasins distribués dans plusieurs villes de France.
- concevoir une architecture en deux services : un premier service pour l’exécution des scripts dans le langage de programmation de
votre choix. Un deuxième service pour le stockage des données en base de données avec SQLite.
- implémenter l’architecture conçue : Créez les fichiers Dockerfile et Docker Compose. Assurez la bonne exécution de l’architecture.

Vous devez prendre connaissance des données partagées et en comprendre les principales
caractéristiques pour créer le schéma de la base de données avec ces tables et relations. Une fois le
schéma créé vous devez :
- créer une base de données avec ses tables associées afin d'importer les données partagées par
le client dans la base de données
- effectuer une première analyse des ventes avec SQL
- stocker les résultats des analyses

Comme le fichier de données sur les ventes s'actualise en temps réel, vous devez vous assurer que les
lignes de données à importer ne sont pas déjà stockées en base de données.

## 🗂 Ressources :

_Données de l'entreprise (URLs)_

Données "produits" : https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=0&single=true&output=csv

Données "magasins" : https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=714623615&single=true&output=csv

Données "ventes" : https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=760830694&single=true&output=csv

## 📥 Livrables :

_Schémas de l'architecture des services et de la base de données_
[INSÉRER IMAGES]

_Dockerfile_
-> Voir le fichier dans ce repo

_Docker Compose_
-> Voir le fichier dans ce repo

_Scripts d'éxecution Python_
-> Voir les fichiers dans ce repo

_Fiche synthèse des résultats d'analyse obtenus_
[CRÉER LE FICHIER PUIS L'AJOUTER AU REPO]
