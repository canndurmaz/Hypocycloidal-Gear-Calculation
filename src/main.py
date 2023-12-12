from GearMaterialProperties import GearMaterialProperties
from GearMesh import GearMesh
from GearTrain import GearTrain
from Hypocycloid import Hypocycloid
import numpy as np

force_from_torque=float(10/26e-3)
material=GearMaterialProperties(1,200,0.3,200e9,180e6,210e6,2000)
stationary=Hypocycloid(int(input("Input Stationary Gear Teeth Number: ")),28e-3,0.7e-3,5e-3,[500.0,0.0,0.0],material,10e-3,0.7e-3,1e6,omega=0)
Hypobottom=Hypocycloid(int(input("Input Hypocycloidal Bottom Gear Teeth Number: ")),21e-3,0.7e-3,5e-3,[500.0,0.0,0.0],material,10e-3,0.7e-3,1e6,omega=8000*np.pi/30)
Hypotop=Hypocycloid(int(input("Input Hypocycloidal Upper Gear Teeth Number: ")),17e-3,0.7e-3,5e-3,[500.0,0.0,0.0],material,10e-3,0.7e-3,1e6,omega=8000*np.pi/30)
turntable=Hypocycloid(int(input("Input Turntable Teeth Number: ")),26e-3,0.7e-3,5e-3,[force_from_torque,0.0,0.0],material,10e-3,0.7e-3,1e6,omega=8000*np.pi/2700)

mesh=GearMesh(Hypobottom,stationary)
mesh2=GearMesh(Hypotop,turntable)
train=GearTrain(mesh,mesh2)
print(f"Reduction Ratio: {train.calculateOverallReduction()}")