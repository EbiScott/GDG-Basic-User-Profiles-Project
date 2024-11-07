import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

database_url = os.getenv("POSTGRE_URI")

engine = create_engine(database_url)
SessionLocal = sessionmaker(bind=engine)
