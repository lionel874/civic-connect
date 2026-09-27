from fastapi import APIRouter, Depends, HTTPException
from auth import get_current_user, get_current_admin, get_current_user_with_role
from SERVICES.order_service import (ajout_order,
                                    lire_order_service,
                                    lire_order_par_id_service,
                                    lire_mes_commandes_service,
                                    modifier_order_service,
                                    patch_order_service,
                                    supprimer_order_service)


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("/", summary="Créer une commande")
def create_order(
    titre: str,
    quantite: int,
    product_id: int,
    user_id: int = Depends(get_current_user),
):
    """
    Crée une nouvelle commande pour l'utilisateur connecté.

    Le montant total (`mte_total`) est calculé automatiquement
    à partir du prix du produit et de la quantité.
    L'utilisateur est déterminé à partir du token de connexion,
    il ne peut pas être choisi manuellement.
    """
    return ajout_order(
        titre,
        quantite,
        user_id,
        product_id
    )


@router.get("/mes-commandes", summary="Lister mes commandes")
def get_mes_commandes(user_id: int = Depends(get_current_user)):
    """Retourne uniquement les commandes de l'utilisateur connecté."""
    return lire_mes_commandes_service(user_id)


@router.get("/", summary="Lister toutes les commandes (admin uniquement)")
def get_order(admin_id: int = Depends(get_current_admin)):
    """Retourne la liste de toutes les commandes. Réservé à l'admin."""
    return lire_order_service()


@router.get("/{order_id}", summary="Obtenir une commande")
def get_order_by_id(
    order_id: int,
    current_user: dict = Depends(get_current_user_with_role)
):
    """Retourne une commande précise, si elle appartient à l'utilisateur ou si admin."""
    order = lire_order_par_id_service(order_id)

    if current_user["role"] != "admin" and order.user_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="Vous ne pouvez consulter que vos propres commandes")

    return order


@router.put("/{order_id}", summary="Remplacer une commande")
def update_order(
    order_id: int,
    titre: str,
    quantite: int,
    product_id: int,
    current_user: dict = Depends(get_current_user_with_role)
):
    """Remplace entièrement une commande existante (propriétaire ou admin)."""
    order = lire_order_par_id_service(order_id)

    if current_user["role"] != "admin" and order.user_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="Vous ne pouvez modifier que vos propres commandes")

    return modifier_order_service(
        order_id,
        titre,
        quantite,
        product_id
    )


@router.patch("/{order_id}", summary="Modifier partiellement une commande")
def patch_order(
    order_id: int,
    titre: str | None = None,
    quantite: int | None = None,
    product_id: int | None = None,
    current_user: dict = Depends(get_current_user_with_role)
):
    """Modifie un ou plusieurs champs d'une commande existante (propriétaire ou admin)."""
    order = lire_order_par_id_service(order_id)

    if current_user["role"] != "admin" and order.user_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="Vous ne pouvez modifier que vos propres commandes")

    return patch_order_service(
        order_id,
        titre,
        quantite,
        product_id
    )


@router.delete("/{order_id}", summary="Supprimer une commande")
def delete_order(
    order_id: int,
    current_user: dict = Depends(get_current_user_with_role)
):
    """Supprime une commande (propriétaire ou admin uniquement)."""
    order = lire_order_par_id_service(order_id)

    if current_user["role"] != "admin" and order.user_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="Vous ne pouvez supprimer que vos propres commandes")

    return supprimer_order_service(order_id)