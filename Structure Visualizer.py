import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_molecule(structure):
    atoms = ['H', 'C', 'O', 'N']
    colors = {'H': 'gray', 'C': 'black', 'O': 'red', 'N': 'blue'}

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for atom, coords in structure.items():
        ax.scatter(coords[0], coords[1], coords[2], color=colors[atom], s=100)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

molecule_structure = {'H': np.array([0, 0, 0]), 'O': np.array([1, 0, 0]), 'H': np.array([1, 1, 0])}
visualize_molecule(molecule_structure)
