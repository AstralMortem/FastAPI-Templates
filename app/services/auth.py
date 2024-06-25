import asyncio
from uuid import UUID
from authx import AuthX
from ..utils.repositories import AbstractRepository, UserRepository
from ..config import settings
from ..schemas.auth import SUser


class AuthService:
    def __init__(self, repo: type[AbstractRepository]):
        self.repo = repo()

    async def get_user_by_uid(self, uid: UUID) -> SUser:
        user = await self.repo.get_one(uid)
        return SUser.model_validate(user)


security = AuthX[SUser](config=settings.SECURITY_CONFIG)


@security.set_subject_getter  # type: ignore
def get_user_from_uid(id: str) -> SUser:
    service = AuthService(UserRepository)
    return asyncio.run(service.get_user_by_uid(UUID(id)))
