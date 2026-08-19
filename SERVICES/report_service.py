from REPOSITORIES.report_repospitory import create_report_repository
from sqlalchemy.orm import Session
from CLASS.location import Location
from CLASS.report import Report
from CLASS.users import User

# logique metier de signalement
def ajout_report_service(id_r, 
                         titre, 
                         description, 
                         user_id, 
                         location_id , 
                         session:Session):

    # verification du titre
          if titre is None or isinstance(titre,str):
            raise ValueError("le titre doit etre une chaine")
    # verification du titre
          if description is None or isinstance(titre,str):
                  raise ValueError("le description doit etre une chaine")


    # verifcation de user

          user = session.get(User,user_id)
          if user is None:
            raise ValueError("utlisateur inexistant") 
          
    # verification de location 

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

          return create_report_repository(signalment, session)