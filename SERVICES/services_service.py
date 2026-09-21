from CLASS.users import User
from CLASS.service import Service
from REPOSITORIES.service_repository import (create_service,
                                             lire_service_repository,
                                             verifier_user_repository,
                                             supprimer_service_repository,
                                             identifier_service_par_id,
                                             )

from SERVICES.location_service import trouver_ou_creer_localisation
def ajout_service(
    nom_s,
    description,
    prix,
    categorie,
    user_id,
    ville,
    quartier,
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

    # Vérification de la catégorie
    if categorie is None or not isinstance(categorie, str) or categorie.strip() == "":
        raise ValueError("La catégorie est obligatoire")

    # Vérification de ville/quartier
    if not ville:
        raise ValueError("La ville est obligatoire")

    if not quartier:
        raise ValueError("Le quartier est obligatoire")

    user = verifier_user_repository(user_id)

    if user is None:
        raise ValueError("L'utilisateur n'existe pas")

    # Trouver la localisation existante ou en créer une nouvelle
    localisation = trouver_ou_creer_localisation(ville, quartier)

    # Création de l'objet Service
    service = Service(
        nom_s=nom_s,
        description=description,
        prix=prix,
        categorie=categorie,
        user_id=user_id,
        location_id=localisation.id_l
    )

    return create_service(service)


# lire les service

def lire_service_service(categorie: str = None, mot_cle: str = None, zone: str = None, page: int = 1, limit: int = 10):
    return lire_service_repository(categorie, mot_cle, zone, page, limit)



#supprimer service par nom


def supprimer_service_service(service_id:int):

    service = identifier_service_par_id(service_id)

    if service is None:
        raise ValueError("service introuvable")

    return supprimer_service_repository(service_id)
