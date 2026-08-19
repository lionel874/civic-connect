from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from SERVICES.order_service import ajout_order


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_order(
    titre: str,
    quantite: int,
    user_id: int,
    product_id: int,
    session: Session = Depends(get_db)
):
    return ajout_order(
        titre=titre,
        quantite=quantite,
        user_id=user_id,
        product_id=product_id,
        session=session
    )