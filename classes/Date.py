from sqlalchemy import Column, String, Integer, ForeignKey, Date, Double
from flask_marshmallow import Marshmallow 
from . import Base

class Date(Base):
    __tablename__ = "DimDate"
    
    dateID = Column("Date_ID", Integer, primary_key=True, autoincrement=True)
    date = Column("Date", Date)
    year = Column("Year", Integer)
    
    def __init__(self, date, year):
        
        self.date = date
        self.year = year
        
        
    def __repr__(self):
        return f" (Date_ID: {self.dateID}, Date: {self.date}, Year: {self.year}) "


class DateSchema(ma.ModelSchema):
    class Meta:
        model = Date