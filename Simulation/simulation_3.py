import numpy as np
import pandas as pd



# Cholesky Factorization Algorithms
COVMAT = np.array([[1.0,0.3,0.3],
                    [0.3,1.0,0.3],
                    [0.3,0.3,1.0]])

mat2 = COVMAT.copy()
AMAT = np.linalg.cholesky(mat2)


def mycholesky(mat):
    result = np.zeros([len(mat), len(mat)])
    v = np.zeros(len(mat))
    for i in range(len(mat)):
        for j in range(i,len(mat)):
            v[j] = mat[j,i]
            for k in range(i):
                v[j] = v[j] - result[j,k]*result[i,k]
            result[j,i] = v[j]/np.sqrt(v[i])
    return(result)

mycholesky(mat2)


mat3 = np.array([
    [1.0, 0.3, -0.2, 0.4],
    [0.3, 1.0, -0.3, 0.1],
    [-0.2, -0.3, 1.0, 0.5],
    [0.4, 0.1, 0.5, 1.0]]
)

np.linalg.cholesky(mat3)
mycholesky(mat3)
