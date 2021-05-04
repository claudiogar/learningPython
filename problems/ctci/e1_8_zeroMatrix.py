#CTCI E1.8: Write an algorithm such that if an element in an M x N matrix is 0, its entire row and column are set to 0.

import numpy as np

def zeroMatrix(matr: np.ndarray) -> np.ndarray:
    rows = set()
    cols = set()

    # keep track of rows and cols containing 0s
    # O(N x M)
    n_rows = np.shape(matr)[0]
    n_cols = np.shape(matr)[1]
    for i in range(0, n_rows):
        for j in range(0, n_cols):
            if matr[i,j] == 0:
                rows.add(i)
                cols.add(j)
    
    for i in range(0, n_rows):
        for j in range(0, n_cols):
            if i in rows or j in cols:
                matr[i,j] = 0
    
    return matr


input = np.array([[1,2,3], [4,0,6]])

print(zeroMatrix(input))
