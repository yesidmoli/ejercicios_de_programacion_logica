"""Leer una matriz de 4 * 4 entera. Indicar cual es el numero mayor de la matriz 
y cual es el numero menor de la matriz"""

try:
	fila = int(input("Digite la cantidad de filas de la matriz "))
	columna = int(input("Digite la cantidad de columnas de la matriz "))

	if  (fila > 0 and fila <= 4 )and (columna > 0 and fila <= 4):

		matriz = []
		mayor = 0
		pos_mayor = 0
		pos_menor = 0
		

		for fil_i in range(fila):
			lista = []
			for col_j in range(columna):

				num = int(input(f"Ingrese un numero entero para la posicion: [{fil_i} ,{col_j}] "))
				lista.append(num)
			matriz.append(lista)

		

		for fil_k in range(len(matriz)):
			for col_l in range(len(matriz[fil_k])):

				if matriz[fil_k][col_l] > mayor:
					mayor = matriz[fil_k][col_l]

					pos_mayor = fil_k, col_l

		
		menor = matriz[0][0]

		for fil_k in range(len(matriz)):
			for col_l in range(len(matriz[fil_k])):
				if matriz[fil_k][col_l] < menor:
					menor = matriz[fil_k][col_l]

					pos_menor = fil_k, col_l


		print(f"la matriz original es {matriz}")
		print(f"El numero mayor de la matriz es: {mayor}")
		print(f"posicion del numero mayor: {pos_mayor}")
		print(f"El numero menor de la matriz es: {menor}")
		print(f"posicion del numero menor: {pos_menor}")


	else:
		print("el rango de las filas o las columnas no es correcto")

except ValueError:
	print("El dato ingresado debe ser numerico")