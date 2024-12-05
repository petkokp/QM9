from numba import jit
import numpy as np

@jit(nopython=True)
def calculate_coulomb_matrix(atomic_numbers, coordinates):
    num_atoms = len(atomic_numbers)
    coulomb_matrix = np.zeros((num_atoms, num_atoms))

    for i in range(num_atoms):
        for j in range(num_atoms):
            if i == j:
                # Diagonale principale
                coulomb_matrix[i, j] = 0.5 * atomic_numbers[i] ** 2.4
            else:
                # Elementi fuori diagonale
                distance = np.linalg.norm(coordinates[i] - coordinates[j])
                coulomb_matrix[i, j] = atomic_numbers[i] * atomic_numbers[j] / distance

    return coulomb_matrix