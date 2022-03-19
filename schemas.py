from pydantic import BaseModel
from typing import Optional
from decouple import config

CSRF_KEY = config("CSRF_KEY")


class CsrfSettings(BaseModel):
    secret_key: str = CSRF_KEY


# responseの際の型定義
class Todo(BaseModel):
    id: str
    title: str
    description: str


# requestの際の型定義
class TodoBody(BaseModel):
    title: str
    description: str


class SuccessMsg(BaseModel):
    message: str


# クライアントから送られてくるデータの型定義
class UserBody(BaseModel):
    email: str
    password: str


# response用のデータの型定義
class UserInfo(BaseModel):
    id: Optional[str] = None
    email: str


class Csrf(BaseModel):
    csrf_token: str
