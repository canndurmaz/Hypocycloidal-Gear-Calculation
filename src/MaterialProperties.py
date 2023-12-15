import numpy as np

class MaterialProperties():
    def __init__(self,grade:int,Brinell_hardness:float,poisson_ratio:float,Youngs_Modulus:float,yield_strength:float,UTS:float,density:float) -> None:
        self.poisson=poisson_ratio
        self.Young=Youngs_Modulus
        self.yield_strength=yield_strength
        self.UTS=UTS
        self.density=density
        self.H_B=Brinell_hardness
        if grade==1:
            self.S_t=(0.533*self.H_B+88.3)*1e6
            self.S_c=(2.22*self.H_B+200)*1e6
            
        elif grade==2:
            self.S_t=(0.703*self.H_B+113)*1e6
            self.S_c=(2.41*self.H_B+237)*1e6
            