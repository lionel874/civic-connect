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



@router.post("/",summary="Créer une commande" )
def create_order(
    titre: str,
    quantite: int,
    user_id: int,
    product_id: int):

    """
    Crée une nouvelle commande.

    Le montant total (`mte_total`) est calculé automatiquement
    à partir du prix du produit et de la quantité — il ne peut
    pas être fourni ni modifié directement par l'utilisateur.
    """
    return ajout_order(
        titre,
        quantite,
        user_id,
        product_id
        
    )

@router.get("/",summary="Lister les commandes")
def get_order():
  """Retourne la liste de toutes les commandes."""
  return lire_order_service()

@router.get("/{order_id}",summary="Obtenir une commande")
def get_order_by_id(order_id: int):
    """Retourne une commande précise par son identifiant."""
    return lire_order_par_id_service(order_id)


@router.put("/{order_id}",summary="Remplacer une commande")
def update_order(
    order_id: int,
    titre: str,
    quantite: int,
    product_id: int
):
    """
    Remplace entièrement une commande existante.

    """
    return modifier_order_service(
        order_id,
        titre,
        quantite,
        product_id
    )


@router.patch("/{order_id}",summary="Modifier partiellement une commande")
def patch_order(
    order_id: int,
    titre: str | None = None,
    quantite: int | None = None,
    product_id: int | None = None
):
    """
    Modifie un ou plusieurs champs d'une commande existante.

  
    """
    return patch_order_service(
        order_id,
        titre,
        quantite,
        product_id
    )


@router.delete("/{order_id}",summary="Supprimer une commande")
def delete_order(order_id: int):
    """Supprime une commande par son identifiant."""
    return supprimer_order_service(order_id)
