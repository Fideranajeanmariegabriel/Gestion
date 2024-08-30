from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client.gestion
collection_etudiants = db.etudiants

@app.route('/')
def home():
    return redirect(url_for('acces_professeur'))

@app.route('/acces_professeur', methods=['GET', 'POST'])
def acces_professeur():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Authentication logic here, for example, checking credentials in MongoDB
        professeur = db.professeurs.find_one({"email": email, "mot_de_passe": password})
        
        if professeur:
            return redirect(url_for('note_matiere', nom_du_professeur=professeur['nom_professeur']))
        else:
            return "Login failed. Please try again."

    return render_template('acces_professeur.html')

@app.route('/note_matiere/<nom_du_professeur>', methods=['GET', 'POST'])
def note_matiere(nom_du_professeur):
    if request.method == 'POST':
        annee_scolaire = request.form['annee_scolaire']
        bimestre = request.form['bimestre']
        classe = request.form['classe']
        matiere = request.form['matiere']
        notes = []

        for key, value in request.form.items():
            if 'note_' in key:
                notes.append({
                    'id': key.replace('note_', ''),
                    'note': value
                })

        # Save notes to MongoDB
        for note in notes:
            collection_etudiants.update_one(
                {"_id": note['id']},
                {"$set": {f"notes.{annee_scolaire}.{bimestre}.{matiere}": note['note']}}
            )

        return "Notes have been updated!"

    # Extract classes and subjects the professor teaches
    professeur = db.professeurs.find_one({"nom_professeur": nom_du_professeur})
    classes = professeur.get('classe', [])
    matieres = professeur.get('matieres_enseigner', [])

    return render_template('note_matiere.html', nom_du_professeur=nom_du_professeur, classes=classes, matieres=matieres)

if __name__ == '__main__':
    app.run(debug=True)
