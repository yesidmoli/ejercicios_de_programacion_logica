"""21. Leer dos matrices 4x5 enteras y determinar cuántos datos tienen en común."""
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

	cont = 0 #iniciamos un contador en 0 para saber si hay datos comunes

	for i in range(len(matriz1)):  # recorremos las matrices
		for j in range(len(matriz1[i])): 

			if matriz1[i][j] == matriz2[i][j]: #comparamos cada dato de las dos matrices
				cont +=1 #contador para contar cuantos datos tienen en comun	

	if cont != 0: #si contador es diferente a 0, hay datos comunes
		print(f" Las dos matrices tienen ({cont}) datos en comun ")
	else:
		print("La dos matrices no tiene datos comunes") #de lo contrario

except ValueError:
	print("El dato ingresado debe ser númerico") 