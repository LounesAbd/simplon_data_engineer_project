import sqlite3
import os

DB_PATH = "/data/database.db"

# Vérifie si le fichier .db existe
db_exists = os.path.exists(DB_PATH)

# Connexion à la base de données SQLite
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

if not db_exists:
    print("📂 La base 'database.db' n'existe pas. Création du fichier...")
else:
    print("📂 La base 'database.db' existe déjà. Connexion...")

# Création des tables si elles n'existent pas
print("🛠️ Création des tables si nécessaire...")

# Création de la table 'produits'
query_create_produits = """
CREATE TABLE IF NOT EXISTS produits (
    ref_produit_id TEXT PRIMARY KEY,
    nom TEXT NOT NULL,
    prix REAL NOT NULL,
    stock INTEGER
    )
"""
cursor.execute(query_create_produits)

# Création de la table 'magasins'
query_create_magasins = """
CREATE TABLE IF NOT EXISTS magasins (
    magasin_id INTEGER PRIMARY KEY,
    ville TEXT NOT NULL,
    nb_salaries INTEGER NOT NULL
    )
"""
cursor.execute(query_create_magasins)

# Création de la table 'ventes'
query_create_ventes = """
CREATE TABLE IF NOT EXISTS ventes (
    vente_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    ref_produit TEXT,
    quantite INTEGER NOT NULL,
    magasin_id INTEGER,
    FOREIGN KEY (ref_produit) REFERENCES produits(ref_produit_id),
    FOREIGN KEY (magasin_id) REFERENCES magasins(magasin_id)
    )
"""
cursor.execute(query_create_ventes)

# Création de la table 'total_ca'
query_create_total_ca = """
CREATE TABLE IF NOT EXISTS total_ca (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    total_ca REAL,
    date_analyse TEXT
    )
"""
cursor.execute(query_create_total_ca)

# Création de la table 'ventes_produit'
query_create_ventes_produit = """
CREATE TABLE IF NOT EXISTS ventes_produit (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ref_produit TEXT,
    nom_produit TEXT,
    quantite INTEGER,
    total_ca REAL,
    date_analyse TEXT,
    FOREIGN KEY (ref_produit) REFERENCES produits(ref_produit_id)
    )
"""
cursor.execute(query_create_ventes_produit)

# Création de la table 'ventes_region'
query_create_ventes_region = """
CREATE TABLE IF NOT EXISTS ventes_region (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ville TEXT,
    total_ca REAL,
    date_analyse TEXT
    )
"""
cursor.execute(query_create_ventes_region)

conn.commit()
conn.close()

print("✅ Base de données et tables créées avec succès !")