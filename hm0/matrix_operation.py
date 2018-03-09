import sys
import numpy as np

matrixA = np.loadtxt(sys.argv[1], delimiter = ',', ndmin = 2)
matrixB = np.loadtxt(sys.argv[2], delimiter = ',', ndmin = 2)

result = np.matmul(matrixA, matrixB).flatten()
result = np.sort(result)

with open('ans_one.txt', 'w') as f:
    for i in result:
        f.write(str(int(i)) + '\n')
