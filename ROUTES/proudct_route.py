from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from SERVICES.product_service import ajout_produit_service

router = APIRouter(
    prefix= "/produit",
    tags=["Product"]
)


def get_db():
    db = SessionLocal()
    try :
        yield db
    finally:
        db.close()

@router.post("/")

def create_product(nom: str,
                   prix: str,
                   quantite:str,
                   db: Session = Depends(get_db)):
    return ajout_produit_service(nom,
                   prix,
                   quantite,
                   db)