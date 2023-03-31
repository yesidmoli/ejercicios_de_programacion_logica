"""16. Leer una matriz 5x4 entera y determinar cuántos números almacenados en ella tienen
un solo dígito."""

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

	# buscamos cuantos numeros de la matriz terminan en 34
	cont = 0
	for fil_k in range(len(matriz)):
		for col_l in range(len(matriz[fil_k])):

			if matriz[fil_k][col_l] > -10 and matriz[fil_k][col_l] < 10: #comparamos para saber que numeros tienen un digito(ya sean positivos o negativos)
				cont += 1
	
	# Imprimimos la matriz y la cantidad de numeros que tienen solo un digito
	print(matriz)

	if cont != 0:
		print(f"En la matriz hay ({cont}) numeros que tienen un digito ")
	else:
		print("La matriz no tiene almacenado numeros con un solo digito")

except ValueError:
	print("El dato ingresado debe ser númerico")   