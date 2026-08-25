from fastapi import APIRouter
from SERVICES.location_service import (ajout_localisation_service,
                                       lire_localisation_service,
                                       supprimer_localisation_service)


router = APIRouter(
    prefix= "/localisation",
    tags=["Location"]
)



@router.post("/")

def create_location(ville: str,
                    quartier:str,
                    adresse: str,
                    ):
    return ajout_localisation_service(ville, quartier, adresse)

@router.get("/")
def get_users():
  return lire_localisation_service()



@router.delete("/{location_id}")
def delete_user(location_id:int):

    return supprimer_localisation_service(location_id)