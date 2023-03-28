"""Leer un matriz de M y N elementos enteros definidos por el usuario.
Imprimir la matriz e indicar la cantidad de elementos que se encuentran en la matriz"""
try:
	fila = int(input("Digite la cantidad de filas de la matriz "))
	columna = int(input("Digite la cantidad de columnas de la matriz "))

	if fila > 0 and columna > 0:

		matriz = []
		cont = 0

		for fil_i in range(fila):
			lista = []
			for col_j in range(columna):

				num = int(input(f"Ingrese un numero entero para la posicion: [{fil_i} ,{col_j}] "))

				lista.append(num)
				cont += 1
			matriz.append(lista)

		print(f"la matriz original es {matriz}")
		print(f"la cantidad de elemntos de la matriz es: {cont}")

	else:
		print("el rango de las filas o las columnas no es correcto")

except ValueError:
	print("El dato ingresado debe ser numerico")