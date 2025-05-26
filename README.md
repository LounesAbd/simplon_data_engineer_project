# Test de positionnement formation Data Engineer Simplon

_Projet pour l'entretien de sélection pour la formation Data Engineer de Simplon._

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

🏗 [Architecture des services](https://github.com/user-attachments/assets/a90184a1-3b86-40ce-8e6d-5df8f7ab84a4)

🔗 [Schema de la base de données](https://github.com/user-attachments/assets/f5727bfc-e38f-49ca-b662-52c5eac9f828)

🐋 [Dockerfile](https://github.com/LounesAbd/simplon_data_engineer_project/blob/main/python-service/Dockerfile)

🚢 [Docker Compose](https://github.com/LounesAbd/simplon_data_engineer_project/blob/main/docker-compose.yml)

⚙️ [Scripts d'éxecution Python](https://github.com/LounesAbd/simplon_data_engineer_project/tree/main/python-service)

📝 [Fiche synthèse des résultats d'analyse obtenus](https://github.com/LounesAbd/simplon_data_engineer_project/blob/main/analyses/fiche_synthese.pdf)

📹 [Video de démonstration](https://github.com/user-attachments/assets/10464e61-1592-4ab7-9a5a-df59da0e2054)
