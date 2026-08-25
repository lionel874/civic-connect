from fastapi import APIRouter
from SERVICES.report_service import (ajout_report_service,
                                     lire_report_service,
                                     identifier_report_service,
                                     supprimer_report_service)


router = APIRouter(
    prefix="/reports",
    tags=["Report"] )



@router.post("/")
def create_report(
    titre: str,
    description: str,
    user_id: int,
    location_id: int,
    
):
    return ajout_report_service(
       
        titre=titre,
        description=description,
        user_id=user_id,
        location_id=location_id,
        
    )

@router.get("/")
def get_report():
    return lire_report_service()

@router.delete("/{report_id}")

def delete_report(report_id:int):
    return supprimer_report_service(report_id)

