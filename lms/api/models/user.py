from db.setup import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from api.Enums.enums import Role
from utilities.mixins import BaseEntity


## A 1-to-1 relationship between the user and profile meaning
## a user can only have one profile
class User(BaseEntity, Base):
    __tablename__ = "users"

    email = Column(String(100), unique=True, index=True, nullable=False)
    role = Column(Enum(Role))
    is_active = Column(Boolean, default=False)
    profile = relationship("Profile", back_populates="owner", uselist=False)
    student_courses = relationship("StudentCourse", back_populates="student")
    student_content_blocks = relationship("CompletedContentBlock", back_populates="student")


class Profile(BaseEntity, Base):
    __tablename__="profiles"
    
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    bio = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    ## Relationship of each user to a profile
    owner = relationship("User", back_populates="profile")