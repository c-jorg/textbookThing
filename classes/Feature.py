from sqlalchemy import Column, String, Integer, ForeignKey, Date, Double
from . import Base

class Feature(Base):
    __tablename__ = "DimFeatures"
    
    featureID = Column("Feature_ID", Integer, primary_key=True, autoincrement=True)
    numberBars = Column("Number_Bars", Integer, nullable=True)
    numberPoints = Column("Number_Points", Integer, nullable=True)
    numberLines = Column("Number_Lines", Integer, nullable=True)
    numberAtoms = Column("Number_Atoms", Integer, nullable=True)
    axesLimits = Column("Axes_limits", Integer, nullable=True)
    
    
    def __init__(self, numberBars, numberPoints, numberLines, numberAtoms, axesLimits):
        self.numberBars = numberBars
        self.numberPoints = numberPoints
        self.numberLines = numberLines
        self.numberAtoms = numberAtoms
        self.axesLimits = axesLimits
        
        
    def __repr__(self):
        return f" (Feature_ID: {self.featureID}, Number_Bars: {self.numberBars}, Number_Points: {self.numberPoints}, Number_Lines: {self.numberLines}, Number_Atoms: {self.numberAtoms}, Axes_Limits: {self.axesLimits}) "