from pydantic import BaseModel
from typing import List, Optional
from  sqlmodel import Field, SQLModel, Session, JSON, Column

class Event(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example":{
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book","launch"],
                "location": "Google Meet"
            }
        }

## For update operations
class EventUpdate(SQLModel):
    title: Optional[str]
    image: Optional[str]
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example":{
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book","launch"],
                "location": "Google Meet"
            }
        }
