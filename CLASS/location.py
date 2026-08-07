class Location:
    def __init__(self, ville , quartier, adresse):
        self.ville = ville
        self.quartier = quartier
        self.adresse = adresse
    def affichage_location(self):
        print("ville :", self.ville ,"quartier :",self.quartier,"adresse :",self.adresse )
