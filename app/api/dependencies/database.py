from app.api.core.config import mysql_settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

# Create MySQL connection URI
mysql_uri = f"mysql://{mysql_settings.MYSQL_USER}:{mysql_settings.MYSQL_PASSWORD}@{mysql_settings.MYSQL_HOST}:{mysql_settings.MYSQL_PORT}/{mysql_settings.MYSQL_DATABASE}"

# Create engine
engine = create_engine(mysql_uri)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for ORM models
Base = declarative_base()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()