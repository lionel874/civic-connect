from sqlalchemy.orm import Session
from CLASS.users import User

from CLASS.service import Service
from REPOSITORIES.service_repository import create_service


def ajout_service(
    nom_s,
    description,
    prix,
    user_id,
    location_id,
    session:Session
):

    # Vérification du nom
    if nom_s is None:
        raise ValueError("Le nom du service ne peut pas être None")

    if not isinstance(nom_s, str):
        raise ValueError("Le nom du service doit être une chaîne")

    if nom_s.strip() == "":
        raise ValueError("Le nom du service ne peut pas être vide")

    # Vérification de la description
    if description is None:
        raise ValueError("La description ne peut pas être None")

    if not isinstance(description, str):
        raise ValueError("La description doit être une chaîne")

    if description.strip() == "":
        raise ValueError("La description ne peut pas être vide")

    # Vérification du prix
    if prix is None:
        raise ValueError("Le prix ne peut pas être None")

    if prix < 0:
        raise ValueError("Le prix ne peut pas être négatif")

    # Vérification de user_id
    if user_id is None:
        raise ValueError("user_id ne peut pas être None")

    # Vérification de location_id
    if location_id is None:
        raise ValueError("location_id ne peut pas être None")

    user = session.get(User, user_id)

    if user is None:
     raise ValueError("L'utilisateur n'existe pas")
    # Création de l'objet Service
    service = Service(
        nom_s=nom_s,
        description=description,
        prix=prix,
        user_id=user_id,
        location_id=location_id
    )

    # Enregistrement via le repository
    return create_service(service, session)