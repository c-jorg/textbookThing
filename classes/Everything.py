#from sqlalchemy import = db.Column, String, db.String, ForeignKey, Date, Double
from . import ma, Feature, Image, db
from marshmallow import fields, post_load, pre_dump
#from marshmallow.exceptions import INCLUDE
import base64, json

class Everything(db.Model):
    __tablename__ = "image_metadate"
    
    ID = db.Column("ID", db.Integer, primary_key=True, autoincrement=True)
    #image table
    Image_name = db.Column("Image_Name", db.String, nullable=True)
    Resolution = db.Column("Resolution", db.String, nullable=True)
    Bytes_size = db.Column("Bytes_Size", db.String, nullable=True)
    IsBW = db.Column("IsBW", db.String, nullable=True)
    Ext = db.Column("Ext", db.String, nullable=True)
    Subject = db.Column("Subject", db.String, nullable=True)
    #fact table
    Extracted_image = db.Column("Extracted_Image", db.LargeBinary, nullable=True)
    Full_page_image = db.Column("Full_Page_Image", db.LargeBinary, nullable=True)
    #feature table
    GraphType = db.Column("GraphType", db.String, nullable=True)
    NumBars = db.Column("NumBars", db.String, nullable=True)
    NumPoints = db.Column("NumPoints", db.String, nullable=True)
    NumSlices = db.Column("NumSlices", db.String, nullable=True)
    CategoryLabel = db.Column("CategoryLabel", db.String, nullable=True)
    ProportionLabel = db.Column("ProportionLabel", db.String, nullable=True)
    AxisX = db.Column("AxisX", db.String, nullable=True)
    AxisY = db.Column("AxisY", db.String, nullable=True)
    NumAtoms = db.Column("Num_Atoms", db.String, nullable=True)
    CellType = db.Column("CellType", db.String, nullable=True)
    StructureCount = db.Column("Structure_Count", db.String, nullable=True)
    MagnificationLevel = db.Column("MagnificationLevel", db.String, nullable=True)
    StainType = db.Column("Stain_Type", db.String, nullable=True)
    Organ = db.Column("Organ", db.String, nullable=True)
    Layers = db.Column("Layers", db.String, nullable=True)
    MeasurementUnits = db.Column("MeasurementUnits", db.String, nullable=True)
    Size = db.Column("Size", db.String, nullable=True)
    Species = db.Column("Species", db.String, nullable=True)
    PopulationDensity = db.Column("PopulationDensity", db.String, nullable=True)
    Habitat = db.Column("Habitat", db.String, nullable=True)
    Sequence = db.Column("Sequence", db.String, nullable=True)
    Structure = db.Column("Structure", db.String, nullable=True)
    BasePairs = db.Column("BasePairs", db.String, nullable=True)
    Molecule = db.Column("Molecule", db.String, nullable=True)
    BondType = db.Column("BondType", db.String, nullable=True)
    Angle = db.Column("Angle", db.String, nullable=True)
    FunctionalGroups = db.Column("FunctionalGroups", db.String, nullable=True)
    Reactants = db.Column("Reactants", db.String, nullable=True)
    Products = db.Column("Products", db.String, nullable=True)
    Temperature = db.Column("Temperature", db.String, nullable=True)
    ReactionType = db.Column("ReactionType", db.String, nullable=True)
    Equipment = db.Column("Equipment", db.String, nullable=True)
    LiquidVolume = db.Column("LiquidVolume", db.String, nullable=True)
    SafetyLabel = db.Column("SafetyLabel", db.String, nullable=True)
    Element = db.Column("Element", db.String, nullable=True)
    AtomicNumber = db.Column("AtomicNumber", db.String, nullable=True)
    AtomicWeight = db.Column("AtomicWeight", db.String, nullable=True)
    AtomicGroup = db.Column("AtomicGroup", db.String, nullable=True)
    
    
    def __init__(self, Image_name=None, Resolution=None, Bytes_size=None, IsBW=None, Ext=None, Extracted_image=None, Full_page_image=None, Subject=None, GraphType=None, NumBars=None, NumPoints=None, NumSlices=None, CategoryLabel=None, ProportionLabel=None, AxisX=None, AxisY=None, NumAtoms=None, CellType=None, StructureCount=None, MagnificationLevel=None, StainType=None, Organ=None, Layers=None, MeasurementUnits=None, Size=None, Species=None, PopulationDensity=None, Habitat=None, Sequence=None, Structure=None, BasePairs=None, Molecule=None, BondType=None, Angle=None, FunctionalGroups=None, Reactants=None, Products=None, Temperature=None, ReactionType=None, Equipment=None, LiquidVolume=None, SafetyLabel=None, Element=None, AtomicNumber=None, AtomicWeight=None, AtomicGroup=None):
        self.Image_name = Image_name
        self.Resolution = Resolution
        self.Bytes_size = Bytes_size
        self.IsBW = IsBW
        self.Ext = Ext
        self.Extracted_image = Extracted_image
        self.Full_page_image = Full_page_image
        self.Subject = Subject
        self.GraphType = GraphType
        self.NumBars = NumBars
        self.NumPoints = NumPoints
        self.NumSlices = NumSlices
        self.CategoryLabel = CategoryLabel
        self.ProportionLabel = ProportionLabel
        self.AxisX = AxisX
        self.AxisY = AxisY
        self.NumAtoms = NumAtoms
        self.CellType = CellType
        self.StructureCount = StructureCount
        self.MagnificationLevel = MagnificationLevel
        self.StainType = StainType
        self.Organ = Organ
        self.Layers = Layers
        self.MeasurementUnits = MeasurementUnits
        self.Size = Size
        self.Species = Species
        self.PopulationDensity = PopulationDensity
        self.Habitat = Habitat
        self.Sequence = Sequence
        self.Structure = Structure
        self.BasePairs = BasePairs
        self.Molecule = Molecule
        self.BondType = BondType
        self.Angle = Angle
        self.FunctionalGroups = FunctionalGroups
        self.Reactants = Reactants
        self.Products = Products
        self.Temperature = Temperature
        self.ReactionType = ReactionType
        self.Equipment = Equipment
        self.LiquidVolume = LiquidVolume
        self.SafetyLabel = SafetyLabel
        self.Element = Element
        self.AtomicNumber = AtomicNumber
        self.AtomicWeight = AtomicWeight
        self.AtomicGroup = AtomicGroup
        
        
    def __repr__(self):
        return f" (GraphType: {self.GraphType} Number_Bars: {self.NumBars}, Number_Points: {self.NumPoints}, Number_Slices: {self.NumSlices}, Number_Atoms: {self.NumAtoms}) "

    def makeImage(self):
        image = Image(self.Image_name, self.Bytes_size, self.Resolution, None, None, None, self.Subject, None, self.Ext, self.IsBW)
        return image

    def makeFeature(self):
        feature = Feature(self.GraphType, self.NumBars, self.NumPoints, self.NumSlices, self.CategoryLabel, self.ProportionLabel, self.AxisX, self.AxisY, self.NumAtoms, self.CellType, self.StructureCount, self.MagnificationLevel, self.StainType, self.Organ, self.Layers, self.MeasurementUnits, self.Size, self.Species, self.PopulationDensity, self.Habitat, self.Sequence, self.Structure, self.BasePairs, self.Molecule, self.BondType, self.Angle, self.FunctionalGroups, self.Reactants, self.Products, self.Temperature, self.ReactionType, self.Equipment, self.LiquidVolume, self.SafetyLabel, self.Element, self.AtomicNumber, self.AtomicWeight, self.AtomicGroup)
        return feature

    @staticmethod
    def replaceNoData(data):
        #jsonData = json.loads(data)
        for key, value in data.items():
            #print(f"key: {key}, value: {value}")
            if value == 'No Data':
                data[key] = None
            #else:
                #print(f"value {value} != 'No Data")
        return data


class EverythingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Everything
        session = db.session
        load_instance = True
        Extracted_image = fields.Raw()
        Full_page_image = fields.Raw()
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