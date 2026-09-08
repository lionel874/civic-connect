def test_creer_report_valide(client, user_id, location_id):

    response = client.post(
        "/reports/",
        params={
            "titre": "Coupure electricite",
            "description": "Plus de courant depuis hier",
            "user_id": user_id,
            "location_id": location_id
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["titre"] == "Coupure electricite"
    assert data["type"] == "panne"
    assert data["statut"] == "en cours"


def test_titre_vide(client, user_id, location_id):

    response = client.post(
        "/reports/",
        params={
            "titre": "",
            "description": "Description",
            "user_id": user_id,
            "location_id": location_id
        }
    )

    assert response.status_code == 400


def test_lire_reports(client):

    response = client.get("/reports/")

    assert response.status_code == 200

    data = response.json()

    assert "total" in data
    assert "resultats" in data


def test_filtre_statut(client, user_id, location_id):

    client.post(
        "/reports/",
        params={
            "titre": "Test filtre statut",
            "description": "Description",
            "user_id": user_id,
            "location_id": location_id
        }
    )

    response = client.get(
        "/reports/",
        params={"statut": "en cours"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["total"] >= 1


def test_filtre_statut_inexistant(client):

    response = client.get(
        "/reports/",
        params={"statut": "resolu"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["total"] == 0
    assert data["resultats"] == []


def test_tri_du_plus_recent(client, user_id, location_id):

    premier = client.post(
        "/reports/",
        params={
            "titre": "Premier signalement",
            "description": "Description",
            "user_id": user_id,
            "location_id": location_id
        }
    )

    deuxieme = client.post(
        "/reports/",
        params={
            "titre": "Deuxieme signalement",
            "description": "Description",
            "user_id": user_id,
            "location_id": location_id
        }
    )

    response = client.get("/reports/")

    data = response.json()

    premier_resultat = data["resultats"][0]

    assert premier_resultat["id_r"] == deuxieme.json()["id_r"]


def test_supprimer_report(client, user_id, location_id):

    creation = client.post(
        "/reports/",
        params={
            "titre": "A supprimer",
            "description": "Sera supprime",
            "user_id": user_id,
            "location_id": location_id
        }
    )

    report_id = creation.json()["id_r"]

    response = client.delete(f"/reports/{report_id}")

    assert response.status_code == 200


def test_supprimer_report_inexistant(client):

    response = client.delete("/reports/999999")

    assert response.status_code == 400