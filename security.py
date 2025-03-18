from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import JWTError, jwt
import os

# Գաղտնի բանալին
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# OAuth2PasswordBearer-ը FastAPI-ի համար
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Կոդավորման մոդել
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Ֆունկցիա՝ ստեղծելու JWT
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Պաշտպանված route-ի ստուգում
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid credentials")
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import JWTError, jwt
import os

# Գաղտնի բանալին
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# OAuth2PasswordBearer-ը FastAPI-ի համար
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Կոդավորման մոդել
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Ֆունկցիա՝ ստեղծելու JWT
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Պաշտպանված route-ի ստուգում
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid credentials")

