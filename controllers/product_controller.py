from sqlalchemy.orm import Session
from CLASS.product import Product
from database import engine

def ajoute_p(nom, prix, quantite,db_engine=engine):
    with Session(db_engine) as session:

        if not nom:
            raise ValueError("le nom est obligatoire")
        if not prix:
            raise ValueError("le prix est obligatoire")
        if not quantite:
            raise ValueError("le quantite est obligatoire")
        

        # pour verifier si ls nom est une chaine de caractere


        if not isinstance(nom, str):
             raise ValueError("Le nom doit être une chaîne de caractères")

        if not isinstance(prix, str):
            raise ValueError("Le prix doit être une chaîne de caractères")

        if not isinstance(quantite, str):
             raise ValueError("Le quantite doit être une chaîne de caractères")
        
        
        produit = Product(nom_p=nom,
                          prix_p = prix,
                          quantite_p = quantite)

        session.add(produit)
        session.commit()

        
        return produit


        
        

def modifier_produit( nouveau_prix,nouvelle_qte):
    with Session(engine) as session:
        produit = session.get(Product)
        if produit is None:
            print("produit introuvable")
            return
        produit.prix_p = nouveau_prix
        produit.quantite_p = nouvelle_qte

        session.commit()