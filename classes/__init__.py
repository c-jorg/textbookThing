#have to import every data type you want to use
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import psycopg2
from flask_marshmallow import Marshmallow 
from .Base import Base, engine, session, Session
from .Date import Date
from .Diagram import Diagram
from .Feature import Feature
from .Image import Image



def init_db():
    Base.metadata.create_all(bind=engine)