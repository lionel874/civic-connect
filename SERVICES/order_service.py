from REPOSITORIES.order_repository import (
    create_order_repo,
    lire_order_repository
)

from REPOSITORIES.user_repository import identifier_user_par_id
from REPOSITORIES.product_repository import identifier_produit_par_id

from CLASS.order import Order

# logique métier de la commande

def ajout_order(
    titre,
    quantite,
    mte_total,
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