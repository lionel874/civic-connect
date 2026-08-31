from fastapi import APIRouter, Query
from SERVICES.report_service import (ajout_report_service,
                                     lire_report_service,
                                     identifier_report_service,
                                     supprimer_report_service)


router = APIRouter(
    prefix="/reports",
    tags=["Report"] )



@router.post("/",summary="creer un signalement")
def create_report(
    titre: str,
    description: str,
    user_id: int,
    location_id: int,
    
):
    """Crée un nouveau service proposé par un utilisateur.""" 
    return ajout_report_service(
       
        titre=titre,
        description=description,
        user_id=user_id,
        location_id=location_id,
        
    )



@router.get("/", summary="lister les signalement")
def get_report(type: str = Query(None, description="Filtrer par type de signalement", example="panne"),
    statut: str = Query(None, description="Filtrer par statut", example="en cours"),
    page: int = Query(1, description="Numéro de la page", ge=1),
    limit: int = Query(10, description="Nombre de résultats par page (max 50)", ge=1, le=50)):
    return lire_report_service(type,statut,page,limit)




@router.delete("/{report_id}", summary="supprimer un signalement")

def delete_report(report_id:int):
    """Supprime un service par son identifiant."""
    return supprimer_report_service(report_id)

