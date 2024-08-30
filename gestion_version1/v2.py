from pymongo import MongoClient
from faker import Faker
import random

# Connexion au client MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['gestion']
collection = db['etudiants']

# Générateur de données fictives
fake = Faker()

# Liste des classes
classes = [
    'Prescolaire', '12è', '11è', '10è', '9è', '8è', '7è', '4è', '3è', '2nd',
    '1èS', '1èL', '1èT', 'TA', 'TD', 'TC'
]

def generate_student_data(classe):
    """Génère des données fictives pour un étudiant."""
    return {
        'etudiant': {
            'nom_etudiant': fake.last_name(),
            'prenom_etudiant': fake.first_name(),
            'date_de_naissance': fake.date_of_birth(minimum_age=10, maximum_age=18).isoformat(),
            'lieu_de_naissance': fake.city(),
            'nationalite': fake.country(),
            'adresse': fake.address(),
            'telephone': fake.phone_number(),
            'email': fake.email(),
            'classe': classe,
            'etablissement_precedente': fake.company()
        },
        'parents': {
            'nom': fake.last_name(),
            'prenom': fake.first_name(),
            'adresse': fake.address(),
            'telephone': fake.phone_number(),
            'email': fake.email(),
            'profession': fake.job(),
            'relation_avec_etudiant': 'Parent',
            'situation_familiale': 'Marié',
            'autorisation_de_sortie': 'Oui',
            'personne_a_contacter_en_cas_d_urgence': fake.name()
        }
    }

def insert_students_for_classes():
    """Insère des étudiants pour chaque classe."""
    for classe in classes:
        students = [generate_student_data(classe) for _ in range(10)]
        collection.insert_many(students)
        print(f"Insertion de 10 étudiants pour la classe {classe}")

if __name__ == "__main__":
    insert_students_for_classes()
    print("Insertion terminée.")
