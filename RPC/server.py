from xmlrpc.server import SimpleXMLRPCServer
import numpy as np

def get_linha(matriz, linha):
    return (matriz[linha])

def get_coluna(matriz, coluna):
    return ([i[coluna] for i in matriz])

def multiplica(A,B,linA,colA):
    C = []
    for i in range(linA):
        C.append([])
        for j in range(colA):
            listMult = [x*y for x, y in zip(get_linha(A, i), get_coluna(B, j))]
            C[i].append(sum(listMult))
    np.savetxt('rpcC.txt', C, fmt='%.4f')
    return C


server = SimpleXMLRPCServer(('localhost', 6000))
print('Listening on port 6000...')

server.register_function(multiplica, 'multiplica')


server.serve_forever()