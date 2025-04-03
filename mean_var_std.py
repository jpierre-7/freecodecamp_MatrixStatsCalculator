'''
freecodecamp Mean-Variance-Standard Deviation Calculator
John Pierre

This program calculates the mean, variance, standard deviation, max, min, and sum of a matrix.
'''

import numpy as np

def calculate(list_input):
    #Input validation
    if not isinstance(list_input, list) or len(list_input) != 9:
        raise ValueError("Input must be a list of nine numbers.")
    
    # Converting list to numpy array
    matrix = np.array(list_input).reshape(3, 3)
    
    # Calculating mean, variance, standard deviation, max, min, and sum for rows, columns, and 
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),    # Columns
            matrix.mean(axis=1).tolist(),    # Rows
            matrix.mean().item()             # Flattened Matrix
        ],
        'variance': [
            matrix.var(axis=0).tolist(),    # Columns
            matrix.var(axis=1).tolist(),    # Rows
            matrix.var().item()             # Flattened Matrix
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),    # Columns
            matrix.std(axis=1).tolist(),    # Rows
            matrix.std().item()             # Flattened Matrix
        ],
        'max': [
            matrix.max(axis=0).tolist(),    # Columns
            matrix.max(axis=1).tolist(),    # Rows
            matrix.max().item()             # Flattened Matrix
        ],
        'min': [
            matrix.min(axis=0).tolist(),    # Columns
            matrix.min(axis=1).tolist(),    # Rows
            matrix.min().item()             # Flattened Matrix
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),    # Columns
            matrix.sum(axis=1).tolist(),    # Rows
            matrix.sum().item()             # Flattened Matrix
        ]
    }

    return calculations
