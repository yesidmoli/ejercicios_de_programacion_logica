"""24. Leer dos matrices 4x5 enteras y determinar si el mayor número primo de una de las
matrices también se encuentra en la otra matriz.""" 

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

	cont = 0 #contador 
	mayor_primo = 0

	for i in range(4):  
		for j in range(5): 

			num = matriz1[i][j] #asignamos a una variable num, la matriz1
			primo = True #iniciamos una variable en verdadero

			if num < 2: # los números menores que 2 no son primos
				primo = False
				
			else:
				#obetenemos los primos de la primera matriz
				for primos in range(2, (num // 2)+1): #creamos el ciclo para saber si primos es divisible por algun numero 
					if num % primos == 0: #si al modularlo es igual a 0 no es primo
						primo = False #cambiamos a falso
						break

			if primo and num > mayor_primo: #comparamos para obtener el mayor primo
					mayor_primo = num

	for i in range(4):  
		for j in range(5):
			if matriz2[i][j] == mayor_primo  :
					cont += 1	

	print(" ************************************************* ")
	print(f"Mayor primo {mayor_primo}")
	if cont != 0: 
		print(f" El mayor numero primo {mayor_primo} de la primera matriz se encuentra en la segunda matriz  ")
	else:
		print(f" El mayor numero primo no se encuentra en la segunda matriz ") 

except ValueError:
	print("El dato ingresado debe ser númerico") 