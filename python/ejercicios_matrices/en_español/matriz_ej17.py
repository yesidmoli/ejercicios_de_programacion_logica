"""17. Leer una matriz 5x4 entera y determinar cuántos múltiplos de 5 hay almacenados en
ella."""
try:
	print("Matriz 5*4")

	# Leemos la matriz 5*4
	matriz = [] # Definimos la matriz
	for i in range(5):  # Recorremos cada fila de la matriz
		fila = []
		for j in range(4): # Recorrer cada columna de la fila
			num = int(input(f"Ingrese un numero entero para la posicion: [{i} ,{j}] ")) # Pedimos al usuario que ingrese un número
			fila.append(num) # Agregamos el número a la fila
		matriz.append(fila) # Agregamos la fila a la matriz

	# buscamos cuantos numeros de la matriz son multiplos de 5
	cont = 0
	multiplos_5 = []
	for fil_k in range(len(matriz)):
		for col_l in range(len(matriz[fil_k])):

			if matriz[fil_k][col_l] % 5 == 0: #comparamos para saber que numeros son multiplos de 5
				cont += 1
				multiplos_5.append(matriz[fil_k][col_l])

	
	# Imprimimos la matriz y la cantidad de numeros que son multiplos de 5
	print(matriz)

	if cont != 0:
		print(f"En la matriz hay ({cont}) numeros que son multiplos de 5 ")
		print(f"Que son: {multiplos_5}")
	else:
		print("La matriz no tiene almacenado numeros multiplos de 5")

except ValueError:
	print("El dato ingresado debe ser númerico")    