from typing import Optional
from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel, EmailStr


class User(Model):
    id = fields.UUIDField(pk=True)
    email = fields.CharField(max_length=255, unique=True, null=True)
    username = fields.CharField(max_length=255, unique=True, null=True)
    fullname = fields.CharField(max_length=255, null=True)
    password = fields.CharField(max_length=255, null=True)
    notification_key = fields.CharField(max_length=500, null=True)
    bio = fields.CharField(max_length=255, default="")
    is_admin = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)


UserModel = pydantic_model_creator(User, name="User")


# request in response out


class AuthIn(BaseModel):
    email: EmailStr
    password: Optional[str]
    username: Optional[str]
    fullname: Optional[str]
    notification_key: Optional[str]
    bio: str = ""


class AuthOut(BaseModel):
    user: UserModel
    token: str
