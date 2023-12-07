import numpy as np

from Hypocycloid import Hypocycloid


class GearMesh():
    def __init__(self,gear1:Hypocycloid,gear2:Hypocycloid) -> None:
        self.driver=gear1
        self.driven=gear2

    def calculateReduction(self):
        self.Reduction = self.driver.N/(self.driven.N-self.driver.N)
        self.driven.omega=self.driver.omega/self.Reduction
        self.driven.cycle=self.driver.cycle/self.Reduction
        self.driven.calculateV()