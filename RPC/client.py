import xmlrpc.client
import numpy as np

# A = np.loadtxt(r'testA.txt', encoding = 'utf-8')
# B = np.loadtxt(r'testA.txt', encoding = 'utf-8')

A = [[1,2,3],[3,4,5]]
B = [[1,2,3],[3,4,5]]

linA = len(A)
colA = len(A[0])

with xmlrpc.client.ServerProxy('http://localhost:6000/') as proxy:
    C = proxy.multiplica(A,B,linA,colA)
    print(C)
    np.savetxt('rpcC.txt', C, fmt='%.4f')
