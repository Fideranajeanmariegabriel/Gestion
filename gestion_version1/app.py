from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# Chiave segreta necessaria per i messaggi flash
app.secret_key = 'supersecretkey'

# Inserisci direttamente l'URI di MongoDB qui
MONGO_URI = "mongodb://localhost:27017/gestion"

# Connessione al client MongoDB
client = MongoClient(MONGO_URI)
db = client['gestion']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/inscription_etudiants', methods=['GET', 'POST'])
def inscription_etudiants():
    if request.method == 'POST':
        etudiant = {
            'nom_etudiant': request.form['nom_etudiant'],
            'prenom_etudiant': request.form['prenom_etudiant'],
            'date_de_naissance': request.form['date_de_naissance'],
            'lieu_de_naissance': request.form['lieu_de_naissance'],
            'nationalite': request.form['nationalite'],
            'adresse': request.form['adresse'],
            'telephone': request.form['telephone'],
            'email': request.form['email'],
            'classe': request.form['classe'],
            'etablissement_precedente': request.form['etablissement_precedente']
        }
        
        parents = {
            'nom': request.form['nom_parent'],
            'prenom': request.form['prenom_parent'],
            'adresse': request.form['adresse_parent'],
            'telephone': request.form['telephone_parent'],
            'email': request.form['email_parent'],
            'profession': request.form['profession_parent'],
            'relation_avec_etudiant': request.form['relation_avec_etudiant'],
            'situation_familiale': request.form['situation_familiale'],
            'autorisation_de_sortie': request.form['autorisation_de_sortie'],
            'personne_a_contacter_en_cas_d_urgence': request.form['personne_a_contacter_en_cas_d_urgence']
        }

        db.etudiants.insert_one({'etudiant': etudiant, 'parents': parents})
        
        return redirect(url_for('home'))
    return render_template('inscription_etudiants.html')

@app.route('/inscription_professeurs', methods=['GET', 'POST'])
def inscription_professeurs():
    if request.method == 'POST':
        professeur = {
            'nom_professeur': request.form['nom_professeur'],
            'prenom_professeur': request.form['prenom_professeur'],
            'date_de_naissance': request.form['date_de_naissance'],
            'lieu_de_naissance': request.form['lieu_de_naissance'],
            'nationalite': request.form['nationalite'],
            'adresse': request.form['adresse'],
            'telephone': request.form['telephone'],
            'email': request.form['email'],
            'numero_de_securite_sociale': request.form['numero_de_securite_sociale'],
            'diplomes': request.form['diplomes'],
            'specialite': request.form['specialite'],
            'experience_professionnelle': request.form['experience_professionnelle'],
            'etablissement_precedents': request.form['etablissement_precedents'],
            'date_d_entree_en_fonction': request.form['date_d_entree_en_fonction'],
            'poste_actuel': request.form['poste_actuel'],
            'disponibilite': request.form['disponibilite'],
            'langues_parlees': request.form['langues_parlees'],
            'personne_a_contacter_en_cas_d_urgence': request.form['personne_a_contacter_en_cas_d_urgence'],
            'references': request.form['references'],
            'mot_de_passe': request.form['mot_de_passe'],
            'matieres_enseigner': request.form.getlist('matieres_enseigner')  # Récupérer les matières sélectionnées
        }

        db.professeurs.insert_one(professeur)
        flash('Inscription réussie!', 'success')
        return redirect(url_for('inscription_professeurs'))
    return render_template('inscription_professeurs.html')

#######################GESTION ETUDIANTS##############################################
@app.route('/gestion_etudiants')
def gestion_etudiants():
    return render_template('gestion_etudiants.html')

@app.route('/get_students')
def get_students():
    classe = request.args.get('classe')
    query = {'etudiant.classe': classe} if classe else {}
    students = list(db.etudiants.find(query))
    for student in students:
        student['_id'] = str(student['_id'])  # Convertir ObjectId en chaîne pour JSON
    return jsonify(students)

@app.route('/edit_student/<id>', methods=['GET', 'POST'])
def edit_student(id):
    if request.method == 'POST':
        # Code pour mettre à jour les informations de l'étudiant
        pass
    else:
        student = db.etudiants.find_one({'_id': ObjectId(id)})
        if student:
            student['_id'] = str(student['_id'])  # Convertir ObjectId en chaîne pour JSON
            return render_template('edit_student.html', student=student)
        else:
            return redirect(url_for('gestion_etudiants'))

@app.route('/delete_student/<id>', methods=['DELETE'])
def delete_student(id):
    db.etudiants.delete_one({'_id': ObjectId(id)})
    return '', 204

#################################GESTION PROFESSEUR#################################
@app.route('/gestion_professeurs')
def gestion_professeurs():
    return render_template('gestion_professeurs.html')

@app.route('/get_professeurs')
def get_professeurs():
    classe = request.args.get('classe')
    query = {'professeur.classe': classe} if classe else {}
    professeurs = list(db.professeurs.find(query))
    for professeur in professeurs:
        professeur['_id'] = str(professeur['_id'])  # Convertir ObjectId en chaîne pour JSON
    return jsonify(professeurs)

@app.route('/edit_professeur/<id>', methods=['GET', 'POST'])
def edit_professeur(id):
    if request.method == 'POST':
        # Code pour mettre à jour les informations du professeur
        pass
    else:
        professeur = db.professeurs.find_one({'_id': ObjectId(id)})
        if professeur:
            professeur['_id'] = str(professeur['_id'])  # Convertir ObjectId en chaîne pour JSON
            return render_template('edit_professeur.html', professeur=professeur)
        else:
            return redirect(url_for('gestion_professeurs'))

@app.route('/delete_professeur/<id>', methods=['DELETE'])
def delete_professeur(id):
    db.professeurs.delete_one({'_id': ObjectId(id)})
    return '', 204


# Supposons que l'authentification est déjà gérée et que le professeur est connecté.
# Nous récupérons ses informations via la session.
@app.route('/gestion_notes', methods=['GET', 'POST'])
def gestion_notes():
    professeur_id = session.get('professeur_id')
    
    if not professeur_id:
        flash('Vous devez être connecté pour accéder à cette page.', 'danger')
        return redirect(url_for('home'))
    
    professeur = db.professeurs.find_one({'_id': ObjectId(professeur_id)})
    
    if not professeur:
        flash('Professeur non trouvé.', 'danger')
        return redirect(url_for('home'))

    if request.method == 'POST':
        matiere = request.form['matiere']
        etudiant_id = request.form['etudiant_id']
        bimestre = int(request.form['bimestre'])
        note = float(request.form['note'])

        # Validation que le professeur enseigne bien la matière
        if matiere not in professeur['matieres_enseigner']:
            flash('Vous ne pouvez pas ajouter de notes pour une matière que vous n\'enseignez pas.', 'danger')
            return redirect(url_for('gestion_notes'))

        # Ajout de la note pour l'étudiant
        note_data = {
            'professeur_id': professeur_id,
            'matiere': matiere,
            'bimestre': bimestre,
            'note': note
        }

        db.etudiants.update_one(
            {'_id': ObjectId(etudiant_id)},
            {'$push': {'notes': note_data}}
        )
        flash('Note ajoutée avec succès.', 'success')
        return redirect(url_for('gestion_notes'))
    
    etudiants = list(db.etudiants.find())
    return render_template('gestion_notes.html', etudiants=etudiants, matieres=professeur['matieres_enseigner'])


if __name__ == '__main__':
    app.run(debug=True)
