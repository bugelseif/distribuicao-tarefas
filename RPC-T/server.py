from xmlrpc.server import SimpleXMLRPCServer
import numpy as np
import threading

def get_linha(matriz, linha):
    return (matriz[linha])

def get_coluna(matriz, coluna):
    return ([i[coluna] for i in matriz])

def multiplica(A,B,linA,colA):
    matriz = np.array_split(A, 2)
    m1 = matriz[0]
    m2 = matriz[1]

    t1 = threading.Thread(target=tarefa1, args=(linA,colA,m1,B))
    t2 = threading.Thread(target=tarefa2, args=(linA,colA,m2,B))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return 'TEMP'

def tarefa1(linA,colA,m1,B):
    C = []
    for i in range(int(linA/2)):
        C.append([])
        for j in range(colA):
            listMult = [x*y for x, y in zip(get_linha(m1, i), get_coluna(B, j))]
            C[i].append(sum(listMult))
    print('fim')
    return C

def tarefa2(linA,colA,m2,B):
    C1 = []
    for i in range(int(linA/2)):
        C1.append([])
        for j in range(colA):
            listMult = [x*y for x, y in zip(get_linha(m2, i), get_coluna(B, j))]
            C1[i].append(sum(listMult))
    print('fim2')
    return C1

server = SimpleXMLRPCServer(('localhost', 6000))
print('Listening on port 6000...')

server.register_function(multiplica, 'multiplica')

server.serve_forever()