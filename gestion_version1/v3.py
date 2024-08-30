from pymongo import MongoClient
from datetime import datetime

# Configuration MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['gestion']  # Nom de la base de données
collection = db['professeurs']  # Nom de la collection

# Liste des matières et des classes avec les valeurs exactes
matieres = [
    'Mathematiques', 'Physiques', 'Chimies', 'Sciences_de_la_Vie_et_de_la_Terre',
    'Français', 'Anglais', 'Malagasy', 'Espagnol', 'Allemand',
    'Education_Physique_et_Sportives', 'Informatiques',
    'Sciences_et_Techniques_Industrielles', 'Sciences_de_l_Ingenieur'
]

classes = [
    'Prescolaire', '12è', '11è', '10è', '9è', '8è', '7è', '4è', '3è',
    '2nd', '1èS', '1èL', '1èT', 'TA', 'TD', 'TC'
]

# Fonction pour générer des informations uniques pour chaque professeur
def generate_professeur_info(matiere, classe):
    return {
        'nom_professeur': f'Nom_{matiere}_{classe}',
        'prenom_professeur': f'Prenom_{matiere}_{classe}',
        'date_de_naissance': datetime(1980, 1, 1).strftime('%Y-%m-%d'),
        'lieu_de_naissance': 'LieuParDefaut',
        'nationalite': 'NationaliteParDefaut',
        'adresse': 'AdresseParDefaut',
        'telephone': '0000000000',
        'email': f'{matiere}_{classe}@exemple.com',
        'numero_de_securite_sociale': '123456789',
        'diplomes': 'DiplomeParDefaut',
        'specialite': matiere,
        'experience_professionnelle': 'ExperienceParDefaut',
        'etablissement_precedents': 'EtablissementParDefaut',
        'date_d_entree_en_fonction': datetime(2024, 1, 1).strftime('%Y-%m-%d'),
        'poste_actuel': 'PosteParDefaut',
        'disponibilite': 'DisponibiliteParDefaut',
        'langues_parlees': 'LanguesParDefaut',
        'personne_a_contacter_en_cas_d_urgence': 'ContactUrgenceParDefaut',
        'references': 'ReferencesParDefaut',
        'mot_de_passe': 'MotDePasseParDefaut',
        'matieres_enseigner': [matiere],
        'classe': classe
    }

# Insertion des professeurs pour chaque matière et classe
for matiere in matieres:
    for classe in classes:
        professeur = generate_professeur_info(matiere, classe)
        collection.insert_one(professeur)
        print(f"Inséré professeur pour {matiere} dans {classe}")

print("Insertion des professeurs terminée.")
