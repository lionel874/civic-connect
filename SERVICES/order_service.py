from REPOSITORIES.order_repository import (
    create_order_repo,
    lire_order_repository,
    identifier_order_par_id,
    modifier_order_repository,
    patch_order_repository,
    supprimer_order_repository
)

from REPOSITORIES.user_repository import identifier_user_par_id
from REPOSITORIES.product_repository import identifier_produit_par_id

from CLASS.order import Order

# logique métier de la commande

def ajout_order(
    titre,
    quantite,
    user_id,
    product_id
):

    # vérification du titre

    if titre is None or not isinstance(titre, str):
        raise ValueError("Le titre doit être une chaîne")

    if not titre.strip():
        raise ValueError("Le titre est obligatoire")


    # vérification de la quantité

    if quantite is None:
        raise ValueError("La quantité est obligatoire")

    if not isinstance(quantite, int):
        raise ValueError("La quantité doit être un entier")

    if quantite <= 0:
        raise ValueError("La quantité doit être supérieure à 0")


    # vérification de l'utilisateur

    user = identifier_user_par_id(user_id)

    if user is None:
        raise ValueError("L'utilisateur n'existe pas")


    # vérification du produit

    product = identifier_produit_par_id(product_id)

    if product is None:
        raise ValueError("Le produit n'existe pas")


    # calcul du montant total

    mte_total = product.prix_p * quantite


    # création de la commande

    command = Order(
        titre_o=titre,
        quantite_o=quantite,
        mte_total=mte_total,
        user_id=user_id,
        product_id=product_id
    )

    return create_order_repo(command)


# lire toutes les commandes

def lire_order_service():

    return lire_order_repository()


# lire une commande par id
def lire_order_par_id_service(order_id: int):

    order = identifier_order_par_id(order_id)

    if order is None:
        raise ValueError("Commande introuvable")

    return order


# modifier une commande (PUT - remplacement complet)
def modifier_order_service(
    order_id,
    titre,
    quantite,
    product_id
):

    if titre is None or not isinstance(titre, str) or not titre.strip():
        raise ValueError("Le titre est obligatoire")

    if quantite is None or not isinstance(quantite, int) or quantite <= 0:
        raise ValueError("La quantité doit être un entier supérieur à 0")

    order = identifier_order_par_id(order_id)

    if order is None:
        raise ValueError("Commande introuvable")

    product = identifier_produit_par_id(product_id)

    if product is None:
        raise ValueError("Le produit n'existe pas")

    # recalcul automatique du montant total
    mte_total = product.prix_p * quantite

    return modifier_order_repository(
        order_id,
        titre,
        quantite,
        mte_total,
        product_id
    )


# modifier partiellement une commande (PATCH)
def patch_order_service(
    order_id,
    titre=None,
    quantite=None,
    product_id=None
):

    if titre is None and quantite is None and product_id is None:
        raise ValueError("Aucune donnée à modifier")

    order = identifier_order_par_id(order_id)

    if order is None:
        raise ValueError("Commande introuvable")

    if titre is not None and (not isinstance(titre, str) or not titre.strip()):
        raise ValueError("Le titre doit être une chaîne non vide")

    if quantite is not None and (not isinstance(quantite, int) or quantite <= 0):
        raise ValueError("La quantité doit être un entier supérieur à 0")

    # déterminer le produit et la quantité finaux pour le recalcul
    produit_final_id = product_id if product_id is not None else order.product_id
    quantite_finale = quantite if quantite is not None else order.quantite_o

    product = identifier_produit_par_id(produit_final_id)

    if product is None:
        raise ValueError("Le produit n'existe pas")

    mte_total = product.prix_p * quantite_finale

    return patch_order_repository(
        order_id,
        titre,
        quantite,
        mte_total,
        product_id
    )


# supprimer une commande
def supprimer_order_service(order_id: int):

    order = supprimer_order_repository(order_id)

    if order is None:
        raise ValueError("Commande introuvable")

    return order