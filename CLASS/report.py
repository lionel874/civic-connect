class Report:
    def __init__(self,titre,description_r, user_id,location_id):
        self.titre = titre
        self.description_r = description_r
        self.user_id = user_id
        self.location_id =location_id

    def afiichage_report(self):
        print("titre :",self.titre , "description :",self.description_r,
              "id_user",self.user_id, "localisation",self.location_id)
        