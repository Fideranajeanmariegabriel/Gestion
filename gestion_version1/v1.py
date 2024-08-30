from pymongo import MongoClient
from faker import Faker

# Connexion à MongoDB
MONGO_URI = "mongodb://localhost:27017/gestion"
client = MongoClient(MONGO_URI)
db = client['gestion']
etudiants_collection = db['etudiants']

# Initialiser Faker pour générer des données fictives
fake = Faker()

# Générer 10 enregistrements d'étudiants pour la classe TC
students = []
for _ in range(10):
    etudiant = {
        'nom_etudiant': fake.last_name(),
        'prenom_etudiant': fake.first_name(),
        'date_de_naissance': fake.date_of_birth(minimum_age=15, maximum_age=18).strftime('%Y-%m-%d'),
        'lieu_de_naissance': fake.city(),
        'nationalite': fake.country(),
        'adresse': fake.address(),
        'telephone': fake.phone_number(),
        'email': fake.email(),
        'classe': 'TC',
        'etablissement_precedente': fake.company()
    }
    
    parents = {
        'nom': fake.last_name(),
        'prenom': fake.first_name(),
        'adresse': fake.address(),
        'telephone': fake.phone_number(),
        'email': fake.email(),
        'profession': fake.job(),
        'relation_avec_etudiant': fake.word(),
        'situation_familiale': fake.word(),
        'autorisation_de_sortie': fake.word(),
        'personne_a_contacter_en_cas_d_urgence': fake.name()
    }

    students.append({'etudiant': etudiant, 'parents': parents})

# Insérer les données dans MongoDB
etudiants_collection.insert_many(students)

print("10 étudiants ont été ajoutés à la base de données.")
