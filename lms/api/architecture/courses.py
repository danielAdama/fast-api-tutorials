from sqlalchemy.orm import Session
from api.models.course import Course
from pydantic_schema.course import CourseCreate

def get_course(course_id: int, db: Session):
    return db.query(Course).filter(Course.id == course_id).first()

def get_courses(db: Session):
    return db.query(Course).all()

def create_course(course: CourseCreate, db: Session):
    new_course = Course(
        title = course.title,
        description = course.description,
        user_id = course.user_id
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course