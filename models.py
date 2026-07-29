class User:
    def __init__(self,id_u,nom,prenom,email,tel,role):
        self.id_u = id_u
        self.nom =nom
        self.prenom =prenom
        self.email = email
        self.tel = tel
        self.role = role

    def afficher(self):
        print("id :", self.id_u, "nom :" , self.nom ,"prenom :",self.prenom , "email :", self.email,
              "tel:", self.tel,
              "role :", self.role)



class Order:
    def __init__(self,num_order, nom_order,quantite,montant_total,user_id,product_id,statut):
        self.num_order = num_order
        self.nom_order = nom_order
        self.quantite = quantite
        self.montant_total = montant_total
        self.user_id = user_id
        self.product_id = product_id
        self.statut = statut

    def afiichage_order(self):
        print("numero_commander :",self.num_order,"nom_commande :",self.nom_order,
              "quantite", self.quantite,"montant :", self.montant_total , "id_user :",self.user_id,
              "id_produit :",self.product_id, "statut_cmd :",self.statut)


class Product:
    def __init__(self,id_p,nom_p,prix_p,quantite_p):
        self.id_p =id_p
        self.nom_p = nom_p
        self.prix_p = prix_p
        self.quantite_p = quantite_p

    def affichage_product(self):
        print("identifiant_produit :",self.id_p ,"nom_produit:",self.nom_p, "prix :",self.prix,
              "quantite :",self.quantite_p)


class Service:
    def __init__(self,id_s,nom_s,description,prix_s, location_id):
        self.id_s = id_s
        self.nom_s =nom_s
        self.description = description
        self.prix_s = prix_s
        self.location_id =location_id

    def affichage_service(self):
        print("identifiant_s :", self.id_s, "nom servive :",self.nom_s,
              "description :",self.description, "prix_service :",self.prix_s,"localisation :",self.location_id)


class Location:
    def __init__(self, ville , quartier, adresse):
        self.ville = ville
        self.quartier = quartier
        self.adresse = adresse
    def affichage_location(self):
        print("ville :", self.ville ,"quartier :",self.quartier,"adresse :",self.adresse )


class Report:
    def __init__(self,titre,description_r, user_id,location_id):
        self.titre = titre
        self.description_r = description_r
        self.user_id = user_id
        self.location_id =location_id

    def afiichage_report(self):
        print("titre :",self.titre , "description :",self.description_r,
              "id_user",self.user_id, "localisation",self.location_id)
        