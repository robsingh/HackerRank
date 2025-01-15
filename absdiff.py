import numpy as np

def diagdiff(arr):
    n = len(arr)
    primary_diagonal = 0
    secondary_diagonal = 0

    for i in range(n):
        primary_diagonal += arr[i][i]
        secondary_diagonal += arr[i][n-i-1]

    return abs(primary_diagonal - secondary_diagonal)


arr = np.array([ [1,2,3], [4,5,6], [9,8,9]])
print(diagdiff(arr))

