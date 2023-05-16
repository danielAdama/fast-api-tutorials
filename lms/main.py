from db.setup import engine
from api.models import course, user
from fastapi import FastAPI
from api.routes import users, courses, sections
from fastapi.middleware.cors import CORSMiddleware

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API LMS",
    description="LMS for managing students and courses",
    verion="1.0",
    contact={
        "name":"Daniel Adama",
        "email":"adamadaniel321@gmail.com"
    }
)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)