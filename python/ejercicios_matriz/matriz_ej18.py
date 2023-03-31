"""18. Leer una matriz 5x5 entera y determinar en qué posición exacta se encuentra el mayor
múltiplo de 8."""

try:
	print("Matriz 5*5")

	# Leemos la matriz 5*4
	matriz = [] # Definimos la matriz
	for i in range(5):  # Recorremos cada fila de la matriz
		fila = []
		for j in range(5): # Recorrer cada columna de la fila
			num = int(input(f"Ingrese un numero entero para la posicion: [{i} ,{j}] ")) # Pedimos al usuario que ingrese un número
			fila.append(num) # Agregamos el número a la fila
		matriz.append(fila) # Agregamos la fila a la matriz

	# buscamos cuantos numeros de la matriz son multiplos de 5
	max_multiplo_8 = 0
	pos_multiplo = 0
	multi_8 = []
	for fil_k in range(len(matriz)):
		for col_l in range(len(matriz[fil_k])):
			#comparamos para saber que numeros son multiplos de 8 y cual es el mayor
			if matriz[fil_k][col_l] % 8 == 0 and matriz[fil_k][col_l] > max_multiplo_8: 
				max_multiplo_8 = matriz[fil_k][col_l]
				pos_multiplo = fil_k, col_l
				multi_8.append(matriz[fil_k][col_l]) #los que sean multiplos de 8 los agregamos a una lista


	# Imprimimos la matriz y la el numero mayor multiplo de 8
	print(matriz)

	if max_multiplo_8 != 0:
		print(f"multiplos de 8: {multi_8}")
		print(f"El numero mayor multiplo de 8 ({max_multiplo_8}) se encuentra en la posicion {pos_multiplo}")
	else:
		print("No hay multiplos de 8 ")

except ValueError:
	print("El dato ingresado debe ser númerico")   