from sqlalchemy.orm import Session
from CLASS.order import Order

# creation d'une commande dans la base de donnee

def create_order_repo(session: Session, command:Order):
        session.add(command)
        session.commit()
        session.refresh(command)
        return command