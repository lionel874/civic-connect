from sqlalchemy.orm import Session
from CLASS.product import Product

# creation 1 produit dans la bd

def create_product_repo(produit:Product, session:Session):
    
        session.add(produit)
        session.commit()
        session.refresh(produit)
        return produit

# modification de produit dans la bd

def modif_produit_repo(produit:Product, session:Session):
    
        product= session.get(Product,produit.prix)
        if product is None:
            return None
        product.prix_p = produit.prix
        product.quantite_p = produit.quantite
        product.nom_p = produit.nom_p

        session.commit()
        session.refresh(product)

        return product
