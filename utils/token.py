from jose import jwt, JWTError
from jose.constants import ALGORITHMS
import os

secret_key = os.getenv("SECRET_KEY")


def create_token(data: dict):
    data_copy = data.copy()
    encoded_jwt = jwt.encode(data_copy,secret_key,ALGORITHMS.HS256)
    return encoded_jwt


def verify_token(token: str, credential_exception: Exception):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[ALGORITHMS.HS256])
        if payload.get("email") is None:
            raise credential_exception
        return payload
    except JWTError:
        raise credential_exception


