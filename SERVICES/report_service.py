from CLASS.report import Report

from REPOSITORIES.report_repository import (
    create_report_repository,
    lire_report_repository,
    identifier_report_par_id,
    modifier_report_repository,
    supprimer_report_repository
)

from REPOSITORIES.user_repository import (
    identifier_user_par_id
)

from REPOSITORIES.location_repository import (
    identifier_localisation_par_id
)


# logique métier de signalement

def ajout_report_service(
    
    titre,
    description,
    user_id,
    location_id
):

    # Vérification du titre
    if titre is None or not isinstance(titre, str):
        raise ValueError("Le titre doit être une chaîne")

    if not titre.strip():
        raise ValueError("Le titre est obligatoire")

    # Vérification de la description
    if description is None or not isinstance(description, str):
        raise ValueError("La description doit être une chaîne")

    if not description.strip():
        raise ValueError("La description est obligatoire")

    # Vérification de user
    user = identifier_user_par_id(user_id)

    if user is None:
        raise ValueError("Utilisateur inexistant")

    # Vérification de location
    localisation = identifier_localisation_par_id(location_id)

    if localisation is None:
        raise ValueError("Localisation inexistante")

    # Création du signalement
    signalement = Report(
        titre=titre,
        description=description,
        user_id=user_id,
        location_id=location_id,
        type="panne",
        statut="en cours"
    )

    return create_report_repository(signalement)


# Lire tous les signalements

def lire_report_service(type: str = None, 
                        statut: str = None,
                          page: int = 1, 
                          limit: int = 10):
    # Sécurité : empêcher une pagination abusive
    if limit > 50:
        limit = 50

    if limit < 1:
        limit = 10

    if page < 1:
        page = 1
    return lire_report_repository(type,statut,page,limit)


# Identifier un signalement par ID

def identifier_report_service(report_id: int):

    report = identifier_report_par_id(report_id)

    if report is None:
        raise ValueError("Report introuvable")

    return report


# Modifier un signalement

def modifier_report_service(
    report_id,
    nouveau_titre,
    nouvelle_description
):

    # Vérification du titre
    if nouveau_titre is None or not isinstance(nouveau_titre, str):
        raise ValueError("Le titre doit être une chaîne")

    if not nouveau_titre.strip():
        raise ValueError("Le titre est obligatoire")

    # Vérification de la description
    if nouvelle_description is None or not isinstance(
        nouvelle_description, str
    ):
        raise ValueError(
            "La description doit être une chaîne"
        )

    if not nouvelle_description.strip():
        raise ValueError(
            "La description est obligatoire"
        )

    # Vérifier si le report existe
    report = identifier_report_par_id(report_id)

    if report is None:
        raise ValueError("Report introuvable")

    return modifier_report_repository(
        report_id,
        nouveau_titre,
        nouvelle_description
    )


# Supprimer un signalement

def supprimer_report_service(report_id: int):

    report = identifier_report_par_id(report_id)

    if report is None:
        raise ValueError("Report introuvable")

    return supprimer_report_repository(report_id)