from fastapi import APIRouter
from SERVICES.services_service import (ajout_service,
                                       lire_service_service,
                                       supprimer_service_service)


router = APIRouter(
    prefix= "/service",
    tags=["Service"]
)





@router.post("/")


def create_service_route(nom_s:str,
                   description:str,
                   prix: float,
                   categorie,
                   user_id: int,
                   location_id: int
                   ):
    return ajout_service(
        nom_s,
        description,
        prix,
        categorie,
        user_id,
        location_id,
        
    )

@router.get("/")
def get_service(categorie: str = None,
    mot_cle: str = None,
    zone: str = None,
    page: int = 1,
    limit: int = 10):
  return lire_service_service(categorie, mot_cle, zone, page, limit)

@router.delete("/{service_id}")
def delete_user(service_id:int ):
    return supprimer_service_service(service_id)