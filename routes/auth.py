from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist
from models import AuthOut, AuthIn, UserModel, User
from utils.encrypt import verify_password, hash_password
from utils.token import create_token

router = APIRouter(prefix="/auth")


@router.post("/", response_model=AuthOut)
async def auth(data: AuthIn):
    if data.password is None:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="provider login is not implemented")

    try:
        user = await UserModel.from_queryset_single(User.get(email=data.email))
        if not verify_password(data.password, user.password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="wrong password")
        return {"token": create_token({"email": data.email, "username": user.username}), "user": user}
    except DoesNotExist:
        pass

    if data.username is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="username required")
    data.password = hash_password(data.password)
    user = await User.create(**dict(data))
    return {"token": create_token({"email": data.email, "username": user.username}), "user": user}
