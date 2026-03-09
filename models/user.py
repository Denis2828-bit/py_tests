from pydantic import BaseModel
from typing import Optional


class Hair(BaseModel):
    color: str
    type: str


class UserData(BaseModel):
    id: int
    firstName: str
    lastName: str
    email: str
    username: str
    age: int
    gender: str
    image: str


class UsersListResponse(BaseModel):
    users: list[UserData]
    total: int
    skip: int
    limit: int


class LoginResponse(BaseModel):
    accessToken: str
    refreshToken: str
    id: int
    username: str
    email: str
    firstName: str
    lastName: str


class CreateUserResponse(BaseModel):
    id: int
    firstName: str
    lastName: str
    age: int


class UpdateUserResponse(BaseModel):
    id: int
    firstName: str
    lastName: str
