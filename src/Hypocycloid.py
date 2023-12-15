import numpy as np

from MaterialProperties import MaterialProperties
from StressCalculation import StressCalculation
from mohr2d import mohr

class Hypocycloid():
    def __init__(self, N:int, R: float, r:float, face_width:float,force:list[float],material:MaterialProperties,tooth_root:float,tooth_height:float,cycle:int,omega:float=None) -> None:
        self.N=N
        self.R=R 
        self.r=r
        self.material=material
        self.face_width=face_width
        self.pitch_dia=2*self.R-self.r
        if len(force) != 3 or not all(isinstance(val, float) for val in force):
            raise ValueError("The 'force' list must have exactly three float values. [tangential, radial, transverse]")
        self.force = force
        self.omega=omega
        self.tooth_root=tooth_root
        self.tooth_height=tooth_height
        self.mt=self.pitch_dia/self.N
        if omega is not None:
            self.calculateV()
        self.cycle=cycle

    def calculateV(self):
        self.V=abs(self.omega*self.pitch_dia/2)
    def calculateBendingStress(self):
        self.BendingStress = self.force[0]*StressCalculation.K_o()*StressCalculation.K_v(Qv=6,V=self.V)*StressCalculation.K_s()*StressCalculation.K_b(self.tooth_root,self.tooth_height)*StressCalculation.K_H(face_width=self.face_width,pitch_dia=self.pitch_dia)/(self.face_width*self.mt*StressCalculation.Y_J(self.N))

    def calculateContactStress(self):
        self.ContactStress = StressCalculation.Z_E(self.material)*np.sqrt(self.force[0]*StressCalculation.K_o()*StressCalculation.K_v(Qv=6,V=self.V)*StressCalculation.K_s()*StressCalculation.K_H(self.face_width,self.pitch_dia)*StressCalculation.Z_R()/(self.pitch_dia*self.face_width*StressCalculation.Z_I()))

    def calculateAllowableBendingStress(self):
        self.AllowableBendingStress = self.material.S_t*StressCalculation.Y_N(self.cycle)/(StressCalculation.Y_Theta()*StressCalculation.Y_Z())
    
    def calculateAllowableContactStress(self):
        self.AllowableContactStress = self.material.S_c*StressCalculation.Z_N(self.cycle)*StressCalculation.Z_N(self.cycle)/(StressCalculation.Y_Theta()*StressCalculation.Y_Z())

    def calculateStresses(self):
        self.calculateV()
        self.calculateBendingStress()
        self.calculateContactStress()
        self.calculateAllowableBendingStress()
        self.calculateAllowableContactStress()
        
        self.FactorofSafety_Bending = self.AllowableBendingStress/self.BendingStress
        self.FactorofSafety_Contact = self.AllowableContactStress/self.ContactStress
        return (self.FactorofSafety_Bending,self.FactorofSafety_Contact)