from pymongo import MongoClient
from faker import Faker

# Connexion au client MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['gestion']
collection = db['professeurs']

# Générateur de données fictives
fake = Faker()

# Liste des matières et des classes
matieres = [
    'Mathematiques', 'Physiques', 'Chimies', 'Sciences_de_la_Vie_et_de_la_Terre',
    'Français', 'Anglais', 'Malagasy', 'Espagnol', 'Allemand',
    'Education_Physique_et_Sportives', 'Informatiques',
    'Sciences_et_Techniques_Industrielles', 'Sciences_de_l_Ingenieur'
]

classes = [
    'Prescolaire', '12è', '11è', '10è', '9è', '8è', '7è', '4è', '3è', '2nd',
    '1èS', '1èL', '1èT', 'TA', 'TD', 'TC'
]

def generate_professor_data(matiere, classe):
    """Génère des données fictives pour un professeur."""
    return {
        'nom_professeur': fake.last_name(),
        'prenom_professeur': fake.first_name(),
        'date_de_naissance': fake.date_of_birth(minimum_age=30, maximum_age=60).isoformat(),
        'lieu_de_naissance': fake.city(),
        'nationalite': fake.country(),
        'adresse': fake.address(),
        'telephone': fake.phone_number(),
        'email': fake.email(),
        'numero_de_securite_sociale': fake.ssn(),
        'diplomes': fake.word(),
        'specialite': matiere,
        'experience_professionnelle': fake.text(max_nb_chars=100),
        'etablissement_precedents': fake.company(),
        'date_d_entree_en_fonction': fake.date_this_decade().isoformat(),
        'poste_actuel': fake.job(),
        'disponibilite': fake.word(),
        'langues_parlees': fake.language_name(),
        'personne_a_contacter_en_cas_d_urgence': fake.name(),
        'references': fake.text(max_nb_chars=50),
        'mot_de_passe': fake.password(),
        'matieres_enseigner': [matiere],
        'classe': classe
    }

def insert_professors_for_classes_and_subjects():
    """Insère des professeurs pour chaque matière et chaque classe."""
    professors = []
    for matiere in matieres:
        for classe in classes:
            professor = generate_professor_data(matiere, classe)
            professors.append(professor)
            print(f"Préparation de l'insertion pour {matiere} dans {classe}")

    # Insertion en une seule opération
    collection.insert_many(professors)
    print("Insertion des professeurs terminée.")

if __name__ == "__main__":
    insert_professors_for_classes_and_subjects()
    print("Insertion terminée.")
