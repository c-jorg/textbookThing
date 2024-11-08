#from flask_sqlalchemy import Column, String, Integer, ForeignKey, Date, Double
from . import db

class Date(db.Model):
    __tablename__ = "DimDate"
    
    dateID = db.Column("Date_ID", db.Integer, primary_key=True, autoincrement=True)
    date = db.Column("Date", db.Date)
    year = db.Column("Year", db.Integer)
    
    def __init__(self, date, year):
        
        self.date = date
        self.year = year
        
        
    def __repr__(self):
        return f" (Date_ID: {self.dateID}, Date: {self.date}, Year: {self.year}) "