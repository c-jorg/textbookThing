#have to import every data type you want to use
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, scoped_session
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask_marshmallow import Marshmallow 
#from .Base import Base, engine, session, Session
from .Base import db, app, ma
from .Date import Date, DateSchema
from .Diagram import Diagram, DiagramSchema
from .Feature import Feature, FeatureSchema
from .Image import Image, ImageSchema
from .Everything import Everything, EverythingSchema



# def init_db():
#     Base.metadata.create_all(bind=engine)

__all__ = [
    'Date',
    'Diagram',
    'Feature',
    'Image',
    'Everything',
    'DateSchema',
    'DiagramSchema',
    'FeatureSchema',
    'ImageSchema',
    'EverythingSchema',
    'db',
    'app'
]