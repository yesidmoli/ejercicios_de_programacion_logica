"""19. Leer dos matrices 4x5 entera y determinar si sus contenidos son exactamente iguales."""
try:
	

	print(" Ingrese los elementos para la primera matriz")
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

	#comparamos las matrices
	cont = 0
	for i in range(len(matriz1)):  
		for j in range(len(matriz1[i])): 
			if matriz1[i][j] != matriz2[i][j]:
				cont +=1
				

	if cont == 0: #si contador sigue en 0 es decir que son iguales las matrices
		print(" Las matrices son exactamente iguales.")
	else:
		print(" Las matrices no son exactamente iguales.") #de lo contrario

except ValueError:
	print("El dato ingresado debe ser númerico")  