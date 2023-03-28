try:
	fila = int(input("Digite la cantidad de filas de la matriz "))
	columna = int(input("Digite la cantidad de columnas de la matriz "))

	if (fila > 0 and fila <= 4 )and (columna > 0 and fila <= 5):

		matriz = []

		for fil_i in range(fila):
			lista = []
			for col_j in range(columna):

				num = int(input("Ingrese un numero entero: "))

				lista.append(num)
			matriz.append(lista)

		print(matriz)

	else:
		print("el rango de las filas o las columnas no es correcto")

except ValueError:
	print("El dato ingresado debe ser numerico")