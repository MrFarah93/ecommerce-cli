# ecommerce/utils/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Database setup
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
