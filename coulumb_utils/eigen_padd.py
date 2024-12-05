import numpy as np

def compute_eigenvalues(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    return eigenvalues

def padd_eig(matrix, resolution):
    padded_matrix = np.zeros((resolution, 1))
    padded_matrix[: matrix.shape[0], : matrix.shape[1]] = matrix

    return padded_matrix

def padd_matrix(matrix, resolution):
    padded_matrix = np.zeros((resolution, resolution))
    padded_matrix[: matrix.shape[0], : matrix.shape[1]] = matrix

    return padded_matrix