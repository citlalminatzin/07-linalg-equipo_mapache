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
def leer_matriz():
    while True:
        try:
            n = int(input("Número de filas: "))
            m = int(input("Número de columnas: "))
            
            if n <= 0 or m <= 0:
                print("Las dimensiones deben ser positivas.")
                continue
            
            break
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")
    
    A = []
    for i in range(n):
        while True:
            try:
                fila = list(map(float, input(f"Fila {i+1} (separa por espacios): ").split()))
                
                if len(fila) != m:
                    print(f"Ingresa exactamente {m} valores.")
                    continue
                
                A.append(fila)
                break
            except ValueError:
                print("Entrada inválida. Usa solo números.")
    
    return A

def mostrar_matriz(A):
    for fila in A:
        print(fila)
        
def ejercicio1():
    print("\n--- EJERCICIO 1: DIAGONALIZACIÓN ---")
    print("1. Usar matriz de ejemplo")
    print("2. Ingresar matriz")
    print("3. Regresar")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        A = [
            [1, 2, -2, 1],
            [4, 5, -7, 6],
            [5, 25, -15, -3],
            [6, -12, -6, 22]
        ]
        print("\nUsando matriz de ejemplo...")

    elif opcion == "2":
        A = leer_matriz()

    elif opcion == "3":
        return

    else:
        print("Opción inválida.")
        return

    if len(A) != len(A[0]):
        print("La matriz debe ser cuadrada.")
        return

    print("\nMatriz:")
    mostrar_matriz(A)

    print("\nDiagonalización:")
    resultado = diag(A)
    print(resultado)


def ejercicio2():
    print("\n--- EJERCICIO 2: FACTORIZACIÓN LU ---")
    A = leer_matriz()

    print("\nMatriz:")
    mostrar_matriz(A)

    print("\nFactorización LU:")
    L, U = lu(A)

    print("\nL:")
    for fila in L:
        print(fila)

    print("\nU:")
    for fila in U:
        print(fila)

    print("\nComprobación L * U:")
    resultado = matmul(L, U)
    for fila in resultado:
        print(fila)


def ejercicio3():
    print("\n--- EJERCICIO 3: FACTORIZACIÓN QR ---")
    A = leer_matriz()

    print("\nMatriz:")
    mostrar_matriz(A)

    print("\nFactorización QR:")
    Q, R = qr(A)

    print("\nQ:")
    for fila in Q:
        print(fila)

    print("\nR:")
    for fila in R:
        print(fila)


def menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Ejercicio 1: Diagonalización")
    print("2. Ejercicio 2: Factorización LU")
    print("3. Ejercicio 3: Factorización QR")
    print("4. Salir")


def main():
    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejercicio1()

        elif opcion == "2":
            ejercicio2()

        elif opcion == "3":
            ejercicio3()

        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__": 
    main()