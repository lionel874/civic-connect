from sqlalchemy.orm import Session
from CLASS.users import User
from database import engine,Base
from controllers.user_controller import modifier_user



modifier_user(2,"tchoumi",
              "frank",
               "frank@gmail.com",
                "671497911",
                 "vendeur" )
# verification dan la base
with Session(engine) as session:
    user = session.get(User,2)
    assert user is not None
    assert user.nom == "tchoumi"
    assert user.prenom =="frank"
    assert user.email == "frank@gmail.com"
    assert user.tel == "671497911"
    assert user.role == "vendeur"

