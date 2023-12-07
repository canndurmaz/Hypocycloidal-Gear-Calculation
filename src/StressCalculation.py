import numpy as np

from GearMaterialProperties import GearMaterialProperties


class StressCalculation():
    
    def K_o():# calculates overload factor
        #cho=int(input("Uniform Work:1\nModerate Shock:2\nHeavy Shock:3"))
        #while (cho != 1 or cho !=2 or cho != 3):
        #    cho=int(input("Uniform Work:1\nModerate Shock:2\nHeavy Shock:3"))
        #match cho:
        #    case 1:
        #        return 1.0
        #    case 2:
        #        return 1.25
        #    case 3:
        #        return 1.75
        return 1
    def K_v(Qv:int,V:float):
        B=0.25*(12-Qv)**(2/3)
        A=50+56*(1-B)
        return ((A+np.sqrt(200*V))/(A))**B
    
    def K_s():
        return 1
    
    def K_b(tooth_root:float,tooth_height:float):
        mb=tooth_root/tooth_height
        if mb<1.2:
            return 1.6*np.log(2.242/mb)
        else:
            return 1
    def K_H(face_width:float,pitch_dia:float):
        Cmc=0.8
        Cpf=face_width/(10*pitch_dia)-0.025
        Cpm=1
        Ce=1
        A=0.127
        B=0.0158
        C=-0.930e-4
        F=face_width*39.3701#inch
        Cma=A+B*F+C*F**2
        return 1+Cmc*(Cpf*Cpm+Cma*Ce)

    def Y_J(N:int):
        ans=float(input(f"Enter value from Figure 14.6 of Shigley/Notes to be used ME308 for teeth:{N}:\t"))
        return ans
    def Z_R():
        return 1
    def Z_I():
        return 1
    def Z_E(material:GearMaterialProperties):
        return np.sqrt(1/(np.pi*2*((1-material.poisson**2)/(material.Young))))
    def Y_N(N):
        return 2.3194*N**(-0.0538)
    def Z_N(N):
        return 2.466*N**(-0.056)
    def Y_Theta():
        return 1
    def Y_Z():
        return 1 #%99 reliability