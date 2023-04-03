"""8. Leer una matriz 4x4 entera y determinar cuántos enteros terminados en 0 hay
almacenados en ella."""

try:
	print("Matriz 4*4")

	matriz = []

	for fil_i in range(4): #leemos y llenamos la matriz segun los parametros
		fila = []
		for col_j in range(4):
			num = int(input(f"Ingrese un numero entero para la posicion: [{fil_i} ,{col_j}] ")) #solicitamos los numeros
			fila.append(num)
		matriz.append(fila)

	print(matriz)

	terminado_0 = 0
	cont = 0

	for fil_k in range(len(matriz)): #buscamos en la matriz los numeros terminados en 0
		for col_l in range(len(matriz[fil_k])):

			if matriz[fil_k][col_l] % 10 == 0: #modulamos para obtener los numeros que su ultimo digito sea 0
				cont +=1 #si hay numeros terminados en 0 contamos

	if cont > 0: #condicionamos para saber cuantos numeros  terminados en 0 hay
		print(f"En la matriz hay {cont} numeros que terminan en 0") 
	else:
		print("No hay numeros que terminen en 0") #de lo contrario
			
except ValueError:
	print("El dato ingresado debe ser númerico") 