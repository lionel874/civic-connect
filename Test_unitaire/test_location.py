def test_creer_location_valide(client):

    response = client.post(
        "/localisation/",
        params={
            "ville": "Bafoussam",
            "quartier": "Tamdja",
            "adresse": "Rue 10"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["ville"] == "Bafoussam"
    assert data["quartier"] == "Tamdja"


def test_lire_locations(client):

    response = client.get("/localisation/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_supprimer_location(client):

    creation = client.post(
        "/localisation/",
        params={
            "ville": "Dschang",
            "quartier": "Foto",
            "adresse": "Rue 5"
        }
    )

    location_id = creation.json()["id_l"]

    response = client.delete(f"/localisation/{location_id}")

    assert response.status_code == 200


def test_supprimer_location_inexistante(client):

    response = client.delete("/localisation/999999")

    assert response.status_code == 400