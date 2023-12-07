import numpy as np
import sympy as sym
from GearMesh import GearMesh



class GearTrain():
    def __init__(self,mesh1:GearMesh,mesh2:GearMesh) -> None:
        self.mesh1=mesh1
        self.mesh2=mesh2

    def calculateOverallReduction(self):
        return (self.mesh1.driver.N*self.mesh2.driven.N)/(self.mesh2.driver.N*self.mesh1.driven.N-self.mesh2.driven.N*self.mesh1.driver.N)


