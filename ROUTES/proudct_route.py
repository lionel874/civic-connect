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



@router.post("/",summary="Créer un produit")

def create_product(nom: str,
                   prix: float,
                   quantite:int,
                   ):
    """Ajoute un nouveau produit au catalogue."""
    return ajout_produit_service(
                   nom,
                   prix,
                   quantite
                   )

@router.get("/",summary="Lister les produits")
def get_products():
    """Retourne la liste de tous les produits disponibles."""
    return lire_products_service()

@router.put("/{product_id}",summary="Remplacer un produit")
def update_product(
    product_id: int,
    nouveau_nom: str,
    nouveau_prix: float,
    nouvelle_quantite: int
):
    """Remplace entièrement les informations d'un produit existant."""
    return modif_produit_service(product_id,
                                 nouveau_nom,
                                 nouveau_prix,
                                 nouvelle_quantite)


@router.delete("/{product_id}",summary="Supprimer un produit")
def delete_product(product_id: int):
  """Supprime un produit du catalogue par son identifiant."""
  return supprimer_product_service(product_id)


@router.patch("/{product_id}",summary="Modifier partiellement un produit")
def patch_produit(
    product_id: int,
    nouveau_nom: str | None = None,
    nouveau_prix: float | None = None,
    nouvelle_quantite: int | None = None,
    
    
):
    """Modifie un ou plusieurs champs d'un produit existant, sans toucher aux autres."""
    return patch_produit_service(
        product_id,
        nouveau_nom,
        nouveau_prix,
        nouvelle_quantite,
        
        
    )
