from datetime import datetime, timedelta, timezone
from typing import Union
import jwt
from passlib.context import CryptContext
from ..config import settings
from .exceptions import InvalidToken
from ..schemas.auth import Token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.SECRET_ALGORITHM
    )
    return Token(access_token=encoded_jwt)


def decode_access_token(token: str):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.SECRET_ALGORITHM]
        )
        return payload
    except jwt.InvalidTokenError:
        raise InvalidToken


def get_token_sub(token: str) -> str:
    return decode_access_token(token).get("sub")
