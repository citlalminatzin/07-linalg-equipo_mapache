def lu(M:list[list[float]]):
    #Dada una matriz M regresa su factorización LU
    n = len(M)
    L = [[0]*n for _ in range(n)]
    for i in range(n):
        L[i][i] = 1

    U = [fila[:] for fila in M]

    for i in range(n):

        # PIVOTEO: buscar mejor pivote en columna i
        fila_max = i
        for k in range(i+1, n):
            if abs(U[k][i]) > abs(U[fila_max][i]):
                fila_max = k

        # Intercambiar filas en U
        if fila_max != i:
            U[i], U[fila_max] = U[fila_max], U[i]

            # Intercambiar en L (solo lo ya calculado)
            for k in range(i):
                L[i][k], L[fila_max][k] = L[fila_max][k], L[i][k]

        # Verificación de pivote
        if abs(U[i][i]) < 1e-10:
            raise ValueError("No se puede factorizar (pivote cero)")

        # Eliminación
        for j in range(i+1, n):
            factor = U[j][i] / U[i][i]
            L[j][i] = factor

            for k in range(i, n):
                U[j][k] -= factor * U[i][k]

    return L, U

def main():
    ...

if __name__ == "__main__":
    main()