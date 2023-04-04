import fastapi
from typing import List, Optional, Dict

router = fastapi.APIRouter()

@router.get("/sections/{id}")
async def read_section() -> Dict:
    return {
        "courses":[]
    }

@router.get("/sections/{id}/content-blocks")
async def read_section_content_blocks():
    return {
        "courses":[]
    }

@router.get("/content-blocks/{id}")
async def read_content_blocks():
    return {
        "courses":[]
    }