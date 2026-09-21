from database import SessionLocal
from CLASS.point_connectivite import PointConnectivite
from CLASS.location import Location


def create_point_connectivite_repository(point):
    db = SessionLocal()
    try:
        db.add(point)
        db.commit()
        db.refresh(point)
        return point
    finally:
        db.close()


def lire_point_connectivite_repository(ville: str = None, qualite_reseau: str = None, page: int = 1, limit: int = 10):
    db = SessionLocal()
    try:
        query = db.query(PointConnectivite, Location.ville, Location.quartier).join(
            Location, PointConnectivite.location_id == Location.id_l
        )

        if ville:
            query = query.filter(Location.ville.contains(ville))

        if qualite_reseau:
            query = query.filter(PointConnectivite.qualite_reseau == qualite_reseau)

        total = query.count()
        resultats_bruts = query.offset((page - 1) * limit).limit(limit).all()

        resultats = []
        for point, ville_r, quartier_r in resultats_bruts:
            resultats.append({
                "id_pc": point.id_pc,
                "nom": point.nom,
                "qualite_reseau": point.qualite_reseau,
                "horaires": point.horaires,
                "user_id": point.user_id,
                "ville": ville_r,
                "quartier": quartier_r
            })

        return {
            "total": total,
            "page": page,
            "limit": limit,
            "resultats": resultats
        }
    finally:
        db.close()


def identifier_point_connectivite_par_id(point_id: int):
    db = SessionLocal()
    try:
        return db.get(PointConnectivite, point_id)
    finally:
        db.close()


def supprimer_point_connectivite_repository(point_id: int):
    db = SessionLocal()
    try:
        point = db.get(PointConnectivite, point_id)

        if point is None:
            return None

        db.delete(point)
        db.commit()
        return point
    finally:
        db.close()