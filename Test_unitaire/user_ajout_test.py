from sqlalchemy.orm import Session

from database import Base, engine
from CLASS.users import User
from controllers.user_controller import ajout_user




ajout_user("tsadjio",
           "alexia",
           "alexia@gmail.com",
           "655504063",
           "utilisateur")

# verification dans la base
with Session(engine) as session:
    user = session.query(User).filter_by(email ="alexia@gmail.com").first()
    assert user is not None
    
    assert user.nom == "tsadjio"
    assert user.prenom == "alexia"
    assert user.email == "alexia@gmail.com"
    assert user.tel == "655504063"
    assert user.role == "utilisateur"