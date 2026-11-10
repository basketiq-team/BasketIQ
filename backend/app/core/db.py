from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from core.config import get_settings

settings = get_settings()

engine = create_engine(settings.database_url, pool_pre_ping=True)
session = sessionmaker(bind= engine, autoflush=False)

def get_db():
    db = session()
    try :
        yield db
    finally:
        db.close()
