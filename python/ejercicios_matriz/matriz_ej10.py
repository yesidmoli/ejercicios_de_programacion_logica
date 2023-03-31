"""10. Leer una matriz 5x3 entera y determinar en qué fila está el mayor número primo."""
try:
	print("Matriz 5*3")

	matriz = []
	
	
	for fil_i in range(5): #leemos la matriz segun los parametros
		fila = []
		for col_j in range(5):
			num = int(input(f"Ingrese un numero entero para la posicion: [{fil_i} ,{col_j}] "))
			fila.append(num)
		matriz.append(fila)

	print(matriz) #imprimimos la matriz
	mayor_primo = 0
	fila = 0
	for fil_i in range(len(matriz)):  #recorremos la matriz
		for col_j in range(len(matriz[fil_i])):

			num = matriz[fil_i][col_j]
			primo = True #iniciamos una variable en verdadero

			if num < 2: # los números menores que 2 no son primos
				primo = False
				
			else:
				#obetenemos los primos
				for primos in range(2, (num // 2)+1): #creamos el ciclo para saber si primos es divisible por algun numero 
					if num % primos == 0: #si al modularlo es igual a 0 no es primo
						primo = False #cambiamos a falso
						break
			if primo:
				if num > mayor_primo: #comparamos para saber en que lugar esta el numero mayor primo
					mayor_primo = num
					fila = fil_i
	if fila != 0: #si la variable fila es diferente a lo asignado, hay numero primo
		print(f"El numero mayor primo {mayor_primo} esta en la fila {fila}")
	else:
		print("No se encontraron numeros primos en la matriz") #de lo contrario
			
except ValueError:
	print("El dato ingresado debe ser númerico") 