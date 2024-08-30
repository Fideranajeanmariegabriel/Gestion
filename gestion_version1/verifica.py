from pymongo import MongoClient

# Inserisci direttamente l'URI di MongoDB qui
MONGO_URI = "mongodb://localhost:27017/gestion"

# Connessione al client MongoDB
client = MongoClient(MONGO_URI)

# Seleziona il database e la collezione
db = client['etudiants']
collection = db['test_collection']

# Documento di test
test_document = {
    "nome": "Mario",
    "cognome": "Rossi",
    "email": "mario.rossi@example.com"
}

# Inserisce il documento nella collezione
insert_result = collection.insert_one(test_document)
print(f"Documento inserito con _id: {insert_result.inserted_id}")

# Recupera il documento appena inserito
retrieved_document = collection.find_one({"_id": insert_result.inserted_id})
print("Documento recuperato:")
print(retrieved_document)
