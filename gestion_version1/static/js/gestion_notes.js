// Injection des matières et étudiants depuis Flask
const matieres = JSON.parse(document.getElementById('matieres-data').textContent);
const etudiants = JSON.parse(document.getElementById('etudiants-data').textContent);

const matiereSelect = document.getElementById('matiere');
const etudiantSelect = document.getElementById('etudiant');
const noteForm = document.getElementById('noteForm');
const errorMessage = document.getElementById('error-message');

// Remplir le select avec les matières disponibles
matieres.forEach(matiere => {
    const option = document.createElement('option');
    option.value = matiere;
    option.textContent = matiere;
    matiereSelect.appendChild(option);
});

// Remplir le select avec les étudiants disponibles
etudiants.forEach(etudiant => {
    const option = document.createElement('option');
    option.value = etudiant._id;
    option.textContent = `${etudiant.etudiant.nom_etudiant} ${etudiant.etudiant.prenom_etudiant}`;
    etudiantSelect.appendChild(option);
});

// Validation JavaScript lors de la soumission du formulaire
noteForm.addEventListener('submit', function(e) {
    const matiere = matiereSelect.value;
    
    // Vérifier si la matière sélectionnée est dans la liste des matières enseignées
    if (!matieres.includes(matiere)) {
        // Empêcher la soumission du formulaire
        e.preventDefault();

        // Afficher un message d'erreur
        errorMessage.style.display = 'block';
    } else {
        // Cacher le message d'erreur si la validation passe
        errorMessage.style.display = 'none';
    }
});
