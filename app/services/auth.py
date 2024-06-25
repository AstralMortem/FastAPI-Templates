from uuid import UUID
from ..utils.repositories import AbstractRepository
from ..config import settings
from ..schemas.auth import Credentials, SUser, SUserInsert, Token
from ..utils.exceptions import UserDoesNotExistExeception, IncorrectPassword
from ..utils.auth import verify_password, get_password_hash, create_access_token


class AuthService:
    def __init__(self, repo: type[AbstractRepository]):
        self.repo = repo()

    async def get_user_by_uid(self, uid: UUID) -> SUser:
        user = await self.repo.get_one(uid)
        return SUser.model_validate(user)

    async def login_user(self, credentials: Credentials):
        user = await self.repo.get_one(credentials.email, "email")
        if not user:
            raise UserDoesNotExistExeception
        if not verify_password(credentials.password, user.password):
            raise IncorrectPassword
        return create_access_token({"sub": user.id})

    async def signup_user(self, form: SUserInsert):
        form.password = get_password_hash(form.password)
        user = await self.repo.insert(form.model_dump())
        return SUser.model_validate(user)
