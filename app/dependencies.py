from typing import Annotated
from fastapi import Depends
from .services.auth import AuthService
from .utils.repositories import UserRepository


auth_dependency = Annotated[AuthService, Depends(lambda: AuthService(UserRepository))]
