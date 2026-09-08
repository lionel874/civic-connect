import os

os.environ["DATABASE_URL"] = "sqlite:///test_database/test_civic_connect.db"

import pytest
from fastapi.testclient import TestClient

from database import Base, engine
from main import app


Base.metadata.create_all(bind=engine)


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def user_id(client):
    response = client.post(
        "/users/",
        params={
            "nom": "Testeur",
            "prenom": "Auto",
            "email": "testeur.auto@gmail.com",
            "tel": "680000000",
            "role": "user"
        }
    )
    return response.json()["id"]


@pytest.fixture
def location_id(client):
    response = client.post(
        "/localisation/",
        params={
            "ville": "Dschang",
            "quartier": "Foto",
            "adresse": "Rue 1"
        }
    )
    return response.json()["id_l"]

@pytest.fixture
def product_id(client):
    response = client.post(
        "/produit/",
        params={
            "nom": "Produit Test",
            "prix": 1000,
            "quantite": 50
        }
    )
    return response.json()["id_p"]