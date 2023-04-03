from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from database.connection import conn
from routes.account import account_router
from routes.events import event_router

app = FastAPI()

app.include_router(account_router, prefix="/account")
app.include_router(event_router, prefix="/events")

@app.on_event("startup")
def on_startup():
    conn()

@app.get("/")
async def index():
    return RedirectResponse(url="/events")