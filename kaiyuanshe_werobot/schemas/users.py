from pydantic import BaseModel


class User(BaseModel):
    username: str
    hashed_password: str
    is_superuser: bool | None = None
    created_at: str | None = None
    updated_at: str | None = None
    deleted_at: str | None = None
    is_deleted: bool | None = None
    email: str
    full_name: str | None = None
    avatar: str | None = None
    description: str | None = None


class UserIn(BaseModel):
    username: str
    hashed_password: str
    is_superuser: bool | None = None
    email: str
    full_name: str
    avatar: str | None = None
    description: str | None = None
