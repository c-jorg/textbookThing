#from sqlalchemy import = db.Column, String, db.String, ForeignKey, Date, Double
from . import ma, Feature, Image, db
from marshmallow import fields, post_load, pre_dump
#from marshmallow.exceptions import INCLUDE
import base64, json

class Everything(db.Model):
    __tablename__ = "image_metadata2"
    
    ID = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    #image table
    Image_name = db.Column("image_name", db.String, nullable=True)
    Resolution = db.Column("resolution", db.String, nullable=True)
    Bytes_size = db.Column("bytes_size", db.String, nullable=True)
    IsBW = db.Column("isbw", db.String, nullable=True)
    Ext = db.Column("ext", db.String, nullable=True)
    Subject = db.Column("subject", db.String, nullable=True)
    Subtopic = db.Column("subtopic", db.String, nullable=True)
    #fact table
    Extracted_image = db.Column("extracted_image", db.LargeBinary, nullable=True)
    Full_page_image = db.Column("full_page_image", db.LargeBinary, nullable=True)
    #feature table
    GraphType = db.Column("graphtype", db.String, nullable=True)
    NumBars = db.Column("numbars", db.String, nullable=True)
    NumPoints = db.Column("numpoints", db.String, nullable=True)
    NumSlices = db.Column("numslices", db.String, nullable=True)
    CategoryLabel = db.Column("categorylabel", db.String, nullable=True)
    ProportionLabel = db.Column("proportionlabel", db.String, nullable=True)
    AxisX = db.Column("axisx", db.String, nullable=True)
    AxisX_min = db.Column("axisx_min", db.String, nullable=True)
    AxisX_max = db.Column("axisx_max", db.String, nullable=True)
    AxisY = db.Column("axisy", db.String, nullable=True)
    GeometricShape = db.Column("geometric_shape", db.String, nullable=True)
    NumAtoms = db.Column("numatoms", db.String, nullable=True)
    CellType = db.Column("celltype", db.String, nullable=True)
    StructureCount = db.Column("structurecount", db.String, nullable=True)
    MagnificationLevel = db.Column("magnificationlevel", db.String, nullable=True)
    StainType = db.Column("staintype", db.String, nullable=True)
    Organ = db.Column("organ", db.String, nullable=True)
    Layers = db.Column("layers", db.String, nullable=True)
    MeasurementUnits = db.Column("measurementunits", db.String, nullable=True)
    Size = db.Column("size", db.String, nullable=True)
    Species = db.Column("species", db.String, nullable=True)
    PopulationDensity = db.Column("populationdensity", db.String, nullable=True)
    Habitat = db.Column("habitat", db.String, nullable=True)
    Sequence = db.Column("sequence", db.String, nullable=True)
    Structure = db.Column("structure", db.String, nullable=True)
    BasePairs = db.Column("basepairs", db.String, nullable=True)
    Molecule = db.Column("molecule", db.String, nullable=True)
    BondType = db.Column("bondtype", db.String, nullable=True)
    Angle = db.Column("angle", db.String, nullable=True)
    FunctionalGroups = db.Column("functionalgroups", db.String, nullable=True)
    Reactants = db.Column("reactants", db.String, nullable=True)
    Products = db.Column("products", db.String, nullable=True)
    Temperature = db.Column("temperature", db.String, nullable=True)
    ReactionType = db.Column("reactiontype", db.String, nullable=True)
    Equipment = db.Column("equipment", db.String, nullable=True)
    LiquidVolume = db.Column("liquidvolume", db.String, nullable=True)
    SafetyLabel = db.Column("safetylabel", db.String, nullable=True)
    Element = db.Column("element", db.String, nullable=True)
    AtomicNumber = db.Column("atomicnumber", db.String, nullable=True)
    AtomicWeight = db.Column("atomicweight", db.String, nullable=True)
    AtomicGroup = db.Column("atomicgroup", db.String, nullable=True)
    
    
    def __init__(self, Image_name=None, Resolution=None, Bytes_size=None, IsBW=None, Ext=None, Extracted_image=None, Full_page_image=None, Subject=None, Subtopic=None, GraphType=None, NumBars=None, NumPoints=None, NumSlices=None, CategoryLabel=None, ProportionLabel=None, AxisX=None, AxisX_min=None, AxisX_max=None, AxisY=None, GeometricShape=None, NumAtoms=None, CellType=None, StructureCount=None, MagnificationLevel=None, StainType=None, Organ=None, Layers=None, MeasurementUnits=None, Size=None, Species=None, PopulationDensity=None, Habitat=None, Sequence=None, Structure=None, BasePairs=None, Molecule=None, BondType=None, Angle=None, FunctionalGroups=None, Reactants=None, Products=None, Temperature=None, ReactionType=None, Equipment=None, LiquidVolume=None, SafetyLabel=None, Element=None, AtomicNumber=None, AtomicWeight=None, AtomicGroup=None):
        self.AxisX_min = AxisX_min
        self.AxisX_max = AxisX_max
        self.Subtopic = Subtopic
        self.GeometricShape = GeometricShape
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
        image = Image(self.Image_name, self.Bytes_size, self.Resolution, None, None, None, self.Subject, self.Subtopic, None, self.Ext, self.IsBW)
        return image

    def makeFeature(self):
        feature = Feature(self.GraphType, self.NumBars, self.NumPoints, self.NumSlices, self.CategoryLabel, self.ProportionLabel, self.AxisX, self.AxisX_min, self.AxisX_max, self.AxisY, self.GeometricShape, self.NumAtoms, self.CellType, self.StructureCount, self.MagnificationLevel, self.StainType, self.Organ, self.Layers, self.MeasurementUnits, self.Size, self.Species, self.PopulationDensity, self.Habitat, self.Sequence, self.Structure, self.BasePairs, self.Molecule, self.BondType, self.Angle, self.FunctionalGroups, self.Reactants, self.Products, self.Temperature, self.ReactionType, self.Equipment, self.LiquidVolume, self.SafetyLabel, self.Element, self.AtomicNumber, self.AtomicWeight, self.AtomicGroup)
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
            print("pre encode")
            print(data.Extracted_image)
            data.Extracted_image = base64.b64encode(data.Extracted_image).decode('utf-8')
            print("post encode" + data.Extracted_image)
        if data.Full_page_image is not None:
            print("Pre encode")
            print(data.Full_page_image)
            data.Full_page_image = base64.b64encode(data.Full_page_image).decode('utf-8')
            print("post encode" +data.Full_page_image)
        return data    