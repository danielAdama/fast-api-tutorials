from fastapi import APIRouter, HTTPException,  status
from models.users import User, UserSignIn, NewUser
from typing import Dict

account_router = APIRouter(
    tags = ["Account"]
)
users = {}

@account_router.post("/signup")
async def sign_new_user(data: NewUser) -> Dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists"
        )
    
    # When the user do not exist add
    users[data.email] = data
    return {
        "message": "User successfully registered!"
    }

@account_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> Dict:
    if users[user.email].email not in user.email:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )
    
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credentials passed"
        )
    
    return {
        "message": "User signed in successfully"
    }

