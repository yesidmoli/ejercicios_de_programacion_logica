"""4. Cargar una lista de 10 posiciones con los 10 primeros elementos de la serie de Fibonacci
y mostrarlo en pantalla. """

try: #creamos las lista vacias 
	numeros = [] 
	val1 = 0 #creamos las variables segun orden fibonacci
	val2 = 1
	aux = 0



	for i in range(0,10): #creamos un ciclo para obtener los numeros y almacenarlos en una lista

		
		numeros.append(val1) #agregamos los numeros a la lista
		aux = val1 + val2
		val1 = val2
		val2 = aux

		
	print(f"La serie Fibonacci es: {numeros}") #imprimimos resultados


except ValueError:
	print("El dato ingresado debe ser numerico")