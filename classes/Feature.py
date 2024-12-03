#from sqlalchemy import Column, String, Integer, ForeignKey, Date, Double, LargeBinary, PrimaryKeyConstraint
from . import db, ma
#from marshmallow.exceptions import INCLUDE

class Feature(db.Model):
    __tablename__ = "DimFeature"
    
    featureID = db.Column("Feature_ID", db.Integer, primary_key=True, autoincrement=True)
    GraphType = db.Column("Graph_Type", db.String, nullable=True)
    NumBars = db.Column("Num_Bars", db.String, nullable=True)
    NumPoints = db.Column("Num_Points", db.String, nullable=True)
    NumSlices = db.Column("Num_Slices", db.String, nullable=True)
    CategoryLabel = db.Column("Category_Label", db.String, nullable=True)
    ProportionLabel = db.Column("Proportion_Label", db.String, nullable=True)
    AxisX = db.Column("Axis_X", db.String, nullable=True)
    AxisXMin = db.Column("Axis_X_Min", db.String, nullable=True)
    AxisXMax = db.Column("Axis_X_Max", db.String, nullable=True)
    AxisY = db.Column("Axis_Y", db.String, nullable=True)
    GeometricShape = db.Column("Geometric_Shape", db.String, nullable=True)
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


    def __init__(self, GraphType, NumBars, NumPoints, NumSlices, CategoryLabel, ProportionLabel, AxisX, AxisXMin, AxisXMax, AxisY, GeometricShape, NumAtoms, CellType, StructureCount, MagnificationLevel, StainType, Organ, Layers, MeasurementUnits, Size, Species, PopulationDensity, Habitat, Sequence, Structure, BasePairs, Molecule, BondType, Angle, FunctionalGroups, Reactants, Products, Temperature, ReactionType, Equipment, LiquidVolume, SafetyLabel, Element, AtomicNumber, AtomicWeight, AtomicGroup, ):
        self.AxisXMin = AxisXMin
        self.AxisXMax = AxisXMax
        self.GeometricShape = GeometricShape
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
        return f" (Feature_ID: {self.featureID}, GraphType {self.GraphType}, etc)"

class FeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feature
        session = db.session
        load_instance = True
        #allows nulls
        unknown = 'include'