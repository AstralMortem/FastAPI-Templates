from curses.ascii import HT
from fastapi import HTTPException, status

__all__ = ["UserDoesNotExistExeception", "IncorrectPassword"]

UserDoesNotExistExeception = HTTPException(
    status.HTTP_401_UNAUTHORIZED,
    {"message": "User with this email does not exists", "path": "email"},
)

IncorrectPassword = HTTPException(
    status.HTTP_401_UNAUTHORIZED,
    {"message": "Email or Password incorrect", "path": "password"},
)
