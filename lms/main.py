from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import List, Optional, Dict

app = FastAPI(
    title="API LMS",
    description="LMS for managing students and courses",
    verion="1.0",
    contact={
        "name":"Daniel Adama",
        "email":"adamadaniel321@gmail.com"
    }
)

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.post("/users")
async def create_user(user: User) -> Dict:
    users.append(user)
    return {"message": "Success"}

@app.get("/users/{id}")
async def get_user(id: int = Path(
    ..., description = "The ID of the user you want to retrieve."),
    is_active: bool = Query(None)
    ):
    return users[id]