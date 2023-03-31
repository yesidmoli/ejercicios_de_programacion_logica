"""22. Leer dos matrices 4x5 enteras y determinar si el número mayor almacenado en la
primera está en la segunda.""" 
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

	mayor_matriz_1 = matriz1[0][0]

	for i in range(len(matriz1)):  # recorremos la primera matriz para obtener el mayor numero
		for j in range(len(matriz1[i])): 

			if matriz1[i][j] > mayor_matriz_1:
				mayor_matriz_1 = matriz1[i][j]

	cont = 0 #iniciamos un contador en 0 

	for i in range(len(matriz2)):  # recorremos la matriz 2
		for j in range(len(matriz2[i])): 

			if matriz2[i][j] == mayor_matriz_1 : #comparamos para saber si esta el mayor 
				cont +=1 #contador
	print(" ************************************************* ")
	print(f" M1 {matriz1}")
	print(f" M2 {matriz2}")
	print(" ************************************************* ")
	print(f" El numero mayor de la primera matriz  es: {mayor_matriz_1}")

	if cont != 0: #si contador es diferente a 0, el numero mayor M1 estan en la M2
		print(f" El numero mayor de la primera matriz ({mayor_matriz_1}), se encuentra tambien en la segunda matriz  ")
	else:
		print(f" El numero mayor de la primera matriz  ({mayor_matriz_1}) no se encuentra en la segunda matriz ") #de lo contrario

except ValueError:
	print("El dato ingresado debe ser númerico")