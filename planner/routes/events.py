from fastapi import APIRouter, HTTPException,  status, Depends, Request
from models.events import Event, EventUpdate
from database.connection import get_session
from sqlalchemy import select
from typing import Dict, List


event_router = APIRouter(
    tags=["Events"]
)
events = []

@event_router.get("/", response_model=List[Event])
async def retrieve_all_events(
    session=Depends(get_session)
    ) -> List[Event]:

    events = session.query(Event).all()
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(
    id: int, 
    session=Depends(get_session)
    ) -> Event:

    event = session.get(Event, id)
    if event:
        return event
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

@event_router.post("/")
async def create_event(
    new_event: Event, 
    session=Depends(get_session)
    ) -> Dict:

    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    return {
        "message": "Event created successfully"
    }

@event_router.delete("/")
async def delete_all_events(id: int) -> Dict:
    events.clear()
    return {
            "message": "Event deleted successfully"
        }

@event_router.delete("/{id}")
async def delete_event(
    id: int,
    session=Depends(get_session)
    ) -> Dict:

    event = session.get(Event, id)
    if event:
        session.delete(event)
        session.commit()

        return {
            "message": "Event deleted successfully"
        }
    
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )

@event_router.put("/{id}", response_model=Event)
async def update_event(
    id: int, 
    new_event: EventUpdate, 
    session=Depends(get_session)
    ) -> Event:

    event = session.get(Event, id)
    if event:
        event_data = new_event.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)
        print(event)
        session.add(event)
        session.commit()
        session.refresh(event)

        return event
    
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )