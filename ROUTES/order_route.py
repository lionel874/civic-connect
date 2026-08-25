from fastapi import APIRouter
from SERVICES.order_service import ajout_order,lire_order_service


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)



@router.post("/")
def create_order(
    titre: str,
    quantite: int,
    user_id: int,
    product_id: int):
    
    return ajout_order(
        titre,
        quantite,
        user_id,
        product_id
        
    )

@router.get("/")
def get_order():
  return lire_order_service()
