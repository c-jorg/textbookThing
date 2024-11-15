#from sqlalchemy import Column, String, Integer, ForeignKey, Date, Double, LargeBinary, PrimaryKeyConstraint
from . import db, ma
from marshmallow import fields, post_load, pre_dump
#from marshmallow.exceptions import INCLUDE
import base64, json

class Diagram(db.Model):
    __tablename__ = "FactDiagram"
    
    
    imageID = db.Column(db.Integer, db.ForeignKey("DimImage.Image_ID"))
    featureID = db.Column(db.Integer, db.ForeignKey("DimFeature.Feature_ID"))
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

class DiagramSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Diagram
        session = db.session
        load_instance = True
        #allows nulls
        unknown = 'include'

    @post_load
    def decode_images(self, data, **kwargs):
        #decodes the string to binary data
        if 'Extracted_image' in data and data['Extracted_image'] is not None:
            data['Extracted_image'] = base64.b64decode(data['Extracted_image'])
        if 'Full_page_image' in data and data['Full_page_image'] is not None:
            data['Full_page_image'] = base64.b64decode(data['Full_page_image'])
        return data

    @pre_dump
    def encode_images(self, data, **kwargs):
        #encode the byte arrays into strings for exporting in json 
        if data.Extracted_image is not None:
            data.Extracted_image = base64.b64encode(data.Extracted_image).decode('utf-8')
        if data.Full_page_image is not None:
            data.Full_page_image = base64.b64encode(data.Full_page_image).decode('utf-8')
        return data  