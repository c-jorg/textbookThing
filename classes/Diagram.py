from . import Base, create_engine, ForeignKey, Column, String, Integer, CHAR, ByteA, Boolean, Decimal, Date, Relationship, declarative_base, sessionmaker, scoped_session
from .Date import Date
from .Feature import Feature
from .Image import Image

class Diagram(Base):
    __tablename__ = "FactDiagram"
    
    imageID = Column(Integer, ForeignKey("DimImage.Image_ID"))
    featureID = Column(Integer, ForeignKey("DimFeatures.Feature_ID"))
    dateID = Column(Integer, ForeignKey("DimDate.Date_ID"))
    image = Column("Image", ByteA)
    page = Column("Page", ByteA)
    
    
    def __init__(self, imageID, featureID, dateID, image, page):
        self.imageID = imageID
        self.featureID = featureID
        self.dateID = dateID
        self.image = image
        self.page = page
        
    
    def __repr__(self):
        return f" (Image_ID: {self.imageID}, Feature_ID: {self.featureID}, Date_ID: {self.dateID}, Image: [bytearray], Page: [bytearry]) "