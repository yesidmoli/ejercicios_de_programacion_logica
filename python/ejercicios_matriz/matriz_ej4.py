"""4. Leer una matriz 4x3 entera y determinar en qué posiciones exactas se encuentran los
números primos.""" 
try:
	print("Matriz 4*3")

	matriz = []
	
	
	for fil_i in range(4): #leemos la matriz segun los parametros
		fila = []
		for col_j in range(3):
			num = int(input(f"Ingrese un numero entero para la posicion: [{fil_i} ,{col_j}] "))
			fila.append(num)
		matriz.append(fila)

	print(matriz) #imprimimos la matriz
	for fil_i in range(len(matriz)):  #recorremos la matriz
		for col_j in range(len(matriz[fil_i])):

			num = matriz[fil_i][col_j]
			primo = True #iniciamos una variable en verdadero

			if num < 2: # los números menores que 2 no son primos
				primo = False
				
			else:

				for primos in range(2, (num // 2)+1): #creamos el ciclo para saber si primos es divisible por algun numero 
					if matriz[fil_i][col_j] % primos == 0:
						primo = False
						break
					

			if primo:
				print(f"El número {num} es primo y se encuentra en la posición ({fil_i , col_j})") #imprimimos el resultado
	if primo == 0:
		print("No hay primos") #al no haber encontrado algun primo

		
except ValueError:
	print("El dato ingresado debe ser númerico") 