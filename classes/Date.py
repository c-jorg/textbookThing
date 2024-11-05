from . import Base, create_engine, ForeignKey, Column, String, Integer, CHAR, Decimal, Date, Relationship, declarative_base, sessionmaker, scoped_session


class Date(Base):
    __tablename__ = "DimDate"
    
    dateID = Column("Date_ID", Integer, primary_key=True)
    date = Column("Date", Date)
    year = Column("Year", Integer)
    
    def __init__(self, dateID, date, year):
        self.dateID = dateID
        self.date = date
        self.year = year
        
        
    def __repr__(self):
        return f" (Date_ID: {self.dateID}, Date: {self.date}, Year: {self.year}) "