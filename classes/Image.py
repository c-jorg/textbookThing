#from flask_sqlalchemy import Column, String, Integer, ForeignKey, Date, Double, Boolean
from . import db

class Image(db.Model):
    __tablename__ = "DimImage"
    
    imageID = db.Column("Image_ID", db.Integer, primary_key=True, autoincrement=True)
    imageName = db.Column("Image_Name", db.String, nullable=True)
    fileSizeKB  = db.Column("File_Size_KB", db.Double, nullable=True)
    pixelWidth = db.Column("Pixel_Width", db.Integer, nullable=True)
    pixelHeight = db.Column("Pixel_Height", db.Integer, nullable=True)
    bookTitle = db.Column("Book_Title", db.String, nullable=True)
    isbn  = db.Column("ISBN", db.String, nullable=True)
    ieeeRef = db.Column("IEEE_Ref", db.String, nullable=True)
    subjectName = db.Column("Subject_Name", db.String, nullable=True)
    diagramType = db.Column("Diagram_Type",db. String, nullable=True)
    blackWhite  = db.Column("Black_White", db.Boolean, nullable=True)
    
    
    def __init__(self, imageName, fileSizeKB, pixelWidth, pixelHeight, bookTitle, isbn, ieeeRef, subjectName, diagramName, blackWhite):
        self.imageName = imageName
        self.fileSizeKB = fileSizeKB
        self.pixelWidth = pixelWidth
        self.pixelHeight = pixelHeight
        self.bookTitle = bookTitle
        self.isbn = isbn
        self.ieeeRef = ieeeRef
        self.subjectName = subjectName
        self.diagramType = diagramName
        self.blackWhite = blackWhite

        
        
        
    def __repr__(self):
        return f" (Image_ID: {self.imageID}, Image_Name: {self.imageName}, File_Size_KB: {self.fileSizeKB}, Pixel_Width: {self.pixelWidth}, Pixel_Height: {self.pixelHeight}, Book_Title: {self.bookTitle}, ISBN: {self.isbn}, IEEE_Ref: {self.ieeeRef}, Subject_Name: {self.subjectName}, Diagram_Type: {self.diagramType}, Black_White: {self.blackWhite}) "
    