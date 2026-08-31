from fastapi import APIRouter
from SERVICES.location_service import (ajout_localisation_service,
                                       lire_localisation_service,
                                       supprimer_localisation_service)


router = APIRouter(
    prefix= "/localisation",
    tags=["Location"]
)



@router.post("/", summary="creer un localisation")

def create_location(ville: str,
                    quartier:str,
                    adresse: str,
                    ):
    """Crée une nouvelle localisation"""
    return ajout_localisation_service(ville, quartier, adresse)

@router.get("/",summary="liste des localisation")
def get_users():
  """liste des localisation"""
  return lire_localisation_service()



@router.delete("/{location_id}",summary="supprimer une localisation")
def delete_user(location_id:int):
    """ supprimer une localisation"""
    return supprimer_localisation_service(location_id)