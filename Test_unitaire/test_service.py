def test_creer_service_valide(client, user_id, location_id):

    response = client.post(
        "/services/",
        params={
            "nom_s": "Vente PC",
            "description": "Ordinateurs à bas prix",
            "prix": 150000,
            "categorie": "Electronique",
            "user_id": user_id,
            "location_id": location_id
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["nom_s"] == "Vente PC"
    assert data["categorie"] == "Electronique"
    assert data["prix"] == 150000


def test_categorie_vide(client, user_id, location_id):

    response = client.post(
        "/services/",
        params={
            "nom_s": "Vente PC",
            "description": "Ordinateurs à bas prix",
            "prix": 150000,
            "categorie": "",
            "user_id": user_id,
            "location_id": location_id
        }
    )

    assert response.status_code == 400


def test_prix_negatif(client, user_id, location_id):

    response = client.post(
        "/services/",
        params={
            "nom_s": "Vente PC",
            "description": "Ordinateurs à bas prix",
            "prix": -100,
            "categorie": "Electronique",
            "user_id": user_id,
            "location_id": location_id
        }
    )

    assert response.status_code == 400


def test_user_inexistant(client, location_id):

    response = client.post(
        "/services/",
        params={
            "nom_s": "Vente PC",
            "description": "Ordinateurs à bas prix",
            "prix": 150000,
            "categorie": "Electronique",
            "user_id": 999999,
            "location_id": location_id
        }
    )

    assert response.status_code == 400


def test_filtre_categorie(client, user_id, location_id):

    client.post(
        "/services/",
        params={
            "nom_s": "Reparation telephone",
            "description": "Reparation rapide",
            "prix": 5000,
            "categorie": "Reparation",
            "user_id": user_id,
            "location_id": location_id
        }
    )

    response = client.get(
        "/services/",
        params={"categorie": "Reparation"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["total"] >= 1

    categories = [service["categorie"] for service in data["resultats"]]

    assert "Reparation" in categories


def test_filtre_categorie_inexistante(client):

    response = client.get(
        "/services/",
        params={"categorie": "CategorieBidon"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["total"] == 0
    assert data["resultats"] == []


def test_pagination_limit(client, user_id, location_id):

    for i in range(3):
        client.post(
            "/services/",
            params={
                "nom_s": f"Service {i}",
                "description": "Description",
                "prix": 1000,
                "categorie": "Divers",
                "user_id": user_id,
                "location_id": location_id
            }
        )

    response = client.get(
        "/services/",
        params={"limit": 2}
    )

    data = response.json()

    assert len(data["resultats"]) <= 2


def test_supprimer_service(client, user_id, location_id):

    creation = client.post(
        "/services/",
        params={
            "nom_s": "A supprimer",
            "description": "Sera supprime",
            "prix": 1000,
            "categorie": "Divers",
            "user_id": user_id,
            "location_id": location_id
        }
    )

    service_id = creation.json()["id_s"]

    response = client.delete(f"/services/{service_id}")

    assert response.status_code == 200


def test_supprimer_service_inexistant(client):

    response = client.delete("/services/999999")

    assert response.status_code == 400