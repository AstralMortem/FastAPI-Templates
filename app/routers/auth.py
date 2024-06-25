from typing import Annotated
from fastapi import APIRouter, Depends

from ..schemas.auth import Credentials, SUserInsert
from ..dependencies import auth_dependency

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
async def login_user(
    credentials: Annotated[Credentials, Depends()], auth_dependency: auth_dependency
):
    return await auth_dependency.login_user(credentials)


@router.post("/signup")
async def signup_user(
    signup_form: Annotated[SUserInsert, Depends()], auth_service: auth_dependency
):
    return await auth_service.signup_user(signup_form)
