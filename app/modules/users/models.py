import sqlalchemy as db

from sqlalchemy.orm import relationship
from passlib.hash import pbkdf2_sha256

from ...db.engine import Base
from ...db.base import BaseMixin


class User(Base, BaseMixin):
    __tablename__ = 'base_users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    

    def hash_password(self) -> None:
        self.password = pbkdf2_sha256.hash(self.password)

    def verify_password(self, password: str) -> bool:
        return pbkdf2_sha256.verify(password, self.password)