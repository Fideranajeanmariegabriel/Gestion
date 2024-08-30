document.addEventListener('DOMContentLoaded', function() {
    const openButton = document.getElementById('open-button');
    const classeSelect = document.getElementById('classe-select');
    const tableBody = document.querySelector('#professeurs-table tbody');

    openButton.addEventListener('click', function() {
        const classe = classeSelect.value;
        if (classe) {
            fetch(`/get_professeurs?classe=${classe}`)
                .then(response => response.json())
                .then(data => {
                    tableBody.innerHTML = ''; // Clear existing table data
                    data.forEach(professeur => {
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td>${professeur.professeur.nom_professeur}</td>
                            <td>${professeur.professeur.prenom_professeur}</td>
                            <td>${professeur.professeur.date_de_naissance}</td>
                            <td>${professeur.professeur.lieu_de_naissance}</td>
                            <td>${professeur.professeur.nationalite}</td>
                            <td>${professeur.professeur.adresse}</td>
                            <td>${professeur.professeur.telephone}</td>
                            <td>${professeur.professeur.email}</td>
                            <td>${professeur.professeur.numero_de_securite_sociale}</td>
                            <td>${professeur.professeur.diplomes}</td>
                            <td>${professeur.professeur.specialite}</td>
                            <td>${professeur.professeur.experience_professionnelle}</td>
                            <td>${professeur.professeur.etablissement_precedents}</td>
                            <td>${professeur.professeur.date_d_entree_en_fonction}</td>
                            <td>${professeur.professeur.poste_actuel}</td>
                            <td>${professeur.professeur.disponibilite}</td>
                            <td>${professeur.professeur.langues_parlees}</td>
                            <td>
                                <button onclick="editProfesseur('${professeur._id}')">Modifier</button>
                                <button onclick="deleteProfesseur('${professeur._id}')">Supprimer</button>
                            </td>
                        `;
                        tableBody.appendChild(row);
                    });
                })
                .catch(error => console.error('Error:', error));
        } else {
            alert('Veuillez sélectionner une classe.');
        }
    });
});

function editProfesseur(id) {
    window.location.href = `/edit_professeur/${id}`;
}

function deleteProfesseur(id) {
    fetch(`/delete_professeur/${id}`, { method: 'DELETE' })
        .then(response => {
            if (response.ok) {
                document.querySelector(`tr[data-id='${id}']`).remove();
            }
        })
        .catch(error => console.error('Error:', error));
}
