#rom flask_sqlalchemy import Column, String, Integer, ForeignKey, Date, Double
from . import db

class Feature(db.Model):
    __tablename__ = "DimFeatures"
    
    featureID = db.Column("Feature_ID", db.Integer, primary_key=True, autoincrement=True)
    numberBars = db.Column("Number_Bars", db.Integer, nullable=True)
    numberPoints = db.Column("Number_Points", db.Integer, nullable=True)
    numberLines = db.Column("Number_Lines", db.Integer, nullable=True)
    numberAtoms = db.Column("Number_Atoms", db.Integer, nullable=True)
    axesLimits = db.Column("Axes_limits", db.Integer, nullable=True)
    
    
    def __init__(self, numberBars, numberPoints, numberLines, numberAtoms, axesLimits):
        self.numberBars = numberBars
        self.numberPoints = numberPoints
        self.numberLines = numberLines
        self.numberAtoms = numberAtoms
        self.axesLimits = axesLimits
        
        
    def __repr__(self):
        return f" (Feature_ID: {self.featureID}, Number_Bars: {self.numberBars}, Number_Points: {self.numberPoints}, Number_Lines: {self.numberLines}, Number_Atoms: {self.numberAtoms}, Axes_Limits: {self.axesLimits}) "