from sqlalchemy.orm import Session
# from api.models.user import User
from pydantic_schema.users import UserCreate, User

def get_user(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(user: UserCreate, db: Session):
    new_user = User(
        email = user.email,
        role = user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user