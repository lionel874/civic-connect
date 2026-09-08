def test_creer_commande_valide(client, user_id, product_id):

    response = client.post(
        "/orders/",
        params={
            "titre": "Commande PC",
            "quantite": 2,
            "user_id": user_id,
            "product_id": product_id
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["titre_o"] == "Commande PC"
    assert data["quantite_o"] == 2
    assert data["mte_total"] == 2000


def test_montant_total_calcule_automatiquement(client, user_id, product_id):

    response = client.post(
        "/orders/",
        params={
            "titre": "Commande test calcul",
            "quantite": 5,
            "user_id": user_id,
            "product_id": product_id
        }
    )

    data = response.json()

    assert data["mte_total"] == 5000


def test_quantite_negative(client, user_id, product_id):

    response = client.post(
        "/orders/",
        params={
            "titre": "Commande invalide",
            "quantite": -1,
            "user_id": user_id,
            "product_id": product_id
        }
    )

    assert response.status_code == 400


def test_produit_inexistant(client, user_id):

    response = client.post(
        "/orders/",
        params={
            "titre": "Commande invalide",
            "quantite": 2,
            "user_id": user_id,
            "product_id": 999999
        }
    )

    assert response.status_code == 400


def test_lire_commande_par_id(client, user_id, product_id):

    creation = client.post(
        "/orders/",
        params={
            "titre": "Commande a lire",
            "quantite": 1,
            "user_id": user_id,
            "product_id": product_id
        }
    )

    order_id = creation.json()["num_o"]

    response = client.get(f"/orders/{order_id}")

    assert response.status_code == 200
    assert response.json()["num_o"] == order_id


def test_lire_commande_inexistante(client):

    response = client.get("/orders/999999")

    assert response.status_code == 400


def test_modifier_commande_recalcule_montant(client, user_id, product_id):

    creation = client.post(
        "/orders/",
        params={
            "titre": "Commande a modifier",
            "quantite": 1,
            "user_id": user_id,
            "product_id": product_id
        }
    )

    order_id = creation.json()["num_o"]

    response = client.put(
        f"/orders/{order_id}",
        params={
            "titre": "Commande modifiee",
            "quantite": 3,
            "product_id": product_id
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["quantite_o"] == 3
    assert data["mte_total"] == 3000


def test_patch_quantite_seule(client, user_id, product_id):

    creation = client.post(
        "/orders/",
        params={
            "titre": "Commande a patcher",
            "quantite": 1,
            "user_id": user_id,
            "product_id": product_id
        }
    )

    order_id = creation.json()["num_o"]

    response = client.patch(
        f"/orders/{order_id}",
        params={"quantite": 4}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["quantite_o"] == 4
    assert data["mte_total"] == 4000


def test_supprimer_commande(client, user_id, product_id):

    creation = client.post(
        "/orders/",
        params={
            "titre": "A supprimer",
            "quantite": 1,
            "user_id": user_id,
            "product_id": product_id
        }
    )

    order_id = creation.json()["num_o"]

    response = client.delete(f"/orders/{order_id}")

    assert response.status_code == 200


def test_supprimer_commande_inexistante(client):

    response = client.delete("/orders/999999")

    assert response.status_code == 400