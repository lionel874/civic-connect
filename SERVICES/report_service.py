from REPOSITORIES.report_repository import create_report_repository
from sqlalchemy.orm import Session
from CLASS.location import Location
from CLASS.report import Report
from CLASS.users import User
from REPOSITORIES.report_repository import(
    identifier_report_par_id,
    lire_report_repository,
    supprimer_report_repository
)


# logique metier de signalement
def ajout_report_service(id_r, 
                         titre, 
                         description, 
                         user_id, 
                         location_id , 
                         session:Session):

    # verification du titre
          if titre is None or not isinstance(titre,str):
            raise ValueError("le titre doit etre une chaine")
    # verification du titre
          if description is None or not isinstance(titre,str):
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

# lire les signalement

def lire_report_service(session: Session):

    return lire_report_repository(session)

# identifier un signalement
def identifier_report_service(
    report_id: int,
    session: Session
):

    report = identifier_report_par_id(
        report_id,
        session
    )

    if report is None:
        raise ValueError("Report introuvable")

    return report


def supprimer_report_service(
    report_id: int,
    session: Session
):

    report = identifier_report_par_id(
        report_id,
        session
    )

    if report is None:
        raise ValueError("Report introuvable")

    return supprimer_report_repository(
        report_id,
        session
    )