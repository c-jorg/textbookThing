#from sqlalchemy import db.Column, db.String, db.Integer, ForeignKey, Date, Double, Boolean
from . import db, ma
#from marshmallow.exceptions import INCLUDE

class Image(db.Model):
    __tablename__ = "DimImage"
    
    imageID = db.Column("Image_ID", db.Integer, primary_key=True, autoincrement=True)
    imageName = db.Column("Image_Name", db.String, nullable=True)
    fileSizeKB  = db.Column("File_Size_KB", db.String, nullable=True)
    resolution = db.Column("Resolution", db.String, nullable=True)
    bookTitle = db.Column("Book_Title", db.String, nullable=True)
    isbn  = db.Column("ISBN", db.String, nullable=True)
    ieeeRef = db.Column("IEEE_Ref", db.String, nullable=True)
    subjectName = db.Column("Subject_Name", db.String, nullable=True)
    diagramType = db.Column("Diagram_Type", db.String, nullable=True)
    extension = db.Column("Extenstion", db.String, nullable=True)
    blackWhite  = db.Column("Black_White", db.String, nullable=True)
    
    
    def __init__(self, imageName, fileSizeKB, resolution, bookTitle, isbn, ieeeRef, subjectName, diagramName, extension, blackWhite):
        self.imageName = imageName
        self.fileSizeKB = fileSizeKB
        self.resolution = resolution
        self.bookTitle = bookTitle
        self.isbn = isbn
        self.ieeeRef = ieeeRef
        self.subjectName = subjectName
        self.diagramType = diagramName
        self.extension = extension
        self.blackWhite = blackWhite

        
        
        
    def __repr__(self):
        return f" (Image_ID: {self.imageID}, Image_Name: {self.imageName}, File_Size_KB: {self.fileSizeKB}, resolution: {self.resolution}, Book_Title: {self.bookTitle}, ISBN: {self.isbn}, IEEE_Ref: {self.ieeeRef}, Subject_Name: {self.subjectName}, Diagram_Type: {self.diagramType}, Black_White: {self.blackWhite}) "
    
class ImageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Image
        session = db.session
        load_instance = True
        #allows nulls
        unknown = 'include'