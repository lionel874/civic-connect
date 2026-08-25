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
                   user_id: int,
                   location_id: int
                   ):
    return ajout_service(
        nom_s,
        description,
        prix,
        user_id,
        location_id,
        
    )

@router.get("/")
def get_users():
  return lire_service_service()

@router.delete("/{service_id}")
def delete_user(service_id:int ):
    return supprimer_service_service(service_id)