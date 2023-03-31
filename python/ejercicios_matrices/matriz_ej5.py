"""5. Leer una matriz 4x3 entera, calcular la suma de los elementos de cada fila y determinar
cuál es la fila que tiene la mayor suma."""

try:
	print("Matriz 4*3")

	# Leer la matriz 4x3 
	matriz = []
	for i in range(4):
	    fila = []
	    for j in range(3):
	        num = int(input(f"Ingrese un numero entero para la posicion: [{i} ,{j}] "))
	        fila.append(num)
	    matriz.append(fila)

	print(matriz)

	# Calculamos la suma de los elementos de cada fila y determinamos la fila con la mayor suma
	max_suma = 0
	max_fila = 0
	for fil_i in range(len(matriz)):
	    suma_fila = 0
	    for col_j in range(len(matriz[fil_i])):
	        suma_fila += matriz[fil_i][col_j]
	    if suma_fila > max_suma:
	        max_suma = suma_fila
	        max_fila = fil_i

	    print(f"La suma de la fila {fil_i} es: {suma_fila}")

	# Imprimimos la fila con la mayor suma
	print(f"La fila con la mayor suma es la fila {max_fila}.")

except ValueError:
	print("El dato ingresado debe ser númerico")  