from . import Base, create_engine, ForeignKey, Column, String, Integer, CHAR, Decimal, Date, Relationship, declarative_base, sessionmaker, scoped_session


class Feature(Base):
    __tablename__ = "DimFeatures"
    
    featureID = Column("Feature_ID", Integer, primary_key=True)
    numberBars = Column("Number_Bars", Integer, nullable=True)
    numberPoints = Column("Number_Points", Integer, nullable=True)
    numberLines = Column("Number_Lines", Integer, nullable=True)
    numberAtoms = Column("Number_Atoms", Integer, nullable=True)
    axesLimits = Column("Axes_limits", Integer, nullable=True)
    
    
    def __init__(self, featureID, numberBars, numberPoints, numberLines, numberAtoms, axesLimits):
        self.featureID = featureID
        self.numberBars = numberBars
        self.numberPoints = numberPoints
        self.numberLines = numberLines
        self.numberAtoms = numberAtoms
        self.axesLimits = axesLimits
        
        
    def __repr__(self):
        return f" (Feature_ID: {self.featureID}, Number_Bars: {self.numberBars}, Number_Points: {self.numberPoints}, Number_Lines: {self.numberLines}, Number_Atoms: {self.numberAtoms}, Axes_Limits: {self.axesLimits}) "