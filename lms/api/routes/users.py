from fastapi import APIRouter, HTTPException,  status, Depends, Request, Path
from sqlalchemy.orm import Session
from api.architecture.users import get_user, get_user_by_email, get_users, create_user
from typing import List, Optional, Dict
from pydantic_schema.users import UserCreate, User
from db.setup import get_db

router = APIRouter()

@router.get("/users", response_model=List[User])
async def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
    ):

    users = get_users(db, skip=skip, limit=limit)
    return users

@router.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_new_user(
    user: UserCreate, 
    db: Session = Depends(get_db)
    ):

    user = get_user_by_email(user.email, db)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exist"
        )
    return create_user(user, db)

@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int = Path(
    ..., description = "The ID of the user you want to retrieve."),
    db: Session = Depends(get_db)
    ):

    user = get_user(user_id, db)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User do not exist"
        )
    
    return user