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


document.getElementById("btn-voir-signalements").addEventListener("click", function() {
    fetch("http://127.0.0.1:8000/reports/")
        .then(response => response.json())
        .then(data => {
            const zone = document.getElementById("liste-signalements");
            zone.innerHTML = "";

            if (data.resultats.length === 0) {
                zone.innerHTML = "<p class='text-muted'>Aucun signalement pour l'instant.</p>";
                return;
            }

            data.resultats.forEach(signalement => {
                const couleur = signalement.statut === "en cours" ? "warning" : "success";

                zone.innerHTML += `
                    <div class="card mb-2 p-3">
                        <h5>${signalement.titre}</h5>
                        <p>${signalement.description}</p>
                        <p>📍 ${signalement.ville}, ${signalement.quartier}</p>
                        <span class="badge bg-${couleur}">${signalement.statut}</span>
                    </div>
                `;
            });
        });
});