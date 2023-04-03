"""14. Leer una matriz 5x5 entera y determinar cuántos números almacenados en ella tienen
más de 3 dígitos."""
try:
	print("Matriz 5*5")

	# Leer la matriz 5*3
	matriz = []
	for i in range(5):
		fila = []
		for j in range(5):
			num = int(input(f"Ingrese un numero entero para la posicion: [{i} ,{j}] "))
			fila.append(num)
		matriz.append(fila)


	# buscamos cuantos numeros de la matriz tienen mas de 3 digitos
	cont = 0
	for fil_k in range(len(matriz)):
		for col_l in range(len(matriz[fil_k])):

			if matriz[fil_k][col_l] > 999:
				cont += 1
	
	# Imprimimos la matriz y la cantidad de numeros almacenados que tengan mas de 3 digitos
	print(matriz)

	if cont != 0:
		print(f"En la matriz hay ({cont}) numeros que tienen mas de 3 digitos ")
	else:
		print("La matriz no tiene almacenado numeros con mas de 3 digitos")

except ValueError:
	print("El dato ingresado debe ser númerico")   