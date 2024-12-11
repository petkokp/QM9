import numpy as np

def normalize_min_max(matrix):
    return (matrix - np.min(matrix)) / (np.max(matrix) - np.min(matrix))

def log_normalize(matrix):
    return np.log1p(np.abs(matrix))