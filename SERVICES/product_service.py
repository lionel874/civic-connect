from REPOSITORIES.product_repository import (create_product_repo,
                                             modif_produit_repo,
                                             lire_produit_repository,
                                             supprimer_produit_repository,
                                             identifier_produit_par_id,
                                             patch_product_repository)
from CLASS.product import Product


# logique metier de produit

def ajout_produit_service(nom, prix, quantite):

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

    return create_product_repo(produit)


# modifier produit 


def modif_produit_service(
    product_id,
    nouveau_nom,
    nouveau_prix,
    nouvelle_quantite
):

    if not nouveau_nom:
        raise ValueError("Le nom du produit est obligatoire")

    if nouveau_prix is None:
        raise ValueError("Le prix du produit est obligatoire")

    if nouvelle_quantite is None:
        raise ValueError("La quantité du produit est obligatoire")

    if not isinstance(nouveau_nom, str):
        raise ValueError("Le nom doit être une chaîne de caractères")

    if not isinstance(nouveau_prix, (int, float)):
        raise ValueError("Le prix doit être un nombre")

    if not isinstance(nouvelle_quantite, int):
        raise ValueError("La quantité doit être un entier")

    if nouveau_prix < 0:
        raise ValueError("Le prix ne peut pas être négatif")

    if nouvelle_quantite < 0:
        raise ValueError("La quantité ne peut pas être négative")

    produit = identifier_produit_par_id(product_id)

    if produit is None:
        raise ValueError("Produit introuvable")

    return modif_produit_repo(
        product_id,
        nouveau_nom,
        nouveau_prix,
        nouvelle_quantite
    )


# LIRE UN PRODUIT


def lire_produit_service(product_id: int):

    produit = identifier_produit_par_id(product_id)

    if produit is None:
        raise ValueError("Produit introuvable")

    return produit



# LIRE TOUS LES PRODUITS


def lire_products_service():

    return lire_produit_repository()



# SUPPRIMER UN PRODUIT


def supprimer_product_service(product_id: int):

    resultat = supprimer_produit_repository(product_id)

    if resultat is None:
        raise ValueError("Produit introuvable")

    return resultat 


# modifier partiellement produit

def patch_produit_service(
    product_id,
    nouveau_nom=None,
    nouveau_prix=None,
    nouvelle_quantite=None,
    
    
):
    if nouveau_nom is None and nouveau_prix is None and nouvelle_quantite is None:
        raise ValueError("Aucune donnée à modifier")

    if nouveau_nom is not None and not isinstance(nouveau_nom, str):
        raise ValueError("Le nom doit être une chaîne de caractères")

    if nouveau_prix is not None:
        if not isinstance(nouveau_prix, (int, float)):
            raise ValueError("Le prix doit être un nombre")

        if nouveau_prix < 0:
            raise ValueError("Le prix ne peut pas être négatif")

    if nouvelle_quantite is not None:
        if not isinstance(nouvelle_quantite, int):
            raise ValueError("La quantité doit être un entier")

        if nouvelle_quantite < 0:
            raise ValueError("La quantité ne peut pas être négative")

    produit = identifier_produit_par_id(product_id)

    if produit is None:
        raise ValueError("Produit introuvable")

    return patch_product_repository(
        product_id,
        nouveau_nom,
        nouveau_prix,
        nouvelle_quantite
    )  