from MaterialProperties import MaterialProperties
from Part import Part


material = MaterialProperties(grade=5, Brinell_hardness=200, poisson_ratio=0.3, Youngs_Modulus=200e9, yield_strength=180e6, UTS=210e6, density=2000)
casing = Part("casing", 'part_info/casing.txt', material)
casing.CalculateMaxStress2DinAxialForceLoading(force=300, torque=10, plotting=True, printing=False)
casing.CalculateMaxStress2DinShearForceLoading(force=300, torque=10, plotting=True, printing=False)
print(f"MAX NORMAL STRESS VALUES = {casing.max_normal_stress}")
print(f" MAX SHEAR STRESS VALUES = {casing.max_shear_stress}")
#print(casing)  # prints all properties of the part
