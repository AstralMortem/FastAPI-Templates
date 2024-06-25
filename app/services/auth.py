import asyncio
from uuid import UUID
from authx import AuthX
from ..utils.repositories import AbstractRepository, UserRepository
from ..config import settings
from ..schemas.auth import Credentials, SUser, SUserInsert, Token
from ..utils.exceptions import UserDoesNotExistExeception, IncorrectPassword
from ..utils.auth import verify_password, get_password_hash

security = AuthX[SUser](config=settings.SECURITY_CONFIG)


class AuthService:
    def __init__(self, repo: type[UserRepository]):
        self.repo = repo()

    async def get_user_by_uid(self, uid: UUID) -> SUser:
        user = await self.repo.get_one(uid)
        return SUser.model_validate(user)

    @staticmethod
    def create_access_token(uid: UUID):
        token = security.create_access_token(uid=str(uid))
        return Token(access_token=token)

    async def login_user(self, credentials: Credentials):
        user = await self.repo.get_one(credentials.email, "email")
        if not user:
            raise UserDoesNotExistExeception
        if not verify_password(credentials.password, user.password):
            raise IncorrectPassword
        return self.create_access_token(user.id)

    async def signup_user(self, form: SUserInsert):
        form.password = get_password_hash(form.password)
        user = await self.repo.insert(form.model_dump())
        return SUser.model_validate(user)


@security.set_subject_getter  # type: ignore
def get_user_from_uid(id: str) -> SUser:
    service = AuthService(UserRepository)
    return asyncio.run(service.get_user_by_uid(UUID(id)))
