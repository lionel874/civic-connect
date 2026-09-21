console.log("app.js est chargé");

document.getElementById("formulaire-recherche").addEventListener("submit", function(event) {
    event.preventDefault();

    const motCle = document.getElementById("mot_cle").value;
    const categorie = document.getElementById("categorie").value;
    const zone = document.getElementById("zone").value;

    const url = `http://127.0.0.1:8000/services/?mot_cle=${motCle}&categorie=${categorie}&zone=${zone}`;

    
        fetch(url)
        .then(response => response.json())
        .then(data => {
            afficherResultats(data.resultats);
        });
});

function afficherResultats(services) {
    const zoneResultats = document.getElementById("resultats");
    zoneResultats.innerHTML = "";

    if (services.length === 0) {
        zoneResultats.innerHTML = "<p>Aucun service trouvé.</p>";
        return;
    }

    services.forEach(service => {
        zoneResultats.innerHTML += `
            <div class="card mb-2 p-3">
                <h5>${service.nom_s}</h5>
                <p>${service.description}</p>
                <p><strong>${service.prix} FCFA</strong> — ${service.categorie}</p>
                <p>📍 ${service.ville}, ${service.quartier}</p>
            </div>
        `;
    });
}

document.getElementById("btn-voir-tous").addEventListener("click", function() {
    fetch("http://127.0.0.1:8000/services/")
        .then(response => response.json())
        .then(data => {
            afficherResultats(data.resultats);
        });
});