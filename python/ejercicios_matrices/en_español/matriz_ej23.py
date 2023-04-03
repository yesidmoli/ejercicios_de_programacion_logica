"""23. Leer dos matrices 4x5 enteras y determinar si el número mayor de una de las matrices
es igual al número mayor de la otra matriz."""
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

	mayor_matriz_1 = matriz1[0][0] #definimos dos variables inicializadas en pos 0,0 para almacenar el mayor de cada matriz
	mayor_matriz_2 = matriz2[0][0]
	cont = 0 #contador 

	for i in range(len(matriz1)):  # recorremos un ciclo aninado para obtener el mayor de cada matriz y comparar
		for j in range(len(matriz1[i])): 

			if matriz1[i][j] > mayor_matriz_1:
				mayor_matriz_1 = matriz1[i][j]

			if matriz2[i][j] > mayor_matriz_2:
				mayor_matriz_2 = matriz2[i][j]

			if mayor_matriz_1 == mayor_matriz_2:
				cont += 1

	print(" ************************************************* ")
	if cont != 0: 
		print(f" El numero mayor de la primera matriz ({mayor_matriz_1}), es igual al numero mayor de la segunda matriz ({mayor_matriz_2}) ")
	else:
		print(f" Los numeros mayores de cada matriz son diferentes ") 

except ValueError:
	print("El dato ingresado debe ser númerico") 