

#para llenar una matriz
try:
	matriz = []

	for fila in range(4):
		lista = []
		for columna in range(7):
			numero = int(input("Ingrese los numeros"))

			lista.append(numero)

		matriz.append(lista)

		#leer una matriz

	for fila in range(len(matriz[columna])):
		for columna in range(len(matriz)):
			matriz[fila][columna]

	print(matriz)

except ValueError:
	print("error")