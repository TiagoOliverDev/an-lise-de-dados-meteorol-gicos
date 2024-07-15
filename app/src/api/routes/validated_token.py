from fastapi import HTTPException, Header, Depends, Security
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.src.models.models import User
from app.src.repositories.user_repository import UserRepository
from app.src.db.database import get_db

# Configurando o esquema OAuth2 com Password e Bearer (token)
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

SECRET_KEY = "9ba263503b01ce2ef81f6641f504b45333aa0662183d0184db79d9e92ccef620"
ALGORITHM = "HS256"

async def token_required(Authorization: str = Header(None)):
    if Authorization:
        token = Authorization.split(' ')[1]
    else:
        raise HTTPException(status_code=401, detail="Token is missing")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        current_user = payload['email']  
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    return current_user