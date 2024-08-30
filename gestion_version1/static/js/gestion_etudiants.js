// Fonction pour charger les étudiants en fonction de la classe sélectionnée
function loadStudents() {
    const classe = document.getElementById('classe').value;
    
    fetch(`/get_students?classe=${classe}`)
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#students-table tbody');
            tableBody.innerHTML = '';
            
            data.forEach(student => {
                const row = document.createElement('tr');
                
                row.innerHTML = `
                    <td>${student.etudiant.nom_etudiant}</td>
                    <td>${student.etudiant.prenom_etudiant}</td>
                    <td>${student.etudiant.date_de_naissance}</td>
                    <td>${student.etudiant.lieu_de_naissance}</td>
                    <td>${student.etudiant.nationalite}</td>
                    <td>${student.etudiant.adresse}</td>
                    <td>${student.etudiant.telephone}</td>
                    <td>${student.etudiant.email}</td>
                    <td>${student.etudiant.classe}</td>
                    <td>${student.etudiant.etablissement_precedente}</td>
                    <td>
                        <button onclick="editStudent('${student._id}')">Modifier</button>
                        <button onclick="deleteStudent('${student._id}')">Supprimer</button>
                    </td>
                `;
                
                tableBody.appendChild(row);
            });
        });
}

// Fonction pour rechercher dans le tableau
function searchTable() {
    const input = document.getElementById('search');
    const filter = input.value.toLowerCase();
    const rows = document.querySelectorAll('#students-table tbody tr');

    rows.forEach(row => {
        const cells = row.getElementsByTagName('td');
        let found = false;

        for (let i = 0; i < cells.length; i++) {
            if (cells[i].innerText.toLowerCase().includes(filter)) {
                found = true;
                break;
            }
        }

        row.style.display = found ? '' : 'none';
    });
}

// Fonction pour modifier un étudiant
function editStudent(id) {
    window.location.href = `/edit_student/${id}`;
}

// Fonction pour supprimer un étudiant
function deleteStudent(id) {
    fetch(`/delete_student/${id}`, { method: 'DELETE' })
        .then(response => {
            if (response.ok) {
                loadStudents(); // Recharger la liste des étudiants
            }
        });
}
