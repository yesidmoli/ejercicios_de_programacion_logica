"""12. Leer una matriz 5x5 entera y determinar en qué fila está el mayor número terminado
en 6.""" 
try:
	print("Matriz 5*5")

	# Leer la matriz 5*5
	matriz = []
	for i in range(5):
		fila = []
		for j in range(5):
			num = int(input(f"Ingrese un numero entero para la posicion: [{i} ,{j}] "))
			fila.append(num)
		matriz.append(fila)


	# Encontrar el mayor número terminado en 6 en la matriz
	mayor_terminado_6 = 0
	fila = 0
	for fil_k in range(len(matriz)):
		for col_l in range(len(matriz[fil_k])):

			if matriz[fil_k][col_l] % 10 == 6 and matriz[fil_k][col_l] > mayor_terminado_6:
				mayor_terminado_6 = matriz[fil_k][col_l]
				fila = fil_k
	
	# Imprimir la matriz y la fila donde se encuentra el mayor numero terminado en 6
	print(matriz)
	if mayor_terminado_6 == 0:
		print("No hay un numero mayor terminado en 6")
	else:
		print(f"El mayor número terminado en 6 que es: ({mayor_terminado_6}) se encuentra en la fila {fila}")

except ValueError:
	print("El dato ingresado debe ser númerico")  