[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/R6N_zRdu)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23491667)
# Práctica 7. Diagonalización Por Método De Gauss, Factorización LU y Factorización QR

## Integrantes
- Alba Pérez Paulina
- Galeana Morán Miguel Ángel
- Herrera Barrera Joyce


## Uso e instalación
No se necesita instalar ninguna libreria externa dado que se implementaron manualmente las operaciones matriciales. Unicamente se necesita Python.

Se necesita abrir la terminal y correr: python main.py 

## Ejercicio 1

Implementar el método de eliminación Gaussiana para diagonalizar una matriz cuadrada.

La matriz con la que estaremos trabajando es:

![Matriz A](Imagenes/mat_A.png)

Es importante resaltar que las siguientes matrices tienen redonde de 4 decimas, sin embargo, en el código, los cálculos se representan con mayor exactitud. Esto con la intención de mostrar un visual más limpio.

Matriz Diagonal Resultante:

![Diagonal](Imagenes/Diagonal.png)

## Ejercicio 2

Programar una función que reciba la matriz cuadrada de tamaño n × n, A, que además sea
triangular superior y que se encargue de eliminar todos los elementos superiores a la diagonal usando una
vez más el método de eliminación Gaussiana.

Matriz Resultante L:

![Matriz L](Imagenes/mat_L.png)

Matriz Resultante U:

![Matriz U](Imagenes/mat_U.png)

Debido a que se encontró un pivote 0, se tuvo que recurrir al pivoteo parcial (intercambiar las filas), lo que es igual a multiplicar nuestra matriz original por una matri de permutación P: PA= LU.

Es por ello que al multiplicar LU tenemos un reenglón intercambiado.

Matriz Resultante LU:

![Matriz LU](Imagenes/mat_LU.png)

## Ejercicio 3

Programar la descomposición QR de una matriz A usando el Proceso de Gram-Schmidt.

Matriz Resultante Q:

![Matriz Q](Imagenes/mat_Q.png)

Matriz Resultante R:

![Matriz R](Imagenes/mat_R.png)

## Conclusión
Esta práctica nos ayudó a entender los procedimientos mostrados y llevados a cabo en código. Nuestra mayor dificultad fue encontrar un pivote que fuese 0, pero consideramos que pudimos resolverlo del mejor modo. Nuestro aprendizaje en este trabajo ha sido el ser meticulosos con el código para obtrener los resultados que esperamos y el orden con nuestra práctica para que el trabajo en equipo sea fluido.