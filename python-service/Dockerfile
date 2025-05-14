# Utilise une image de base Python
FROM python:3.10-slim-bookworm

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier requirements.txt dans le conteneur
COPY requirements.txt .
# Installe les dépendances listées dans requirements.txt en utilisant uv
RUN pip install --no-cache-dir -r requirements.txt

# Copie le reste des fichiers de l'application dans le conteneur
COPY . /app

# Exécute le script de création de la base de données
CMD ["bash", "entrypoint.sh"]

