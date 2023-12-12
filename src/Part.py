import numpy as np
from GearMaterialProperties import GearMaterialProperties

class Part:
    def __init__(self, name:str,file_path:str,material:GearMaterialProperties):
        # Initialize properties with default values
        self.name=name
        self.material=material
        self.V = 0
        self.Ixx = 0
        self.Iyy = 0
        self.Izz = 0
        self.Ixy = 0
        self.Ixz = 0
        self.Iyz = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.A_min = 0
        self.r_max = 0
        # Read values from the text file and update properties
        self.read_values_from_file(file_path)

    def read_values_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

                # Iterate through lines and update properties based on labels
                current_label = None
                for line in lines:
                    line = line.strip()

                    if line.startswith('[') and line.endswith(']'):
                        # Extract label from the line
                        current_label = line[1:-1]
                    else:
                        # Update property based on the current label
                        setattr(self, current_label, float(line))

        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except ValueError:
            print("Error: Invalid values in the file.")
        except Exception as e:
            print(f"An error occurred: {e}")
    def J(self):
        self.J_xy = self.Ixx+self.Iyy

    def calculateAxialStress_z(self,force):
        self.sigma_z = force/self.A_min    

    def calculateTorsion_xy(self,torque):
        self.tau_xy = torque*self.c/self.J()

    

    def __str__(self):
        return f"Name: {self.name}\nV: {self.V}, A: {self.A_min},r: {self.r_max}, Ixx: {self.Ixx}, Iyy: {self.Iyy}, Izz: {self.Izz}, Ixy: {self.Ixy}, Ixz: {self.Ixz}, Iyz: {self.Iyz}, x: {self.x}, y: {self.y}, z: {self.z}"



material=GearMaterialProperties(1,200,0.3,200e9,180e6,210e6,2000)
# Example usage
casing = Part("casing",'part_info/casing.txt',material)
print(casing)

