document.addEventListener('DOMContentLoaded', function () {
    const classeField = document.getElementById('classe');
    const notesSection = document.getElementById('notes_section');

    classeField.addEventListener('change', function () {
        const selectedClasse = classeField.value;

        // Fetch students via an API or pre-loaded data
        fetch(`/api/get_students/${selectedClasse}`)
            .then(response => response.json())
            .then(students => {
                notesSection.innerHTML = ''; // Clear the section

                students.forEach(student => {
                    const input = document.createElement('input');
                    input.type = 'text';
                    input.name = `note_${student.id}`;
                    input.placeholder = `Note for ${student.nom}`;

                    notesSection.appendChild(input);
                });
            });
    });
});
