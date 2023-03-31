"""1. Leer una matriz 4x4 entera y determinar en qué fila y en qué columna se encuentra el
número mayor."""

try:
	print("Matriz 4*4")
	fila = int(input("Ingrese la cantidad de filas de la matriz: ")) #obtenemos los parametros
	columna = int(input("Ingrese la cantidad de columnas de la matriz"))

	if (fila > 0 and fila <= 4) and (columna > 0 and columna <= 4):

		matriz = []
		mayor = 0
		pos_mayor = 0

		for fil_i in range(fila): #leemos la matriz segun los parametros
			fila = []
			for col_j in range(columna):
				num = int(input(f"Ingrese un numero entero para la posicion: [{fil_i} ,{col_j}] "))
				fila.append(num)
			matriz.append(fila)

		for fil_k in range(len(matriz)): #buscamos en la matriz el numero mayor
			for col_l in range(len(matriz[fil_k])):

				if matriz[fil_k][col_l] > mayor:
					mayor = matriz[fil_k][col_l]
					pos_mayor = fil_k, col_l

		print(f"El numero mayor de la matriz que es: {mayor} se encuentra en la posicion [{pos_mayor}]") #imprimimos el numero mayor y la posicion

	else:
		print("el rango de las filas o las columnas no es correcto")


except ValueError:
	print("El dato ingresado debe ser númerico")