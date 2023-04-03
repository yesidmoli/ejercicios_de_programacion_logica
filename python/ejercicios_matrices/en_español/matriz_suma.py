"""Leer una matriz 4 *3 entera, calcular la suma de todos los elementos de la matriz"""
try:
	fila = int(input("Digite la cantidad de filas de la matriz "))
	columna = int(input("Digite la cantidad de columnas de la matriz "))

	if (fila > 0 and fila <= 4 )and (columna > 0 and fila <= 3):

		matriz = []
		suma = 0

		for fil_i in range(fila):
			lista = []
			for col_j in range(columna):

				num = int(input(f"Ingrese un numero entero para la posicion: [{fil_i} ,{col_j}] "))

				lista.append(num)
			matriz.append(lista)

		print(matriz)

		for fil_k in range(len(matriz)):
			for col_l in range(len(matriz[fil_k])):
				sumatoria = matriz[fil_k][col_l]
			
				suma += sumatoria

		print(f"La suma de los elementos de la matriz es: {suma}")

	else:
		print("el rango de las filas o las columnas no es correcto")

except ValueError:
	print("El dato ingresado debe ser numerico")