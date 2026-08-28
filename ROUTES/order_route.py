from fastapi import APIRouter
from SERVICES.order_service import (ajout_order,
                                    lire_order_service,
                                    lire_order_par_id_service,
                                    modifier_order_service,
                                    patch_order_service,
                                    supprimer_order_service)


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

@router.get("/{order_id}")
def get_order_by_id(order_id: int):
    return lire_order_par_id_service(order_id)


@router.put("/{order_id}")
def update_order(
    order_id: int,
    titre: str,
    quantite: int,
    product_id: int
):
    return modifier_order_service(
        order_id,
        titre,
        quantite,
        product_id
    )


@router.patch("/{order_id}")
def patch_order(
    order_id: int,
    titre: str | None = None,
    quantite: int | None = None,
    product_id: int | None = None
):
    return patch_order_service(
        order_id,
        titre,
        quantite,
        product_id
    )


@router.delete("/{order_id}")
def delete_order(order_id: int):
    return supprimer_order_service(order_id)
