"""Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de la lista está
el mayor número leído. """

try:
	lista = [] #creamos una lista vacia

	#creamos dos varibles inicializadas en 0 para guardar la posicion y el numero mayor
	pos = 0  
	mayor = 0

	for i in range(10): #creamos un ciclo para ingresar los numeros que seran añadidos  en la lista

		num = int(input("Ingrese el numero entero"))

		lista.append(num)

	for j in range(len(lista)): #creamos otro ciclo para obtener la posicion del numero mayor 

		num = lista[j]

		if num > mayor:

			mayor = num
			pos = j

	print(lista)
	print(f"El numero mayor que es {mayor} se encuentra en la posicion {pos}") #imprimimos resultados


except ValueError:
	print("El dato debe ser numerico")