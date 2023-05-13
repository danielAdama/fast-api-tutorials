from datetime import datetime
from db.setup import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from api.Enums.enums import ContentType
from api.models.user import User
from sqlalchemy_utils import URLType
from utilities.mixins import BaseEntity


class Course(BaseEntity, Base):
    __tablename__ = "courses"

    ## Relationship of each user to a course
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(256), nullable=False)
    description = Column(Text, nullable=True)

    ## Name of the course user
    created_by = relationship("User")
    ## Each course has many sections
    sections = relationship("Section", back_populates="course", uselist=False)
    student_courses = relationship("StudentCourse", back_populates="course")


class Section(BaseEntity, Base):
    __tablename__ = "sections"

    ## Relationship of each course to a section
    course_id = Column(Integer, ForeignKey("courses.id"))
    title = Column(String(256), nullable=False)
    description = Column(Text, nullable=True)

    course = relationship("Course", back_populates="sections")
    content_blocks = relationship("ContentBlock", back_populates="section")
    

class ContentBlock(BaseEntity, Base):
    __tablename__ = "content_blocks"

    title = Column(String(256), nullable=False)
    description = Column(Text, nullable=True)
    type = Column(Enum(ContentType))
    url =  Column(URLType, nullable=True)
    content = Column(Text, nullable=True)
    section_id = Column(Integer, ForeignKey("sections.id"), nullable=False)

    section = relationship("Section", back_populates="content_blocks")
    completed_content_blocks = relationship("CompletedContentBlock", back_populates="content_block")


class StudentCourse(BaseEntity, Base):

    """Students can be assigned to courses
    """

    __tablename__ = "student_courses"
    is_completed = Column(Boolean, nullable=False)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    completed = Column(Boolean, default=False)

    student = relationship(User, back_populates="student_courses")
    course = relationship("Course", back_populates="student_courses")
    

class CompletedContentBlock(BaseEntity, Base):

    """This shows when a student has completed a content block.
    """

    __tablename__ = "completed_content_blocks"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    content_block_id = Column(Integer, ForeignKey("content_blocks.id"), nullable=False)
    url = Column(URLType, nullable=True)
    feedback = Column(Text, nullable=True)
    grade = Column(Integer, default=0)

    student = relationship(User, back_populates="student_content_blocks")
    content_block = relationship(ContentBlock, back_populates="completed_content_blocks")
