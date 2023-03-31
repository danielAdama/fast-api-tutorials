from todo import todo_router
from typing import List, Dict, Tuple, Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> Dict:
    return {
        "message":"Hello World"
    }

app.include_router(todo_router)