from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# CONNECTION_STRING = "postgresql://user:password@postgresserver/db"
CONNECTION_STRING = "postgresql+psycopg2://danny:root@localhost/lms_db"
CONNECTION_ARGS = {
    #"check_same_thread":False
}

engine = create_engine(
    CONNECTION_STRING,
    CONNECTION_ARGS,
    future=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True
    )

Base = declarative_base()

def get_db():
    db=SessionLocal(),
    try:
        yield db
    finally:
        db.close()