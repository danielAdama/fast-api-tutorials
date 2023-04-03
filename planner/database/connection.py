from  sqlmodel import Field, SQLModel, Session, create_engine
from models.events import Event
import os


dbPath = os.path.join(os.getcwd(),"planner.sqlite3")
connection_string = f'sqlite:///{dbPath}'
connect_args = {"check_same_thread": False}
engine_url = create_engine(
    connection_string, 
    echo=True, 
    connect_args=connect_args
)

def conn():
    SQLModel.metadata.create_all(engine_url)

def get_session():
    with Session(engine_url) as session:
        yield session