# Standard Imports
from fastapi import Depends
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from datetime import timedelta

from .. import API_PREFIX
from ..utils.helpers import BaseSchema

# Environment Import
from .config import JWT_SECRET
from .config import JWT_EXPIRATION_DAYS

# Database Import
from ..db.engine import get_db
from ..modules.users.models import User


manager = LoginManager(JWT_SECRET, tokenUrl=API_PREFIX+'/auth/token')
route = APIRouter()


# Login Schema
class LoginData(BaseSchema):
    username: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "fulano@sbf.com",
                "password": "mysecretpassword"
            }
        }

@manager.user_loader
def load_user(username: str):
    db = next(get_db())
    user = db.query(User).filter(
        User.email == username
    ).first()
    return user

@route.post('/auth/token', include_in_schema=False)
def auth_token(data: OAuth2PasswordRequestForm = Depends()):
    return login(data)

@route.post('/login')
def login(data: LoginData):
    username = data.username
    password = data.password

    user: User = load_user(username)
    if not user:
        raise InvalidCredentialsException
    elif user.verify_password(password) == False:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data=dict(sub=username),
        expires=timedelta(days=JWT_EXPIRATION_DAYS)
    )
    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'admin': user.admin
    }