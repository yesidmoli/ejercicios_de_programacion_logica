"""Leer 10 números enteros, almacenarlos en una lista y determinar cuántas veces está
repetido el mayor. """

try:
	lista = [] #creamos lista vacia
	mayor = 0
	pos = 0
	cont = 0

	for i in range(10): #creamos un ciclo para obtener los numeros, segun el rango establecido

		lista.append(int(input("Ingrese el numero entero ")))

	for j in range(len(lista)):

		if lista[j] > mayor:

			mayor = lista[j]
			pos = j

	for k in range(len(lista)):

		if lista[k] == mayor:

			cont += 1

	print(cont)


except ValueError:
	print("El dato ingresado debe ser numerico")