"""2. Leer una matriz 4x4 entera y determinar cuántas veces se repita en ella el número mayor."""
try:
	print("Matriz 4*4")

	matriz = []
	mayor = 0
	pos_mayor = 0
	cont = 0

	for fil_i in range(4): #leemos la matriz segun los parametros
		fila = []
		for col_j in range(4):
			num = int(input(f"Ingrese un numero entero para la posicion: [{fil_i} ,{col_j}] "))
			fila.append(num)
		matriz.append(fila)

	for fil_k in range(len(matriz)): #buscamos en la matriz el numero mayor
		for col_l in range(len(matriz[fil_k])):
			

			if matriz[fil_k][col_l] > mayor: #condicionamos para obtener el mayor
				mayor = matriz[fil_k][col_l]
				pos_mayor = fil_k, col_l

			if matriz[fil_k][col_l] == mayor: #comparamos para saber cuantas veces se repite el mayor
				cont += 1
	print(f"El numero mayor que es {mayor} se repite ({cont} veces) ") #imprimimos resultado
	
except ValueError:
	print("El dato ingresado debe ser númerico") 