import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16 


def mohr(S):
    """Plot Mohr circle for a 2D tensor"""
    S11 = S[0][0] 
    S12 = S[0][1] 
    S22 = S[1][1] 
    center = [(S11 + S22)/2.0, 0.0]
    radius = np.sqrt((S11 - S22)**2/4.0 + S12**2)
    Smin = center[0] - radius
    Smax = center[0] + radius

    print("Minimum Normal Stress: %g" % Smin)
    print("Maximum Normal Stress: %g" % Smax)
    print("Average Normal Stress: %g" % center[0])
    print("Minimum Shear Stress: %g" % -radius)
    print("Maximum Shear Stress: %g" % radius)

    circ = plt.Circle((center[0],0), radius, facecolor='#cce885', lw=3,
    edgecolor='#5c8037') 
    plt.axis('image')
    ax = plt.gca() 
    ax.add_artist(circ)
    ax.set_xlim(Smin - .1*radius, Smax + .1*radius)
    ax.set_ylim(-1.1*radius, 1.1*radius)
    plt.plot([S22, S11], [S12, -S12], 'ko')
    plt.plot([S22, S11], [S12, -S12], 'k')
    plt.plot(center[0], center[1], 'o', mfc='w')
    plt.text(S22 + 0.1*radius, S12, 'A')
    plt.text(S11 + 0.1*radius, -S12, 'B')
    plt.xlabel(r"$\sigma$", size=18)
    plt.ylabel(r"$\tau$", size=18) 
    plt.show()
    return None

if __name__ == "__main__":
    S = np.array([[-91.287, 0.669],[0.669, -91.287]])
    mohr(S)

    plt.figure()
    S2 = np.array([[-91.287, 25.465],[25.465, 126.063]])
    mohr(S2)
    plt.show()