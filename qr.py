#!/usr/bin/env python

#Realiza la factorización QR de una matriz

from gram_schmidt import transpose, matmul, proj, normalize

def qr(M:list[list[float]])->tuple[list[list[float]], list[list[float]]]:
    #Realiza la factorización QR de una matriz M
    cols = transpose(M)
    n= len(cols)
    Q_cols = []

    for j, a in enumerate(cols):
        #restamos las proyecciones de a sobre los q anteriores
        u= list(a)
        for q in Q_cols:
            u = [ui - pi for ui, pi in zip(u, proj(u, q))]
        Q_cols.append(normalize(u))

    Q = transpose(Q_cols)
    R = matmul(transpose(Q), M)
    return Q,R