import sqlite3
from io import StringIO
import pandas as pd
import requests

# Path de la base de données
DB_PATH = '/data/database.db'

# URLs des fichiers CSV à importer
URL_PRODUITS = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=0&single=true&output=csv"
URL_MAGASINS = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=714623615&single=true&output=csv"
URL_VENTES = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=760830694&single=true&output=csv"

# Fonction de téléchargement CSV
def download_csv(url):
    response = requests.get(url)
    response.raise_for_status() # Vérifie si la requête a réussi
    response.encoding = 'utf-8' # Définit le bon encodage pour accepter les caractères spéciaux t.q accents
    return pd.read_csv(StringIO(response.text))

# Téléchargement des fichiers CSV
produits_df = download_csv(URL_PRODUITS)
magasins_df = download_csv(URL_MAGASINS)
ventes_df = download_csv(URL_VENTES)

# Connexion SQLite
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Import des produits
print("📦 Insertion des produits...")
produits_df.columns = ['nom', 'ref_produit_id', 'prix', 'stock']

cur.execute("DELETE FROM produits") # Supprime les anciennes données
conn.commit()

produits_df.to_sql('produits', conn, if_exists='append', index=False)

# Import des magasins
print("🏪 Insertion des magasins...")
magasins_df.columns = ['magasin_id', 'ville', 'nb_salaries']

cur.execute("DELETE FROM magasins") # Supprime les anciennes données
conn.commit()

magasins_df.to_sql('magasins', conn, if_exists='append', index=False)

# Import des ventes (en évitant les doublons)
print("💸 Insertion des ventes (avec vérification)...")
ventes_df.columns = ['date', 'ref_produit', 'quantite', 'magasin_id']

inserted = 0
skipped = 0

for _, row in ventes_df.iterrows():
    # Vérifie si la vente existe déjà
    cur.execute("""
        SELECT 1 FROM ventes
        WHERE date = ? AND ref_produit = ? AND quantite = ? AND magasin_id = ?
    """, (row["date"], row["ref_produit"], row["quantite"], row["magasin_id"]))
    
    if not cur.fetchone():
        cur.execute("""
            INSERT INTO ventes (date, ref_produit, quantite, magasin_id)
            VALUES (?, ?, ?, ?)
        """, (row["date"], row["ref_produit"], row["quantite"], row["magasin_id"]))
        inserted += 1
    else:
        skipped += 1

conn.commit()
conn.close()

print(f"✅ Import terminé : {inserted} ventes insérées, {skipped} ignorées.")