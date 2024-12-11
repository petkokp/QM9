import numpy as np

def sort_by_row_norm(matrix):
    row_norms = np.linalg.norm(matrix, axis=1)
    sorted_indices = np.argsort(-row_norms)
    sorted_matrix = matrix[sorted_indices][:, sorted_indices]
    return sorted_matrix

def sort_by_atomic_number(atomic_numbers, matrix):
    sorted_indices = np.argsort(-atomic_numbers)
    sorted_matrix = matrix[sorted_indices][:, sorted_indices]
    return sorted_matrix

def randomly_sort_matrix(matrix):
    permutation = np.random.permutation(matrix.shape[0])
    matrix_sorted = matrix[permutation, :][:, permutation]
    return matrix_sorted