import threading
import numpy as np

A = np.loadtxt(r'testA.txt', encoding = 'utf-8')
B = np.loadtxt(r'testA.txt', encoding = 'utf-8')


linA = len(A)
colA = len(A[0])

matriz = np.array_split(A, 2)
m1 = matriz[0]
m2 = matriz[1]

def get_linha(matriz, linha):
    return (matriz[linha])

def get_coluna(matriz, coluna):
    return ([i[coluna] for i in matriz])

def tarefa1():
    C = []
    for i in range(int(linA/2)):
        C.append([])
        for j in range(colA):
            listMult = [x*y for x, y in zip(get_linha(m1, i), get_coluna(B, j))]
            C[i].append(sum(listMult))
    np.savetxt('testpt1.txt', C, fmt='%.4f')
    print('fim1')

def tarefa2():
    C = []
    for i in range(int(linA/2)):
        C.append([])
        for j in range(colA):
            listMult = [x*y for x, y in zip(get_linha(m2, i), get_coluna(B, j))]
            C[i].append(sum(listMult))
    np.savetxt('testpt2.txt', C, fmt='%.4f')
    print('fim2')


t1 = threading.Thread(target=tarefa1)
t2 = threading.Thread(target=tarefa2)

t1.start()
t2.start()

t1.join()
t2.join()