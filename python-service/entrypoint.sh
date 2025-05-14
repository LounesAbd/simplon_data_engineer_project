#!/bin/bash
set -e  # Stoppe le script en cas d'erreur

echo "📦 Création de la database et des tables..."
python create_db.py

echo "📥 Importation des données..."
python import_data.py

echo "📊 Analyse des données..."
python analyse_data.py

echo "✅ Fin de l'exécution."
