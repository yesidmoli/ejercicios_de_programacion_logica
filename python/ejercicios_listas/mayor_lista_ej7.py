"""7. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se
encuentra el número mayor."""

try:
	lista = [] #creamos la lista vacia
	mayor = 0
	pos = 0

	for i in range(10): #creamos un ciclo para obtener los numeros

		lista.append(int(input("Ingrese el numero entero "))) #agregamos a la lista los numeros ingresados

	"""for j in range(len(lista)): #recorremos la lista para obtener posicion y el mayor

		if lista[j] > mayor: #condicionamos para obtener el mayor
			mayor = lista[j]
			pos = j"""


	mayor = max(lista) #metodos para obtener en una lista el mayor y posicion
	pos = lista.index(mayor)
		

	print(lista)
	print(f"El numero mayor de la lista es: {mayor} y esta en la posicion {pos}") #imprimimos el resultado



except ValueError:
	print("El dato ingresado debe ser numerico")