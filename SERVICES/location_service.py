from REPOSITORIES.location_repository import (create_location_repository,
                                              lire_localisation_repository)
from CLASS.location import Location
from sqlalchemy.orm import Session

def ajout_localisation_service( ville, quartier, adresse, session:Session):
    
        if not ville:
            raise ValueError(" la ville est obligatoire")
                
        if not quartier:
            raise ValueError("Le quartier est obligatoire")
        
        if not adresse:
          raise ValueError(" adresse la est obligatoire")
        

        # test pour verifier si le type est respeccter
        if not isinstance(ville, str):
           raise ValueError("Le nom doit être une chaîne de caractères")

        if not isinstance(quartier, str):
                 raise ValueError("Le quartier doit être une chaîne de caractères")
        if not isinstance(adresse, str):
                 raise ValueError("L'adresse doit être une chaîne de caractères")
        
        localisation = Location(
                                        ville = ville,
                                        quartier = quartier,
                                        adresse = adresse
                                        )
        return create_location_repository(localisation,session)

# lire toute les localisation

def lire_localisation_service(session:Session):
   return lire_localisation_repository (session)



        