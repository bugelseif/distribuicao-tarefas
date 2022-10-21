import numpy as np
import hash

# A = [[1,2,3],[3,4,5]]
# B = [[1,2,3],[3,4,5]]
A = np.loadtxt(r'testA.txt', encoding = 'utf-8')
B = np.loadtxt(r'testA.txt', encoding = 'utf-8')
C = []
linA = len(A)
colA = len(A[0])
linB = len(B)
colB = len(B[0])

def get_linha(matriz, linha):
    return (matriz[linha])

def get_coluna(matriz, coluna):
    return ([i[coluna] for i in matriz])

for i in range(linA):
    C.append([])
    for j in range(colA):
        listMult = [x*y for x, y in zip(get_linha(A, i), get_coluna(B, j))]
        C[i].append(sum(listMult))
np.savetxt('linearC.txt', C, fmt='%.4f')

# print(hash.calc_hash('matrizes\matA.txt')) # d992dd8ffb4d30cc30141ecb61c1d213 -ok
# print(hash.calc_hash('matrizes\matB.txt')) # fdad8d9422b05e7e4f5e94c03b14cb1c -ok
# print(hash.calc_hash('matC.txt')) # 0d53e92899458712caa521714808b47b | 38af9555e71e9d02b55911d827cfd507 -no