from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from .mixins import BaseTable


class User(SQLAlchemyBaseUserTableUUID, BaseTable):
    pass
