from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_url = "postgresql://postgres:postgres@localhost/BasicUserProfile"

engine = create_engine(database_url)
SessionLocal = sessionmaker(bind=engine)
