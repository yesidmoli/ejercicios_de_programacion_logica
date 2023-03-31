"""20. Leer dos matrices 4x5 entera, luego leer un entero y determinar si cada uno de los
elementos de una de las matrices es igual a cada uno de los elementos de la otra matriz
multiplicado por el entero leído. """

try:
	print(" Ingrese los elementos para la primera matriz")
	print(" ************************************************* ")
	matriz1 = [] # Definimos las matrices
	matriz2 = []

	for i in range(4):  # Recorremos cada fila de la matriz
		fila = []
		for j in range(5): # Recorrer cada columna de la fila
			num = int(input(f"Ingrese un numero entero para la posicion: [{i} ,{j}] ")) # Pedimos al usuario que ingrese un número
			fila.append(num) # Agregamos el número a la fila
		matriz1.append(fila) # Agregamos la fila a la matriz

	print(" ************************************************* ")
	print(" Ingrese los elementos para la segunda matriz")
	for i in range(4):  
		fila = []
		for j in range(5): 
			num = int(input(f"Ingrese un numero entero para la posicion: [{i} ,{j}] ")) 
			fila.append(num)
		matriz2.append(fila) 

	print(" ************************************************* ")
	#solicitamos el numero entero
	numero = int(input(" Ingrese un numero entero: "))

	cont = 0			#inicializamos un contador y  dos variables para guardar la multiplicacion
	multi_matriz_1 = 0
	multi_matriz_2 = 0
	multiplicacion1 = [] #creamos dos listas para almacenar la multiplicacion de cada matriz
	multiplicacion2 = []

	for i in range(len(matriz1)):  #comparamos las matrices, multiplicando el numero entero leido
		for j in range(len(matriz1[i])): 

			multi_matriz_1 = matriz1[i][j] * numero
			multiplicacion1.append(multi_matriz_1)

			multi_matriz_2 = matriz2[i][j] * numero
			multiplicacion2.append(multi_matriz_2)

			if multi_matriz_1 != multi_matriz_2: #si la multiplicacion de cada una de las matrices es diferente, no son iguales
				cont +=1 #contador para saber si son diferentes
				
	print(" ************************************************* ")
	print("Multiplicacion de cada matriz")
	print(f" M1 {multiplicacion1}")
	print(f" M2 {multiplicacion2}")

	print(" ************************************************* ")
	if cont == 0: #si contador sigue en 0 es decir que son iguales las matrices
		print(f" Los elementos de las matrices multiplicados por ({numero}) son exactamente iguales.")
	else:
		print(" Los elmentos de las matrices no son exactamente iguales.") #de lo contrario

except ValueError:
	print("El dato ingresado debe ser númerico")