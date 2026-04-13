def gaussian_elimination(M: list[list[float]]):
    """ Dada una matriz M regresa una matriz triangular
    superior usando eliminacion gaussiana usando un pivote parcial. """
    n = len(M)
    A = [fila[:] for fila in M]

    for i in range(n):
        # Pivote: Se busca el renglon o fila con el valor máximo en la columna i
        fila_max = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[fila_max][i]):
                fila_max = k
        
        A[i], A[fila_max] = A[fila_max], A[i]
        
        if abs(A[i][i]) > 1e-15:
            for j in range(i + 1, n):
                factor = A[j][i] / A[i][i]
                for k in range(i, n):
                    A[j][k] -= factor * A[i][k]
                
                A[j][i] = 0.0
                
    return A


def triang_sup_to_diag(M:list[list[float]]):
    """
    Dada una matriz M triangular superior 
    regresa una matriz diagonal.
    """
    n = len(M)
    A = [row[:] for row in M]

    for i in range(n - 1, -1, -1):
        if abs(A[i][i]) > 1e-15:
            for j in range(i - 1,-1,-1):
                factor = A[j][i] / A[i][i]
                for k in range(i,n):
                    A[j][k] -= factor * A[i][k]
                    A[j][i] = 0.0
    return A

def diag(M:list[list[float]]):
    """Dada una matriz regresa una matriz diagonalizada"""
    n = len(M)
    Y = gaussian_elimination(M)
    matriz_diagonal = triang_sup_to_diag(Y)
    diagonal = [] 
    for i in range(n): 
        diagonal.append(matriz_diagonal[i][i]) 
    return diagonal

''' Seccion interactiva para el usuario. Permite ingresar matrices y ejecutar las funciones anteriores '''

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


def menu():
    print("1. Ejemplo ejercicio 1.")
    print("2. Ingresar una matriz")
    print("3. Salir")


def main():
    while True:
        menu()
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
            A= leer_matriz()
        
        elif opcion == "3":
            print("Saliendo...")
            break
        
        else:
            print("Opción inválida.")
            continue
        
        # Validación: matriz cuadrada
        if len(A) != len(A[0]):
            print("\nError: La matriz debe ser cuadrada.")
            continue
        
        print("\nMatriz original:")
        mostrar_matriz(A)
        
        resultado = diag(A)
        
        print("\nDiagonal resultante:")
        print(resultado)


if __name__ == "__main__":
    main()
    
