"""11. Leer una matriz 5x3 entera y determinar en qué columna está el menor número par."""
try:
	print("Matriz 5*3")

	# Leer la matriz 5*3
	matriz = []
	for i in range(5):
		fila = []
		for j in range(3):
			num = int(input(f"Ingrese un numero entero para la posicion: [{i} ,{j}] "))
			fila.append(num)
		matriz.append(fila)


	# Encontrar el menor número par en la matriz
	menor_par = float('inf') # Inicializar con infinito positivo ya que aún no se ha encontrado ningún número par
	col_par = 0
	for fil_k in range(len(matriz)):
		for col_l in range(len(matriz[fil_k])):

			if matriz[fil_k][col_l] % 2 == 0 and matriz[fil_k][col_l] < menor_par:
				menor_par = matriz[fil_k][col_l]
				col_par = col_l
		
	# Imprimir la matriz y la columna donde se encuentra el menor número par
	print(matriz)
	if menor_par == float('inf'):
		print("No se encontró ningún número par en la matriz")
	else:
		print(f"El menor número par ({menor_par}) se encuentra en la columna {col_par}")

except ValueError:
	print("El dato ingresado debe ser númerico")  