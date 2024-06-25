from curses.ascii import HT
from fastapi import HTTPException, status
from jwt import InvalidTokenError

__all__ = ["UserDoesNotExistExeception", "IncorrectPassword", "InvalidToken"]

UserDoesNotExistExeception = HTTPException(
    status.HTTP_401_UNAUTHORIZED,
    {"message": "User with this email does not exists", "path": "email"},
)

IncorrectPassword = HTTPException(
    status.HTTP_401_UNAUTHORIZED,
    {"message": "Email or Password incorrect", "path": "password"},
)

InvalidToken = HTTPException(status.HTTP_403_FORBIDDEN, {"message": "Invalid token"})
