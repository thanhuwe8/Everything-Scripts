import numpy as np
import pandas as pd

# Cholesky Factorization Algorithms
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


# Unit testing
# Test 1
mat2 = np.array([[1.0,0.3,0.3],
                    [0.3,1.0,0.3],
                    [0.3,0.3,1.0]])
np.linalg.cholesky(mat2)
mycholesky(mat2)

# Test 2
mat2 = np.array([
    [1.0, 0.3, -0.2, 0.4],
    [0.3, 1.0, -0.3, 0.1],
    [-0.2, -0.3, 1.0, 0.5],
    [0.4, 0.1, 0.5, 1.0]])
np.linalg.cholesky(mat2)
mycholesky(mat2)


# Portfolio simulation
'''
Simulate 252 days of return for 3 assets with high correlation
'''
covmat = np.array([[1,0.8,0.8],
                    [0.8,1,0.8],
                    [0.8,0.8,1]])
A = mycholesky(covmat)
np.linalg.cholesky(covmat)
print(A)

sim_n = 260
Y = np.zeros([3,sim_n])
Z = np.random.normal(0.0, 1.0, [3, sim_n])
S = np.zeros([3,sim_n+1])
S_0 = [45,50,55]
S[:,0] = S_0

for i in range(0, sim_n):
    Y[:,i] = np.matmul(Z[:,i],A)







