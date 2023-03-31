"""9. Leer una matriz 3x4 entera y determinar cuántos de los números almacenados son primos
y terminan en 3."""
try:
	print("Matriz 3*4")

	matriz = []
	
	
	for fil_i in range(3): #leemos la matriz segun los parametros
		fila = []
		for col_j in range(4):
			num = int(input(f"Ingrese un numero entero para la posicion: [{fil_i} ,{col_j}] "))
			fila.append(num)
		matriz.append(fila)

	print(matriz) #imprimimos la matriz
	cont = 0
	primos_terminados_3 = []

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
					

			if primo: #si hay primos, modulamos para saber si terminan en 3
				if num % 10 == 3: 
					cont += 1
					primos_terminados_3.append(num) #si si agregamos a una lista (opcional)

	if cont > 0: #si el contador es mayor a 0 es decir que si hay numeros primos que terminan en 3
		print(f"En la matriz hay {cont} numero(s) primo (s) que terminan en 3 ")
		print(f"(El) o (Los) numero(s) primo(s) terminado  en 3 son: {primos_terminados_3}")

	else:
		print("Puede que hayan numeros primos pero no terminan en 3 ") #de lo contrario

		
except ValueError:
	print("El dato ingresado debe ser númerico")  