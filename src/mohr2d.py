import numpy as np
import matplotlib.pyplot as plt


def mohr(S, plot=False, printing=False):
    """Plot Mohr circle for a 2D tensor"""
    S11 = S[0][0]
    S12 = S[0][1]
    S22 = S[1][1]
    center = [(S11 + S22) / 2.0, 0.0]
    radius = np.sqrt((S11 - S22) ** 2 / 4.0 + S12 ** 2)
    Smin = center[0] - radius
    Smax = center[0] + radius

    if printing:
        print("Minimum Normal Stress: %g" % Smin)
        print("Maximum Normal Stress: %g" % Smax)
        print("Average Normal Stress: %g" % center[0])
        print("Minimum Shear Stress: %g" % -radius)
        print("Maximum Shear Stress: %g" % radius)

    if plot:
        circ = plt.Circle((center[0], 0), radius, facecolor='white', lw=3, edgecolor='black', label='Mohr Circle')
        plt.axis('image')
        ax = plt.gca()
        ax.add_artist(circ)
        ax.set_xlim(Smin - 0.1 * radius, Smax + 0.1 * radius)
        ax.set_ylim(-1.1 * radius, 1.1 * radius)
        plt.plot([S22, S11], [S12, -S12], 'ro-', lw=2, label='Stress Element')  # Red lines
        plt.plot(center[0], center[1], 'bo', label='Points')  # Blue points
        plt.text(S22 + 0.1 * radius, S12, 'A', color='red')
        plt.text(S11 + 0.1 * radius, -S12, 'B', color='red')
        plt.xlabel(r"$\sigma$", size=18)
        plt.ylabel(r"$\tau$", size=18)
        plt.title('Mohr Circle' + f'\nMax Normal Stress: {Smax:.2f}MPa, Max Shear Stress: {radius:.2f}MPa', fontweight='bold')

        plt.legend()
        plt.grid(color='black', linestyle='-', linewidth=0.5)
        plt.show()

    return Smax, radius


if __name__ == "__main__":
    S = np.array([[-91.287, 0.669],[0.669, -91.287]])
    mohr(S)

    plt.figure()
    S2 = np.array([[-91.287, 25.465],[25.465, 126.063]])
    mohr(S2)
    plt.show()