def test_creer_utilisateur_valide(client):

    response = client.post(
        "/users/",
        params={
            "nom": "Tsafack",
            "prenom": "Paul",
            "email": "paul.test@gmail.com",
            "tel": "680048703",
            "role": "user"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["nom"] == "Tsafack"
    assert data["prenom"] == "Paul"
    assert data["role"] == "user"


def test_nom_vide(client):

    response = client.post(
        "/users/",
        params={
            "nom": "",
            "prenom": "Paul",
            "email": "paul2@gmail.com",
            "tel": "680048703",
            "role": "user"
        }
    )

    assert response.status_code == 400


def test_prenom_vide(client):

    response = client.post(
        "/users/",
        params={
            "nom": "Tsafack",
            "prenom": "",
            "email": "paul3@gmail.com",
            "tel": "680048703",
            "role": "user"
        }
    )

    assert response.status_code == 400


def test_email_vide(client):

    response = client.post(
        "/users/",
        params={
            "nom": "Tsafack",
            "prenom": "Paul",
            "email": "",
            "tel": "680048703",
            "role": "user"
        }
    )

    assert response.status_code == 400


def test_tel_vide(client):

    response = client.post(
        "/users/",
        params={
            "nom": "Tsafack",
            "prenom": "Paul",
            "email": "paul4@gmail.com",
            "tel": "",
            "role": "user"
        }
    )

    assert response.status_code == 400


def test_nom_contient_des_chiffres(client):

    response = client.post(
        "/users/",
        params={
            "nom": "123",
            "prenom": "Paul",
            "email": "paul5@gmail.com",
            "tel": "680048703",
            "role": "user"
        }
    )

    assert response.status_code == 400


def test_prenom_contient_des_chiffres(client):

    response = client.post(
        "/users/",
        params={
            "nom": "Tsafack",
            "prenom": "456",
            "email": "paul6@gmail.com",
            "tel": "680048703",
            "role": "user"
        }
    )

    assert response.status_code == 400


def test_tel_doit_commencer_par_6(client):

    response = client.post(
        "/users/",
        params={
            "nom": "Tsafack",
            "prenom": "Paul",
            "email": "paul7@gmail.com",
            "tel": "580048703",
            "role": "user"
        }
    )

    assert response.status_code == 400


def test_tel_uniquement_des_chiffres(client):

    response = client.post(
        "/users/",
        params={
            "nom": "Tsafack",
            "prenom": "Paul",
            "email": "paul8@gmail.com",
            "tel": "68004ABCD",
            "role": "user"
        }
    )

    assert response.status_code == 400


def test_email_invalide(client):

    response = client.post(
        "/users/",
        params={
            "nom": "Tsafack",
            "prenom": "Paul",
            "email": "paul-sans-arobase",
            "tel": "680048703",
            "role": "user"
        }
    )

    assert response.status_code == 400


def test_role_admin_refuse(client):

    response = client.post(
        "/users/",
        params={
            "nom": "Tsafack",
            "prenom": "Paul",
            "email": "paul9@gmail.com",
            "tel": "680048703",
            "role": "admin"
        }
    )

    assert response.status_code == 400


def test_role_inconnu_refuse(client):

    response = client.post(
        "/users/",
        params={
            "nom": "Tsafack",
            "prenom": "Paul",
            "email": "paul10@gmail.com",
            "tel": "680048703",
            "role": "policier"
        }
    )

    assert response.status_code == 400


def test_role_provider_accepte(client):

    response = client.post(
        "/users/",
        params={
            "nom": "Tsafack",
            "prenom": "Paul",
            "email": "paul11@gmail.com",
            "tel": "680048703",
            "role": "provider"
        }
    )

    assert response.status_code == 200
    assert response.json()["role"] == "provider"


def test_lire_users(client):

    response = client.get("/users/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_supprimer_user(client):

    creation = client.post(
        "/users/",
        params={
            "nom": "ASupprimer",
            "prenom": "Test",
            "email": "asupprimer@gmail.com",
            "tel": "680048703",
            "role": "user"
        }
    )

    user_id = creation.json()["id"]

    response = client.delete(f"/users/{user_id}")

    assert response.status_code == 200


def test_supprimer_user_inexistant(client):

    response = client.delete("/users/999999")

    assert response.status_code == 400