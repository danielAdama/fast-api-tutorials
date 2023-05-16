from fastapi import APIRouter, HTTPException,  status, Depends, Request, Path
from sqlalchemy.orm import Session
from api.repository.users import get_user, get_user_by_email, get_users, create_user
from typing import List, Optional, Dict
from pydantic_schema.users import UserCreate, User, Token
from db.setup import get_db
from dotenv import load_dotenv, find_dotenv
import logging
import os
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from typing import Union, Dict


HANDLE = "appl"
logger = logging.getLogger(HANDLE)
logger.setLevel(level=logging.DEBUG)
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(level=logging.DEBUG)
logger.addHandler(consoleHandler)
load_dotenv(find_dotenv())

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# def verify_password(user_id: int, db: Session):
#     return db.query(User).filter(User.id == user_id).first()

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(password):
    hashed_password = get_password_hash(password)
    return pwd_context.verify(password, hashed_password)

def authenticate_user(email: str, db: Session):
    user = get_user_by_email(email, db)
    if not user:
        user.verified = False
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User do not exist"
        )
    
    if not verify_password(user.password):
        user.verified = False
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect Password"
        )

def create_access_token(data: Dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            # days=
            minutes = 15
        )
    
    to_encode.update(
        {
            "exp": expire
        }
    )
    encoded_jwt = jwt.encode(
        to_encode,
        key = os.environ.get("SECRET_KEY"),
        algorithm = os.environ.get("ALGORITHM")
    )
    return encoded_jwt

# def get_user_by_token(email: str, db: Session):
#     return db.query(User).filter(User.email == email).first()

# async 
def get_current_user(user: UserCreate, db: Session, token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        details = "Could not validate credentials",
        headers = {"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(
            token,
            key = os.environ.get("SECRET_KEY"),
            algorithm = [os.environ.get("ALGORITHM")]
        )

        email: str = payload.get("sub")
        if email is None:
            return None
        
        # Store in db
        create_user(user)
        # Check data type
        token_data = User(
            email = user.email
        )

    except JWTError:
        raise credential_exception
    
    user = get_user_by_email(token_data.email, db)
    if user is None:
        raise credential_exception
    
    return user

# async 
def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.verified:
        raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST,
           detail="Inactive User"
        )
    
    return current_user


router = APIRouter()

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm() = Depends()):
    print(form_data)
    # user = authenticate_user(email, db)


@router.post("/signup", response_model=User, status_code=status.HTTP_201_CREATED)
async def sign_up(
    user: UserCreate,
    db: Session = Depends(get_db)
    ):

    user = get_user_by_email(user.email, db)
    
    
    password = get_password_hash(user.password)


    # if user:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="User already exist"
    #     )
    # return create_user(user, db)

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