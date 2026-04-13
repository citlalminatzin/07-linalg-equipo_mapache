#!/usr/bin/env python

from collections.abc import Sequence
from gram_schmidt import matmul
from gaussian_elimination import diag
from lu import lu
from qr import qr

# linspace obtenido de (https://code.activestate.com/recipes/579000/)
class linspace(Sequence):
    """linspace(start, stop, num) -> linspace object
    
    Return a virtual sequence of num numbers from start to stop (inclusive).
    
    If you need a half-open range, use linspace(start, stop, num+1)[:-1].
    """
    
    def __init__(self, start, stop, num):
        if not isinstance(num, numbers.Integral) or num <= 1:
            raise ValueError('num must be an integer > 1')
        self.start, self.stop, self.num = start, stop, num
        self.step = (stop-start)/(num-1)
    def __len__(self):
        return self.num
    def __getitem__(self, i):
        if isinstance(i, slice):
            return [self[x] for x in range(*i.indices(len(self)))]
        if i < 0:
            i = self.num + i
        if i >= self.num:
            raise IndexError('linspace object index out of range')
        if i == self.num-1:
            return self.stop
        return self.start + i*self.step
    def __repr__(self):
        return '{}({}, {}, {})'.format(type(self).__name__,
                                       self.start, self.stop, self.num)
    def __eq__(self, other):
        if not isinstance(other, linspace):
            return False
        return ((self.start, self.stop, self.num) ==
                (other.start, other.stop, other.num))
    def __ne__(self, other):
        return not self==other
    def __hash__(self):
        return hash((type(self), self.start, self.stop, self.num))  

def main():

    A = [
        [1, 2, -2, 1],
        [4, 5, -7, 6],
        [5, 25, -15, -3],
        [6, -12, -6, 22]
    ]

    print("Matriz original:")
    for fila in A:
        print(fila)

    # Ejercicio 1: Diagonalización
    d = diag(A)
    print("\nDiagonal:")
    print(d)

    #Ejercicio : LU
    L, U = lu(A)
    print("\nL:")
    for fila in L:
        print(fila)

    print("\nU:")
    for fila in U:
        print(fila)

    # Comprobación con LU
    print("\nComprobación L * U:")
    resultado = matmul(L, U)
    for fila in resultado:
        print(fila)

    # Ejercicio 3: QR
    Q, R = qr(A)
    print("\nQ:")
    for fila in Q:
        print(fila)

    print("\nR:")
    for fila in R:
        print(fila)

if __name__ == "__main__":
    main()
