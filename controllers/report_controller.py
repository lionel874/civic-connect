from sqlalchemy.orm import Session
from database import engine
from CLASS.report import Report
from CLASS.location import Location
from CLASS.users import User

def ajout_report(id_r, titre, description, user_id, location_id , db_engine = engine):
    with Session(db_engine) as session :

        user = session.get(User,user_id)

        if user is None:

            raise ValueError("utlisateur inexistant")
        
        localisation = session.get(Location,location_id)

        if localisation is None:
            raise ValueError("localisation inexistant")



        #### champ obligatoire
        if not titre:
            raise ValueError("le titre est obligatoire")
        
        if not description:
             raise ValueError("la description est obligatoire")
        
        signalment = Report( id_r = id_r,
                            titre = titre,
                            description = description,
                            user_id = user_id,
                            location_id = location_id)

        session.add(signalment)
        session.commit()

        return signalment