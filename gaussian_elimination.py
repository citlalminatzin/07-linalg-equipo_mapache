A=[[1,2,-2,1],
[4,5,-7,6],
[5,25,-15,-3],
[6,-12,-6,22]]

def gaussian_elimination(M: list[list[float]]):
    n = len(M)
    A = [fila[:] for fila in M]

    for i in range(n):
        # Pivote: Se busca el renglon o fila con el valor máximo en la columna i
        fila_max = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[fila_max][i]):
                fila_max = k
        
        # Intercambio de renglones
        A[i], A[fila_max] = A[fila_max], A[i]
        
        # Eliminación 
        if abs(A[i][i]) > 1e-15:
            for j in range(i + 1, n):
                factor = A[j][i] / A[i][i]
                for k in range(i, n):
                    A[j][k] -= factor * A[i][k]
                # Pasamos el cero debajo del pivote 
                A[j][i] = 0.0
                
    return A


def triang_sup_to_diag(M:list[list[float]]):
    """
    Dada una matriz M triangular superior 
    regresa una matriz diagonal
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

def main():
    print("Matriz original:")
    for fila in A: print(fila)
    
    resultado = diag(A)
    
    print("\nDiagonal resultante:")
    print(resultado)

if __name__ == "__main__":
    main()
    