from fastapi import FastAPI
from routes.account import account_router
from routes.events import event_router

app = FastAPI()

app.include_router(account_router, prefix="/account")
app.include_router(event_router, prefix="/events")