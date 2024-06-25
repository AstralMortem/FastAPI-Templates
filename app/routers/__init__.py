from fastapi import APIRouter
from .auth import router as r_auth


routers_list: list[APIRouter] = [
    r_auth,
]
