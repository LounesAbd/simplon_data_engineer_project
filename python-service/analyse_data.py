import sqlite3
from datetime import date

# Path de la base de données
DB_PATH = '/data/database.db'

# Connexion SQLite
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Date du jour
today = date.today().isoformat()

# 1 - Insertion des données dans la table 'total_ca'
cur.execute("""
            SELECT SUM(v.quantite * p.prix) AS total_ca
            FROM ventes v
            JOIN produits p ON v.ref_produit = p.ref_produit_id
            """)
total_ca = cur.fetchone()[0] or 0.0

cur.execute("""
            INSERT INTO total_ca (total_ca, date_analyse)
            VALUES (?, ?)
            """, (total_ca, today))

print(f"✅ CA total : {total_ca:.2f} €")

# 2 - Insertion des données dans la table 'ventes_produit'
cur.execute("""
            SELECT
                v.ref_produit,
                p.nom AS nom_produit,
                SUM(v.quantite) AS quantite,
                SUM(v.quantite * p.prix) AS total_ca
            FROM ventes AS v
            JOIN produits AS p ON v.ref_produit = p.ref_produit_id
            GROUP BY v.ref_produit, p.nom
            """)
ventes_produit = cur.fetchall()

for ref_produit, nom_produit, quantite, total_ca in ventes_produit:
    cur.execute("""
                INSERT INTO ventes_produit (ref_produit, nom_produit, quantite, total_ca, date_analyse)
                VALUES (?, ?, ?, ?, ?)
                """, (ref_produit, nom_produit, quantite, total_ca, today))
    
print(f"✅ CA par produit : {len(ventes_produit)} lignes insérées")

# 3 - Insertion des données dans la table 'ventes_region'
cur.execute("""
            SELECT
                m.ville,
                SUM(v.quantite * p.prix) AS total_ca
            FROM ventes AS v
            JOIN produits AS p ON v.ref_produit = p.ref_produit_id
            JOIN magasins AS m ON v.magasin_id = m.magasin_id
            GROUP BY m.ville
            """)
ventes_region = cur.fetchall()

for ville, total_ca in ventes_region:
    cur.execute("""
                INSERT INTO ventes_region (ville, total_ca, date_analyse)
                VALUES (?, ?, ?)
                """, (ville, total_ca, today))
    
print(f"✅ CA par région : {len(ventes_region)} lignes insérées")

conn.commit()
conn.close()
print("🏁 Analyse terminée et résultats stockées dans la base.")