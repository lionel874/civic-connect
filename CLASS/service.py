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
