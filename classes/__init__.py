#have to import every data type you want to use
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Decimal, Date, Relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import psycopg2



Base = declarative_base()
engine = create_engine("postgresql+psycopg2://postgres:letmein@localhost:3333/textbook_images", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def init_db():
    
    from .Date import Date
    from .Feature import Feature
    from .Image import Image
    #put class imports above this line
    Base.metadate.create_all(bond=engine)