from REPOSITORIES.product_repository import (create_product_repo,
                                             modif_produit_repo,
                                             lire_produit_repository,
                                             supprimer_produit_repository,
                                             identifier_produit_par_id)
from CLASS.product import Product
from sqlalchemy.orm import Session

# logique metier de produit

def ajout_produit_service(nom, prix, quantite, session:Session):

    if not nom:
         raise ValueError("le nom est obligatoire")
    if not prix:
        raise ValueError("le prix est obligatoire")
    if not quantite:
        raise ValueError("le quantite est obligatoire")
            
    
    # pour verifier si ls nom est une chaine de caractere
    
    
    if not isinstance(nom, str):
        raise ValueError("Le nom doit être une chaîne de caractères")
    
    if not isinstance(prix, float):
        raise ValueError("Le prix doit être une chaîne de caractères")
    
    if not isinstance(quantite, int):
        raise ValueError("Le quantite doit être une chaîne de caractères")
            
            
    produit = Product(nom_p=nom,
                prix_p = prix,
                quantite_p = quantite)

    return create_product_repo(produit,session)


# modifier produit 

def modif_produit_service(product_id,
    nouveau_nom,
    nouvelle_description,
    nouveau_prix,
    session: Session
):

    if not nouveau_nom:
        raise ValueError("Le nom du produit est obligatoire")

    if not nouvelle_description:
        raise ValueError("La description du produit est obligatoire")

    if nouveau_prix is None:
        raise ValueError("Le prix du produit est obligatoire")

    produit = session.get(Product,session)

    if produit is None:
        raise ValueError("Produit introuvable")
    
    produit.nom_p = nouveau_nom
    produit.description_p = nouvelle_description
    produit.prix = nouveau_prix

    return modif_produit_repo(
        produit,
        session)


# supprimer un produit

def supprimer_product_service(
    product_id: int,
    session: Session
):

    produit = identifier_produit_par_id(
        product_id,
        session
    )

    if produit is None:
        raise ValueError("Produit introuvable")

    return supprimer_produit_repository(
        product_id,
        session)


def lire_products_service(session: Session):

    return lire_produit_repository(session)