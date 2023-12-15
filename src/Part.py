import numpy as np
from MaterialProperties import MaterialProperties
import mohr2d

class Part:
    def __init__(self, name: str, file_path: str, material: MaterialProperties):
        # Initialize properties with default values
        self.name = name
        self.material = material
        self.file_path = file_path
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
        self.r_min = 0
        self.L = 0
        self.max_normal_stress = []
        self.max_shear_stress = []

        # Read values from the text file and update properties
        self.read_values_from_file()
        self._update_all()

    def read_values_from_file(self):
        """Read values from the text file."""
        try:
            with open(self.file_path, 'r') as file:
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
            print(f"File not found: {self.file_path}")
        except ValueError:
            print("Error: Invalid values in the file.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def _calculate_J_xy(self):
        """Calculate the first moment of area in XY plane."""
        self.J_xy = self.Ixx + self.Iyy

    def _calculateAxialStress_z(self, force):
        """Calculate axial stress due to applied force."""
        self._update_all()
        sigma_z = force / self.A_min
        return sigma_z

    def _calculateTorsion(self, torque):
        """Calculate torsional stress due to applied torque."""
        self._update_all()
        tau = torque * self.r_max / self.J_xy
        return tau

    def _update_all(self):
        """Update all properties."""
        self.read_values_from_file()
        self._calculate_J_xy()

    def CalculateMaxStress2DinAxialForceLoading(self, force: float, torque: float, printing=False, plotting=False):
        """
        Calculate maximum normal and shear stresses under axial force loading.

        :param force: Applied axial force.
        :param torque: Applied torque.
        :param printing: Flag to print values.
        :param plotting: Flag to plot Mohr's circle.
        """
        self._update_all()
        sigma = self._calculateAxialStress_z(force)
        tau = self._calculateTorsion(torque)

        stress_tensor = np.array([
            [sigma, tau],
            [tau, 0]
        ])
        max_normal, max_shear = mohr2d.mohr(stress_tensor, plot=plotting, printing=printing)
        self.max_normal_stress.append(max_normal)
        self.max_shear_stress.append(max_shear)

    def _calculateMomentFromShearingForce(self, force: float):
        """Calculate moment induced by shearing force."""
        moment = force * self.L
        return moment

    def _calculateTransverseShear(self, force):
        """Calculate transverse shear stress."""
        shear_stress = 2 * force * self.A_min
        return shear_stress

    def _calculateBendingStress(self, moment, I):
        """Calculate bending stress."""
        stress = moment * self.r_max / I
        return stress

    def CalculateMaxStress2DinShearForceLoading(self, force: float, torque: float, printing=False, plotting=False):
        """
        Calculate maximum normal and shear stresses under shear force loading.

        :param force: Applied shear force.
        :param torque: Applied torque.
        :param printing: Flag to print values.
        :param plotting: Flag to plot Mohr's circle.
        """
        self._update_all()
        moment = self._calculateMomentFromShearingForce(force=force)
        tau = self._calculateTorsion(torque=torque)
        bending_stress = self._calculateBendingStress(moment, self.Izz)
        transverse_shear = self._calculateTransverseShear(force)
        
        stress_tensor = np.array([
            [bending_stress, tau],
            [tau, 0]
        ])
        max_normal, max_shear = mohr2d.mohr(stress_tensor, plot=plotting, printing=printing)
        self.max_normal_stress.append(max_normal)
        self.max_shear_stress.append(max_shear)

    def __str__(self):
        return f"Name: {self.name}\nV: {self.V}, A: {self.A_min}, L: {self.L}, r_max: {self.r_max}, r_min: {self.r_min} Ixx: {self.Ixx}, Iyy: {self.Iyy}, Izz: {self.Izz}, Ixy: {self.Ixy}, Ixz: {self.Ixz}, Iyz: {self.Iyz}, x: {self.x}, y: {self.y}, z: {self.z}"
