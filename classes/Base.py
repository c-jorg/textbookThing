# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, scoped_session
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
#from os import eviron
import psycopg2
from flask_marshmallow import Marshmallow 

# Base = declarative_base()
# engine = create_engine("postgresql+psycopg2://postgres:letmein@localhost:3333/textbook_images", echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()


app = Flask(__name__)
CORS(app)
ma = Marshmallow()
ma.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:postgres@localhost:5432/textbook_images"
db = SQLAlchemy(app)