from REPOSITORIES.order_repository import create_order_repo
from sqlalchemy.orm import Session
from CLASS.users import User
from CLASS.order import Order
from CLASS.product import Product


# logique metier de la commande

def ajout_order( titre, quantite, mte, user_id, product_id,session:Session):
    
      # verification du titre
      if titre is None or isinstance(titre,str):
        raise ValueError("le titre doit etre une chaine")

      # verification de la quantite

      if quantite is None:
        raise ValueError("quantite ne peut pas etre none")
      if not isinstance(quantite,int):
        raise ValueError("quantite doit etre uun entier")
      if quantite < 0:
        raise ValueError("la quantite doit etre superieur a 0")

      # verification du produit
      product= session.get(Product,product_id)

      if product is None:
        raise ValueError("le produit n'existe pas")

      # calcul du montant total
      mte = product.prix_p*quantite



      command = Order(
                    titre_o = titre,
                    quantite_o = quantite,
                    mte= mte,
                    user_id = user_id,
                    product_id =product_id)

      return create_order_repo(session,command)