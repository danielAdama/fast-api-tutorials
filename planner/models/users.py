from pydantic import BaseModel, EmailStr
from typing import List, Optional, Union
from models.events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    username: str
    events: Optional[Union[List[Event], None]]

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "username":"danny",
                "events": []
            }
        }

class NewUser(User):
    password: str

class UserSignIn(BaseModel):
    email: EmailStr
    password: str 
    
    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": []
            }
        }