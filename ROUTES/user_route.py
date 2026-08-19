from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from SERVICES.user_service import ajout_user, modifier_user_service

router = APIRouter(
    prefix= "/users",
    tags=["Users"]
)


def get_db():
    db = SessionLocal()
    try :
        yield db
    finally:
        db.close()


@router.post("/")


def create_user(nom: str,
                prenom: str,
                email: str,
                tel:str,
                role: str,
                db: Session = Depends(get_db)):
    return ajout_user(nom, prenom, email, tel, role, db)


@router.put("/{user_id}")


def update_user(user_id:int,
                nouveau_nom: str,
                nouveau_prenom:str,
                nouveau_email:str,
                nouveau_tel: str,
                nouveau_role: str,
                db: Session = Depends(get_db)):
    return modifier_user_service(
        user_id,
        nouveau_nom,
        nouveau_prenom,
        nouveau_email,
        nouveau_tel,
        nouveau_role,
        db
    )