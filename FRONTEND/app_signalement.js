document.getElementById("formulaire-signalement").addEventListener("submit", function(event) {
    event.preventDefault();

    const titre = document.getElementById("titre").value;
    const description = document.getElementById("description").value;
    const userId = document.getElementById("user_id").value;
    const locationId = document.getElementById("location_id").value;

    const url = `http://127.0.0.1:8000/reports/?titre=${titre}&description=${description}&user_id=${userId}&location_id=${locationId}`;

    fetch(url, {
        method: "POST"
    })
        .then(response => {
            if (response.ok) {
                afficherMessage("Signalement envoyé avec succès !", "success");
                document.getElementById("formulaire-signalement").reset();
            } else {
                afficherMessage("Erreur : vérifiez les informations saisies.", "danger");
            }
        });
});

function afficherMessage(texte, type) {
    const zoneMessage = document.getElementById("message");
    zoneMessage.innerHTML = `<div class="alert alert-${type}">${texte}</div>`;
}