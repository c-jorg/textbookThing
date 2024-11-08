#from flask_sqlalchemy import Column, String, Integer, ForeignKey, Date, Double, LargeBinary, PrimaryKeyConstraint
from . import db

class Diagram(db.Model):
    __tablename__ = "FactDiagram"
    
    
    imageID = db.Column(db.Integer, db.ForeignKey("DimImage.Image_ID"))
    featureID = db.Column(db.Integer, db.ForeignKey("DimFeatures.Feature_ID"))
    dateID = db.Column(db.Integer, db.ForeignKey("DimDate.Date_ID"))
    image = db.Column("Image", db.LargeBinary)
    page = db.Column("Page", db.LargeBinary)
    
    __table__args__=(
        db.PrimaryKeyConstraint(
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