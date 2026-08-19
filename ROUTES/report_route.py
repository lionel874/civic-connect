from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from SERVICES.report_service import ajout_report_service


router = APIRouter(
    prefix="/reports",
    tags=["Report"] )

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_report(
    id_r: int,
    titre: str,
    description: str,
    user_id: int,
    location_id: int,
    session: Session = Depends(get_db)
):
    return ajout_report_service(
        id_r=id_r,
        titre=titre,
        description=description,
        user_id=user_id,
        location_id=location_id,
        session=session
    )