from . import Base, create_engine, ForeignKey, Column, String, Integer, CHAR, Boolean, Decimal, Date, Relationship, declarative_base, sessionmaker, scoped_session


class Image(Base):
    __tablename__ = "DimImage"
    
    imageID = Column("Image_ID", Integer, primary_key=True)
    imageName = Column("Image_Name", String, nullable=True)
    fileSizeKB  = Column("File_Size_KB", Decimal, nullable=True)
    pixelWidth = Column("Pixel_Width", Integer, nullable=True)
    pixelHeight = Column("Pixel_Height", Integer, nullable=True)
    bookTitle = Column("Book_Title", String, nullable=True)
    isbn  = Column("ISBN", String, nullable=True)
    ieeeRef = Column("IEEE_Ref", String, nullable=True)
    subjectName = Column("Subject_Name", String, nullable=True)
    diagramType = Column("Diagram_Type", String, nullable=True)
    blackWhite  = Column("Black_White", Boolean, nullable=True)
    
    
    def __init__(self, imageID, imageName, fileSizeKB, pixelWidth, pixelHeight, bookTitle, isbn, ieeeRef, subjectName, diagramName, blackWhite):
        self.imageID = imageID
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
    