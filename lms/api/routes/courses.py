import fastapi
from typing import List, Optional, Dict

router = fastapi.APIRouter()

@router.get("/courses")
async def read_courses() -> Dict:
    return {
        "courses":[]
    }

@router.post("/courses")
async def create_course() -> Dict:
    return {
        "courses":[]
    }

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