"""Leer 10 números enteros, almacenarlos en una lista y determinar cuántas veces está
repetido el mayor. """

try:
	numeros = [] #creamos lista vacia
	mayor = 0
	pos = 0
	cont = 0

	for i in range(10): #creamos un ciclo para obtener los numeros, segun el rango establecido

		numeros.append(int(input("Ingrese el numero entero ")))

	for j in range(len(numeros)):

		if numeros[j] > mayor:

			mayor = numeros[j]
			pos = j

	for k in range(len(numeros)):

		if numeros[k] == mayor:

			cont += 1

	print(cont)


except ValueError:
	print("El dato ingresado debe ser numerico")