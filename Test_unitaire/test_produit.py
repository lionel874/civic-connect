def test_creer_produit_valide(client):

    response = client.post(
        "/produit/",
        params={
            "nom": "Clavier",
            "prix": 5000,
            "quantite": 20
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["nom_p"] == "Clavier"
    assert data["prix_p"] == 5000
    assert data["quantite_p"] == 20


def test_lire_produits(client):

    response = client.get("/produit/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_remplacer_produit(client, product_id):

    response = client.put(
        f"/produit/{product_id}",
        params={
            "nouveau_nom": "Souris",
            "nouveau_prix": 3000,
            "nouvelle_quantite": 15
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["nom_p"] == "Souris"
    assert data["prix_p"] == 3000
    assert data["quantite_p"] == 15


def test_patch_prix_seul(client, product_id):

    response = client.patch(
        f"/produit/{product_id}",
        params={"nouveau_prix": 7500}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["prix_p"] == 7500


def test_supprimer_produit(client):

    creation = client.post(
        "/produit/",
        params={
            "nom": "A supprimer",
            "prix": 1000,
            "quantite": 5
        }
    )

    produit_id = creation.json()["id_p"]

    response = client.delete(f"/produit/{produit_id}")

    assert response.status_code == 200


def test_supprimer_produit_inexistant(client):

    response = client.delete("/produit/999999")

    assert response.status_code == 400