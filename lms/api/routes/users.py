import fastapi
from fastapi import Path, Query
from pydantic import BaseModel
from typing import List, Optional, Dict

router = fastapi.APIRouter()

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@router.get("/users", response_model=List[User])
async def get_users():
    return users

@router.post("/users")
async def create_user(user: User) -> Dict:
    users.append(user)
    return {"message": "Success"}

@router.get("/users/{id}")
async def get_user(id: int = Path(
    ..., description = "The ID of the user you want to retrieve."),
    is_active: bool = Query(None)
    ):
    return users[id]