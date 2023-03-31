"""3. Leer una matriz 3x4 entera y determinar en qué posiciones exactas se encuentran los
números pares."""

try:
	print("Matriz 3*4")

	matriz = []
	num_par = 0
	
	for fil_i in range(3): #leemos la matriz segun los parametros
		fila = []
		for col_j in range(4):
			num = int(input(f"Ingrese un numero entero para la posicion: [{fil_i} ,{col_j}] "))
			fila.append(num)
		matriz.append(fila)

	print(matriz) #imprimimos la matriz

	for fil_i in range(len(matriz)):  #recorremos la matriz
		for col_j in range(len(matriz[fil_i])):

			if matriz[fil_i][col_j] % 2 == 0: #comparamos la matriz para obtener los numeros pares y sus posiciones
				num_par = matriz[fil_i][col_j]

				print(f"El numero par {num_par} se encuentra en la posicion {fil_i, col_j} ") #imprimimos los pares con sus posiciones
		
except ValueError:
	print("El dato ingresado debe ser númerico") 