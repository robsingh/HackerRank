import numpy as np

def flip_matrix(matrix):
    n = len(matrix)
    max_sum = 0

    for i in range(n//2):
        for j in range(n//2):
            max_sum += max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1])
    
    return max_sum


matrix = np.array([[112,42,83,119],[56,125,56,49],[15,78,101,43],[62,98,114,108]])
print(flip_matrix(matrix))