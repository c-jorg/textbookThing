# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, scoped_session
import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#new version using flask, pretty much the same but the session variable is in db like db.session
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:letmein@localhost:3333/textbook_images"
db = SQLAlchemy(app)

#this is the old version not using flask
# Base = declarative_base()
# engine = create_engine("postgresql+psycopg2://postgres:letmein@localhost:3333/textbook_images", echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()
