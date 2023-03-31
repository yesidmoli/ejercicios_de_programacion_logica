"""6. Leer una matriz 4x4 entera y calcular el promedio de los números mayores de cada fila."""
try:
	print("Matriz 4*4")

	# Leemos la matriz 4x3 
	matriz = []
	
	for i in range(4):
	    fila = []
	    for j in range(4):
	        num = int(input(f"Ingrese un numero entero para la posicion: [{i} ,{j}] ")) #solicitamos los numeros para cada posicion
	        fila.append(num)
	    matriz.append(fila)

	print(matriz)

	cont = 0
	sumatoria = 0
	for fil_i in range(len(matriz)): #recorremos la matriz (filas y columnas) para obtener el numero mayor de cada fila
		mayor_fila = 0
		
		for col_j in range(len(matriz[fil_i])): 
			fila = matriz[fil_i][col_j]

			if fila > mayor_fila: #comparamos para obtener el mayor
				mayor_fila = fila
				
		print(f"El mayor de la fila {fil_i} es: {mayor_fila}") #imprimimos la fila y el mayor de la fila

		sumatoria += mayor_fila #realizamos la sumatoria
		cont += 1 #contamos cuantas veces se suma
		promedio = sumatoria // cont #promediamos
  
	print(f"El promedio de los numeros mayores de cada fila es: {promedio}") #imprimimos el promedio
	#print(cont)
	#print(sumatoria)
	

except ValueError:
	print("El dato ingresado debe ser númerico") 