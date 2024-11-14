#from sqlalchemy import = db.Column, String, db.String, ForeignKey, Date, Double
from . import db, ma

class Feature(db.Model):
    __tablename__ = "DimFeatures"
    
    featureID = db.Column("Feature_ID", db.Integer, primary_key=True, autoincrement=True)
    GraphType = db.Column("Graph_Type", db.String, nullable=True),
    NumBars = db.Column("Number_Bars", db.String, nullable=True),
    NumPoints = db.Column("Number_Points", db.String, nullable=True),
    NumSlices = db.Column("Number_Slices", db.String, nullable=True),
    CategoryLabel = db.Column("Category_label", db.String, nullable=True),
    ProportionLabel = db.Column("ProportionLabel", db.String, nullable=True),
    AxisX = db.Column("Axis_X", db.String, nullable=True),
    AxisY = db.Column("Axis_Y", db.String, nullable=True),
    NumAtoms = db.Column("Number_Atoms", db.String, nullable=True),
    CellType = db.Column("Cell_Type", db.String, nullable=True),
    StructureCount = db.Column("Structure_Count", db.String, nullable=True),
    MagnificationLevel = db.Column("Magnification_Level", db.String, nullable=True),
    StainType = db.Column("Stain_Type", db.String, nullable=True),
    Organ = db.Column("Organ", db.String, nullable=True),
    Layers = db.Column("Layers", db.String, nullable=True),
    MeasurementUnits = db.Column("Measurment_Units", db.String, nullable=True),
    Size = db.Column("Size", db.String, nullable=True),
    Species = db.Column("Species", db.String, nullable=True),
    PopulationDensity = db.Column("Population_Density", db.String, nullable=True),
    Habitat = db.Column("Habitat", db.String, nullable=True),
    Sequence = db.Column("Sequence", db.String, nullable=True),
    Structure = db.Column("Structure", db.String, nullable=True),
    BasePairs = db.Column("Base_Pairs", db.String, nullable=True),
    Molecule = db.Column("Molecule", db.String, nullable=True),
    BondType = db.Column("Bond_Type", db.String, nullable=True),
    Angle = db.Column("Angle", db.String, nullable=True),
    FunctionalGroups = db.Column("Functional_Graphs", db.String, nullable=True),
    Reactants = db.Column("Reactants", db.String, nullable=True),
    Products = db.Column("Products", db.String, nullable=True),
    Temperature = db.Column("Temperature", db.String, nullable=True),
    ReactionType = db.Column("Reaction_Type", db.String, nullable=True),
    Equipment = db.Column("Equipment", db.String, nullable=True),
    LiquidVolume = db.Column("Liquid_Volume", db.String, nullable=True),
    SafetyLabel = db.Column("Safety_Label", db.String, nullable=True),
    Element = db.Column("Element", db.String, nullable=True),
    AtomicNumber = db.Column("Atomic_Number", db.String, nullable=True),
    AtomicWeight = db.Column("Atomic_Weight", db.String, nullable=True),
    AtomicGroup = db.Column("Atomic_Group", db.String, nullable=True)
    
    
    def __init__(self, numberBars, numberPoints, numberLines, numberAtoms, axesLimits):
        self.numberBars = numberBars
        self.numberPoints = numberPoints
        self.numberLines = numberLines
        self.numberAtoms = numberAtoms
        self.axesLimits = axesLimits
        
        
    def __repr__(self):
        return f" (Feature_ID: {self.featureID}, Number_Bars: {self.numberBars}, Number_Points: {self.numberPoints}, Number_Lines: {self.numberLines}, Number_Atoms: {self.numberAtoms}, Axes_Limits: {self.axesLimits}) "

class FeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feature
        session = db.session
        load_instance = True