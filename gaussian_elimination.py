def gaussian_elimination(M: list[list[float]]):
    n = len(M)
    A = [fila[:] for fila in M]

    for i in range(n):
        # Pivote: Se busca el renglon o fila con el valor máximo en la columna i
        fila_max = i
        for k in range(i + 1, n):
            if math.abs(A[k][i]) > math.abs(A[fila_max][i]):
                fila_max = k
        
        # Intercambio de renglones
        A[i], A[fila_max] = A[fila_max], A[i]
        
        # Eliminación 
        if math.abs(A[i][i]) > 1e-15:
            for j in range(i + 1, n):
                factor = A[j][i] / A[i][i]
                for k in range(i, n):
                    A[j][k] -= factor * A[i][k]
                # Pasamos el cero debajo del pivote 
                A[j][i] = 0.0
                
    return A
    ...
def triang_sup_to_diag(M:list[list[float]]):
    """
    Dada una matriz M traingular superior 
    regresa una matriz diagonal
    """
    ...
def diag(M:list[list[float]]):
    """Dada una matriz regresa una matriz diagonalizada"""
    ...
def main():
    ...
if __name__ == "__main__":
    main() 
