from CLASS.point_connectivite import PointConnectivite

from REPOSITORIES.point_connectivite_repository import (
    create_point_connectivite_repository,
    lire_point_connectivite_repository,
    identifier_point_connectivite_par_id,
    supprimer_point_connectivite_repository
)

from REPOSITORIES.user_repository import identifier_user_par_id
from SERVICES.location_service import trouver_ou_creer_localisation


QUALITES_AUTORISEES = ["Bon", "Moyen", "Faible"]


def ajout_point_connectivite_service(
    nom,
    qualite_reseau,
    horaires,
    user_id,
    ville,
    quartier,
):

    if not nom or not isinstance(nom, str):
        raise ValueError("Le nom est obligatoire")

    if qualite_reseau is None or qualite_reseau.strip().capitalize() not in QUALITES_AUTORISEES:
       raise ValueError("Qualité réseau invalide")

    qualite_reseau = qualite_reseau.strip().capitalize()

    if not horaires or not isinstance(horaires, str):
        raise ValueError("Les horaires sont obligatoires")

    user = identifier_user_par_id(user_id)
    if user is None:
        raise ValueError("Utilisateur inexistant")

    if not ville:
        raise ValueError("La ville est obligatoire")

    if not quartier:
        raise ValueError("Le quartier est obligatoire")

    localisation = trouver_ou_creer_localisation(ville, quartier)

    point = PointConnectivite(
        nom=nom,
        qualite_reseau=qualite_reseau,
        horaires=horaires,
        user_id=user_id,
        location_id=localisation.id_l
    )

    return create_point_connectivite_repository(point)


def lire_point_connectivite_service(ville: str = None, qualite_reseau: str = None, page: int = 1, limit: int = 10):
    if limit > 50:
        limit = 50
    if limit < 1:
        limit = 10
    if page < 1:
        page = 1

    return lire_point_connectivite_repository(ville, qualite_reseau, page, limit)


def supprimer_point_connectivite_service(point_id: int):
    point = identifier_point_connectivite_par_id(point_id)

    if point is None:
        raise ValueError("Point de connectivité introuvable")

    return supprimer_point_connectivite_repository(point_id)