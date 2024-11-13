from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import psycopg2
from flask_marshmallow import Marshmallow 

Base = declarative_base()
engine = create_engine("postgresql+psycopg2://postgres:letmein@localhost:3333/textbook_images", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
