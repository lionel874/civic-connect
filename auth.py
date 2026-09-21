from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = "change-moi-en-production"  # à déplacer dans une variable d'environnement plus tard
ALGORITHM = "HS256"
DUREE_TOKEN_MINUTES = 30

security_scheme = HTTPBearer()


def creer_token(user_id: int, role: str) -> str:
    expiration = datetime.utcnow() + timedelta(minutes=DUREE_TOKEN_MINUTES)
    payload = {"sub": str(user_id), "role": role, "exp": expiration}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security_scheme)) -> int:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token invalide")
        return int(user_id)
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalide ou expiré")