#from sqlalchemy import = db.column, String, db.String, ForeignKey, Date, Double
from . import db, ma

class Feature(db.Model):
    __tablename__ = "DimFeatures"
    
    featureID = db.column("Feature_ID", db.Integer, primary_key=True, autoincrement=True)
    GraphType = db.column("Graph_Type", db.String, nullable=True),
    NumBars = db.column("Number_Bars", db.String, nullable=True),
    NumPoints = db.column("Number_Points", db.String, nullable=True),
    NumSlices = db.column("Number_Slices", db.String, nullable=True),
    CategoryLabel = db.column("Category_label", db.String, nullable=True),
    ProportionLabel = db.column("ProportionLabel", db.String, nullable=True),
    AxisX = db.column("Axis_X", db.String, nullable=True),
    AxisY = db.column("Axis_Y", db.String, nullable=True),
    NumAtoms = db.column("Number_Atoms", db.String, nullable=True),
    CellType = db.column("Cell_Type", db.String, nullable=True),
    StructureCount = db.column("Structure_Count", db.String, nullable=True),
    MagnificationLevel = db.column("Magnification_Level", db.String, nullable=True),
    StainType = db.column("Stain_Type", db.String, nullable=True),
    Organ = db.column("Organ", db.String, nullable=True),
    Layers = db.column("Layers", db.String, nullable=True),
    MeasurementUnits = db.column("Measurment_Units", db.String, nullable=True),
    Size = db.column("Size", db.String, nullable=True),
    Species = db.column("Species", db.String, nullable=True),
    PopulationDensity = db.column("Population_Density", db.String, nullable=True),
    Habitat = db.column("Habitat", db.String, nullable=True),
    Sequence = db.column("Sequence", db.String, nullable=True),
    Structure = db.column("Structure", db.String, nullable=True),
    BasePairs = db.column("Base_Pairs", db.String, nullable=True),
    Molecule = db.column("Molecule", db.String, nullable=True),
    BondType = db.column("Bond_Type", db.String, nullable=True),
    Angle = db.column("Angle", db.String, nullable=True),
    FunctionalGroups = db.column("Functional_Graphs", db.String, nullable=True),
    Reactants = db.column("Reactants", db.String, nullable=True),
    Products = db.column("Products", db.String, nullable=True),
    Temperature = db.column("Temperature", db.String, nullable=True),
    ReactionType = db.column("Reaction_Type", db.String, nullable=True),
    Equipment = db.column("Equipment", db.String, nullable=True),
    LiquidVolume = db.column("Liquid_Volume", db.String, nullable=True),
    SafetyLabel = db.column("Safety_Label", db.String, nullable=True),
    Element = db.column("Element", db.String, nullable=True),
    AtomicNumber = db.column("Atomic_Number", db.String, nullable=True),
    AtomicWeight = db.column("Atomic_Weight", db.String, nullable=True),
    atomicGroup = db.column("Atomic_Group", db.String, nullable=True)
    
    
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