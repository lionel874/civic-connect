function chargerProduits() {
    fetch("http://127.0.0.1:8000/produit/")
        .then(response => response.json())
        .then(produits => {
            const zone = document.getElementById("liste-produits");
            zone.innerHTML = "";

            if (produits.length === 0) {
                zone.innerHTML = "<p class='text-muted'>Aucun produit pour l'instant.</p>";
                return;
            }

            produits.forEach(produit => {
                zone.innerHTML += `
                    <div class="col-12 col-md-6 col-lg-4">
                        <div class="card shadow-sm h-100" style="cursor:pointer" onclick="voirDetailsProduit(${produit.id_p}, '${produit.nom_p}', ${produit.prix_p}, ${produit.quantite_p})">
                            <div class="card-body">
                                <h5 class="card-title">${produit.nom_p}</h5>
                                <p class="card-text fs-5 text-success fw-bold">${produit.prix_p} FCFA</p>
                                <span class="badge bg-secondary mb-2">Stock : ${produit.quantite_p}</span>
                                <button class="btn btn-outline-danger btn-sm w-100" onclick="supprimerProduit(${produit.id_p})">Supprimer</button>
                            </div>
                        </div>
                    </div>
                `;
            });
        });
}

function supprimerProduit(id) {
    fetch(`http://127.0.0.1:8000/produit/${id}`, {
        method: "DELETE"
    })
        .then(response => {
            if (response.ok) {
                chargerProduits();
            }
        });
}
function voirDetailsProduit(id, nom, prix, quantite) {
    document.getElementById("modalTitre").innerText = nom;
    document.getElementById("modalCorps").innerHTML = `
        <p><strong>Prix :</strong> ${prix} FCFA</p>
        <p><strong>Stock disponible :</strong> ${quantite}</p>
        <p><strong>Identifiant :</strong> ${id}</p>
    `;

    const modal = new bootstrap.Modal(document.getElementById("modalDetails"));
    modal.show();
}

function voirDetailsCommande(id, titre, quantite, montant) {
    document.getElementById("modalTitre").innerText = titre;
    document.getElementById("modalCorps").innerHTML = `
        <p><strong>Quantité :</strong> ${quantite}</p>
        <p><strong>Montant total :</strong> ${montant} FCFA</p>
        <p><strong>Identifiant :</strong> ${id}</p>
    `;

    const modal = new bootstrap.Modal(document.getElementById("modalDetails"));
    modal.show();
}

function chargerCommandes() {
    fetch("http://127.0.0.1:8000/orders/")
        .then(response => response.json())
        .then(commandes => {
            const zone = document.getElementById("liste-commandes");
            zone.innerHTML = "";

            if (commandes.length === 0) {
                zone.innerHTML = "<p class='text-muted'>Aucune commande pour l'instant.</p>";
                return;
            }

            commandes.forEach(commande => {
                zone.innerHTML += `
                    <div class="col-12 col-md-6 col-lg-4">
                        <div class="card shadow-sm h-100 border-start border-primary border-3" style="cursor:pointer" onclick="voirDetailsCommande(${commande.num_o}, '${commande.titre_o}', ${commande.quantite_o}, ${commande.mte_total})">
                            <div class="card-body">
                                <h5 class="card-title">${commande.titre_o}</h5>
                                <p class="card-text mb-1">Quantité : <strong>${commande.quantite_o}</strong></p>
                                <p class="card-text fs-5 text-primary fw-bold mb-2">${commande.mte_total} FCFA</p>
                                <button class="btn btn-outline-danger btn-sm w-100" onclick="supprimerCommande(${commande.num_o})">Supprimer</button>
                            </div>
                        </div>
                    </div>
                `;
            });
        });
}

function supprimerCommande(id) {
    fetch(`http://127.0.0.1:8000/orders/${id}`, {
        method: "DELETE"
    })
        .then(response => {
            if (response.ok) {
                chargerCommandes();
            }
        });
}

chargerProduits();
chargerCommandes();