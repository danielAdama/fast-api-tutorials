from fastapi import APIRouter, HTTPException,  status, Depends, Request, Path
from sqlalchemy.orm import Session
from typing import List, Optional, Dict
from sqlalchemy.orm import Session
from api.repository.courses import get_course, get_courses, create_course
from db.setup import get_db
from pydantic_schema.course import Course, CourseCreate

router = APIRouter()

@router.get("/courses", response_model=List[Course])
async def read_courses(
    db: Session = Depends(get_db)
    ):

    courses = get_courses(db)
    return courses

@router.post("/courses", response_model=Course)
async def create_new_course(
    course: CourseCreate, 
    db: Session = Depends(get_db)
    ):

    # user = get_user_by_email(user.email, db)
    # if user:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="User already exist"
    #     )
    return create_course(course, db)

@router.get("/courses/{id}")
async def read_course() -> Dict:
    return {
        "courses":[]
    }

@router.patch("/courses/{id}")
async def update_courses() -> Dict:
    return {
        "courses":[]
    }

@router.delete("/courses/{id}")
async def delete_courses() -> Dict:
    return {
        "courses":[]
    }

@router.get("/courses/{id}/sections")
async def read_course_sections() -> Dict:
    return {
        "courses":[]
    }