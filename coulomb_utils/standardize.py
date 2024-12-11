import numpy as np

def standardize_matrix(matrix):
    mean = np.mean(matrix, axis=0)
    std_dev = np.std(matrix, axis=0)
    standardized_matrix = (matrix - mean) / std_dev

    # scaler = StandardScaler()
    # standardized_matrix = scaler.fit_transform(matrix)
    return standardized_matrix