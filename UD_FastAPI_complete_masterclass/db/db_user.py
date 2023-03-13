from sqlalchemy.orm.session import Session
from fastapi import Depends
from .database import get_db
from .models import DBUser
from ..schemas import UserBase


def create_user(db: Session, request: UserBase):
    new_user = DBUser(
        request.username,
        request.email,
        request.password
    )