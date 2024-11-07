from sqlalchemy import Column, String, Integer, ForeignKey, Date, Double, LargeBinary, PrimaryKeyConstraint
from . import Base

class Diagram(Base):
    __tablename__ = "FactDiagram"
    
    
    imageID = Column(Integer, ForeignKey("DimImage.Image_ID"))
    featureID = Column(Integer, ForeignKey("DimFeatures.Feature_ID"))
    dateID = Column(Integer, ForeignKey("DimDate.Date_ID"))
    image = Column("Image", LargeBinary)
    page = Column("Page", LargeBinary)
    
    __table__args__=(
        PrimaryKeyConstraint(
            imageID, featureID, dateID
        ),
    )


    def __init__(self, imageID, featureID, dateID, image, page):
        self.imageID = imageID
        self.featureID = featureID
        self.dateID = dateID
        self.image = image
        self.page = page
        
    
    def __repr__(self):
        return f" (Image_ID: {self.imageID}, Feature_ID: {self.featureID}, Date_ID: {self.dateID}, Image: [bytearray], Page: [bytearry]) "