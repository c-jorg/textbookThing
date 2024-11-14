#from sqlalchemy import = db.Column, String, db.String, ForeignKey, Date, Double
from . import db, ma, Feature, Image

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
    Extracted_image = db.Coumn("Extracted_Image", db.LargeBinary, nullable=True)
    Full_page_image = db.Column("Full_Page_Image", db.LargeBinary, nullable=True)
    #feature table
    GraphType = db.Column("Graph_Type", db.String, nullable=True)
    NumBars = db.Column("Num_Bars", db.String, nullable=True)
    NumPoints = db.Column("Num_Points", db.String, nullable=True)
    NumSlices = db.Column("Num_Slices", db.String, nullable=True)
    CategoryLabel = db.Column("Category_Label", db.String, nullable=True)
    ProportionLabel = db.Column("Proportion_Label", db.String, nullable=True)
    AxisX = db.Column("Axis_X", db.String, nullable=True)
    AxisY = db.Column("Axis_Y", db.String, nullable=True)
    NumAtoms = db.Column("Num_Atoms", db.String, nullable=True)
    CellType = db.Column("Cell_Type", db.String, nullable=True)
    StructureCount = db.Column("Structure_Count", db.String, nullable=True)
    MagnificationLevel = db.Column("Magnification_Level", db.String, nullable=True)
    StainType = db.Column("Stain_Type", db.String, nullable=True)
    Organ = db.Column("Organ", db.String, nullable=True)
    Layers = db.Column("Layers", db.String, nullable=True)
    MeasurementUnits = db.Column("Measurement_Units", db.String, nullable=True)
    Size = db.Column("Size", db.String, nullable=True)
    Species = db.Column("Species", db.String, nullable=True)
    PopulationDensity = db.Column("Population_Density", db.String, nullable=True)
    Habitat = db.Column("Habitat", db.String, nullable=True)
    Sequence = db.Column("Sequence", db.String, nullable=True)
    Structure = db.Column("Structure", db.String, nullable=True)
    BasePairs = db.Column("Base_Pairs", db.String, nullable=True)
    Molecule = db.Column("Molecule", db.String, nullable=True)
    BondType = db.Column("Bond_Type", db.String, nullable=True)
    Angle = db.Column("Angle", db.String, nullable=True)
    FunctionalGroups = db.Column("Functional_Groups", db.String, nullable=True)
    Reactants = db.Column("Reactants", db.String, nullable=True)
    Products = db.Column("Products", db.String, nullable=True)
    Temperature = db.Column("Temperature", db.String, nullable=True)
    ReactionType = db.Column("Reaction_Type", db.String, nullable=True)
    Equipment = db.Column("Equipment", db.String, nullable=True)
    LiquidVolume = db.Column("Liquid_Volume", db.String, nullable=True)
    SafetyLabel = db.Column("Safety_Label", db.String, nullable=True)
    Element = db.Column("Element", db.String, nullable=True)
    AtomicNumber = db.Column("Atomic_Number", db.String, nullable=True)
    AtomicWeight = db.Column("Atomic_Weight", db.String, nullable=True)
    AtomicGroup = db.Column("Atomic_Group", db.String, nullable=True)
    
    
    def __init__(self, id, Image_name, Resolution, Bytes_size, IsBW, Ext, Extracted_image, Full_page_image, Subject, GraphType, NumBars, NumPoints, NumSlices, CategoryLabel, ProportionLabel, AxisX, AxisY, NumAtoms, CellType, StructureCount, MagnificationLevel, StainType, Organ, Layers, MeasurementUnits, Size, Species, PopulationDensity, Habitat, Sequence, Structure, BasePairs, Molecule, BondType, Angle, FunctionalGroups, Reactants, Products, Temperature, ReactionType, Equipment, LiquidVolume, SafetyLabel, Element, AtomicNumber, AtomicWeight, AtomicGroup):
        self.id = id
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
        return f" (Feature_ID: {self.featureID}, Number_Bars: {self.numberBars}, Number_Points: {self.numberPoints}, Number_Lines: {self.numberLines}, Number_Atoms: {self.numberAtoms}, Axes_Limits: {self.axesLimits}) "

    def makeImage(self):
        image = Image(self.Image_name, self.Bytes_size, self.Resolution, None, None, None, self.Subject, None self.Ext, self.IsBW)
        return image

    def makeFeature(self):
        feature = Feature(self.GraphType, self.NumBars, self.NumPoints, self.NumSlices, self.CategoryLabel, self.ProportionLabel, self.AxisX, self.AxisY, self.NumAtoms, self.CellType, self.StructureCount, self.MagnificationLevel, self.StainType, self.Organ, self.Layers, self.MeasurementUnits, self.Size, self.Species, self.PopulationDensity, self.Habitat, self.Sequence, self.Structure, self.BasePairs, self.Molecule, self.BondType, self.Angle, self.FunctionalGroups, self.Reactants, self.Products, self.Temperature, self.ReactionType, self.Equipment, self.LiquidVolume, self.SafetyLabel, self.Element, self.AtomicNumber, self.AtomicWeight, self.AtomicGroup)
        return feature


class EverythingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Everything
        session = db.session
        load_instance = True