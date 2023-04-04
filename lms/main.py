from fastapi import FastAPI
from api.routes import users, courses, sections

app = FastAPI(
    title="API LMS",
    description="LMS for managing students and courses",
    verion="1.0",
    contact={
        "name":"Daniel Adama",
        "email":"adamadaniel321@gmail.com"
    }
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)