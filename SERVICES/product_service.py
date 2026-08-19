from REPOSITORIES.product_reposotory import create_product_repo
from CLASS.product import Product
from sqlalchemy.orm import Session

# logique metier de produit

def ajout_p(nom, prix, quantite, session:Session):

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