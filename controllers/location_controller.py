from sqlalchemy.orm import Session
from CLASS.location import Location
from database import engine

def ajout_localisation( ville, quartier, adresse, longitude,latitude,db_engine=engine):
    with Session(db_engine) as session:
        if not ville:
            raise ValueError(" la ville est obligatoire")
                
        if not quartier:
            raise ValueError("Le quartier est obligatoire")
        
        if not adresse:
          raise ValueError(" adresse la est obligatoire")
        if not longitude:
            raise ValueError("la longitude est obligatoire")
        if not latitude:
            raise ValueError("la latitude est obligatoire")

        # test pour verifier si le type est respeccter
        if not isinstance(ville, str):
           raise ValueError("Le nom doit être une chaîne de caractères")

        if not isinstance(quartier, str):
                 raise ValueError("Le quartier doit être une chaîne de caractères")
        if not isinstance(adresse, str):
                 raise ValueError("L'adresse doit être une chaîne de caractères")
        if not isinstance(longitude, str):
                raise ValueError("Le longitude doit être une chaîne de caractères")
        if not isinstance(latitude, str):
                   raise ValueError("Le latitude doit être une chaîne de caractères")
                
                
                
         
        localisation = Location(
                                ville = ville,
                                quartier = quartier,
                                adresse = adresse,
                                longitude = longitude,
                                latitude = latitude)

        session.add(localisation)
        session.commit()


        return localisation