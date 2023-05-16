from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    email: str
    first_name: str
    last_name: str
    password: str
    role: int

class UserCreate(UserBase):
    ...

class User(UserBase):
    id: int
    # is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class TokenBase(BaseModel):
    token_hash: str

class TokenCreate(TokenBase):
    ...

class Token(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class AccessTokenBase(BaseModel):
    access_token: str
    token_type: str

class AccessTokenCreate(TokenBase):
    ...

class AccessToken(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True