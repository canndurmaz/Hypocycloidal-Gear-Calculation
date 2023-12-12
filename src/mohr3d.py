import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigvalsh
from matplotlib import rcParams
 
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16 


def plot_mohr3d(S):
    r"""Plot 3D Mohr circles."""
    
    S3, S2, S1 = eigvalsh(S)

    R_maj = 0.5*(S1 - S3)
    cent_maj = 0.5*(S1+S3)
    
    R_min = 0.5*(S2 - S3)
    cent_min = 0.5*(S2 + S3)
    
    R_mid = 0.5*(S1 - S2)
    cent_mid = 0.5*(S1 + S2)
    
    circ1 = plt.Circle((cent_maj,0), R_maj, facecolor='#cce885', lw=3,
                       edgecolor='#5c8037')
    circ2 = plt.Circle((cent_min,0), R_min, facecolor='w', lw=3,
                       edgecolor='#15a1bd')
    circ3 = plt.Circle((cent_mid,0), R_mid, facecolor='w', lw=3,
                       edgecolor='#e4612d')
    plt.axis('image')
    ax = plt.gca()
    ax.add_artist(circ1)
    ax.add_artist(circ2)
    ax.add_artist(circ3)
    ax.set_xlim(S3 - .1*R_maj, S1 + .1*R_maj)
    ax.set_ylim(-1.1*R_maj, 1.1*R_maj)
    plt.xlabel(r"$\sigma$", size=18)
    plt.ylabel(r"$\tau$", size=18)
    #plt.savefig('Mohr_circle_3D.svg')
    plt.show()

def plot_mohr3d_(array):
    plt.figure()
    plot_mohr3d(array)
    plt.show()

if __name__ == "__main__":
    S=np.array([
        [124,-57,67],
        [-57,0,0],
        [67,0,0]
    ])
    plot_mohr3d_(S)