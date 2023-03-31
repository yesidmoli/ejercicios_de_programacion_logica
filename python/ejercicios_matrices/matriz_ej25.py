"""25. Leer dos matrices 4x5 enteras y determinar si el mayor número primo de una de las
matrices es también el mayor número primo de la otra matriz."""

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
 
	mayor_primo1 = 0

	for i in range(4): #recorremos la matriz 1 para obtener el primo 
		for j in range(5): 

			num1 = matriz1[i][j] #asignamos a una variable num2, la matriz1
			primo = True #iniciamos una variable en verdadero

			if num1 < 2: # los números menores que 2 no son primos
				primo = False
				
			else:
				#obetenemos los primos de la primera matriz
				for primos in range(2, (num1 // 2)+1): #creamos el ciclo para saber si primos es divisible por algun numero 
					if num1 % primos == 0: #si al modularlo es igual a 0 no es primo
						primo = False #cambiamos a falso
						break

			if primo and num1 > mayor_primo1: #comparamos para obtener el mayor primo
					mayor_primo1 = num1

	mayor_primo2 = 0
	for i in range(4): #recorremos la matriz 2 para obtener el primo 
		for j in range(5): 

			num2 = matriz2[i][j] #asignamos a una variable num2, la matriz2
			primo = True #iniciamos una variable en verdadero

			if num2 < 2: # los números menores que 2 no son primos
				primo = False
				
			else:
				#obetenemos los primos de la segunda matriz
				for primos in range(2, (num2 // 2)+1): #creamos el ciclo para saber si primos es divisible por algun numero 
					if num2 % primos == 0: #si al modularlo es igual a 0 no es primo
						primo = False #cambiamos a falso
						break

			if primo and num2 > mayor_primo2: #comparamos para obtener el mayor primo
					mayor_primo2 = num2

			
	print(" ************************************************* ")
	print(f"Mayor primo primera matriz {mayor_primo1}") #si queremos imprimimos los primos mayores de cada matriz
	print(f"Mayor primo segunda matriz {mayor_primo2}")

	if mayor_primo1 == mayor_primo2: #si el mayor primo de la primera matriz es igual al mayor de la segunda
		print(f" Los mayores primos de las matrices son iguales")
	else:
		print(f" Los mayores primos de las matrices no son iguales ") #de lo contrario

except ValueError:
	print("El dato ingresado debe ser númerico") 