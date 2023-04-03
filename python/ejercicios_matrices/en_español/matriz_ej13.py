"""13. Leer una matriz 5x3 entera y determinar en qué columna está el mayor número que
comienza con el dígito 4."""

try:
	print("Matriz 5*3")

	# Leer la matriz 5*3
	matriz = []
	for i in range(5):
		fila = []
		for j in range(3):
			num = int(input(f"Ingrese un numero entero para la posicion: [{i} ,{j}] "))
			fila.append(num)
		matriz.append(fila)


	# Encontramos en que columna esta el mayor número que comienza en 4 en la matriz
	max_inicia_4 = 0
	col = 0
	for fil_k in range(len(matriz)):
		for col_l in range(len(matriz[fil_k])):

			if matriz[fil_k][col_l] // 10 == 4 and matriz[fil_k][col_l] > max_inicia_4: # NOTA: Si el número en la celda de la matriz es igual a 4,
				max_inicia_4 = matriz[fil_k][col_l]										# esta expresión no lo considerará como un número que inicia con 4.
				col = col_l
	
	# Imprimir la matriz y la columna en  donde se encuentra el mayor número que comienza en 4
	print(matriz)
	if max_inicia_4 == 0:
		print("No hay un numero mayor que comience en 4")
	else:
		print(f"El mayor número que comienza en 4 es: ({max_inicia_4}) se encuentra en la fila {col}")

except ValueError:
	print("El dato ingresado debe ser númerico")  