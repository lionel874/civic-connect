from fastapi import APIRouter, Query
from SERVICES.services_service import (ajout_service,
                                       lire_service_service,
                                       supprimer_service_service)


router = APIRouter(
    prefix= "/services",
    tags=["Service"]
)





@router.post("/",summary="Créer un service")
def create_service_route(nom_s:str,
                   description:str,
                   prix: float,
                   categorie,
                   user_id: int,
                   location_id: int
                   ):
    """Crée un nouveau service proposé par un utilisateur."""    
    return ajout_service(
        nom_s,
        description,
        prix,
        categorie,
        user_id,
        location_id,
        
    )

@router.get("/", summary="Lister les services")
def get_service(
     categorie: str = Query(None, description="Filtrer par catégorie exacte du service", example="Ménage"),
     mot_cle: str = Query(None, description="Recherche partielle dans le nom ou la description", example="plombier"),
     zone: str = Query(None, description="Recherche partielle sur la ville ou le quartier", example="Bafoussam"),
     page: int = Query(1, description="Numéro de la page", ge=1),
     limit: int = Query(10, description="Nombre de résultats par page (max 50)", ge=1, le=50)
    ):
  return lire_service_service(categorie, mot_cle, zone, page, limit)
"""
    Retourne la liste des services disponibles.

    Les filtres se combinent en **OU** : un service correspondant
    à au moins un des critères fournis est retourné.
    """
@router.delete("/{service_id}",summary="Supprimer un service")
def delete_user(service_id:int ):
    """Supprime un service par son identifiant."""
    return supprimer_service_service(service_id)