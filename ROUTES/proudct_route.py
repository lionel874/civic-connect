from fastapi import APIRouter
from SERVICES.product_service import (ajout_produit_service,
                                      modif_produit_service,
                                      lire_products_service,
                                      supprimer_product_service,
                                      patch_produit_service)

router = APIRouter(
    prefix= "/produit",
    tags=["Product"]
)



@router.post("/")

def create_product(nom: str,
                   prix: float,
                   quantite:int,
                   ):
    return ajout_produit_service(
                   nom,
                   prix,
                   quantite
                   )

@router.get("/")
def get_products():

    return lire_products_service()

@router.put("/{product_id}")
def update_product(
    product_id: int,
    nouveau_nom: str,
    nouveau_prix: float,
    nouvelle_quantite: int
):
    return modif_produit_service(product_id,
                                 nouveau_nom,
                                 nouveau_prix,
                                 nouvelle_quantite)


@router.delete("/{product_id}")
def delete_product(product_id: int):
  return supprimer_product_service(product_id)


@router.patch("/{product_id}")
def patch_produit(
    product_id: int,
    nouveau_nom: str | None = None,
    nouveau_prix: float | None = None,
    nouvelle_quantite: int | None = None,
    
    
):
    return patch_produit_service(
        product_id,
        nouveau_nom,
        nouveau_prix,
        nouvelle_quantite,
        
        
    )
