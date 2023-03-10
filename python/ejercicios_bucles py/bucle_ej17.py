"""Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los
promedios de los y múltiplos de 5 para valores de x y y leídos."""

try:
	x = int(input("Ingrese el valor de x para los primero multiplos de 2 :  "))
	y = int(input("Ingrese el valor de y para los primero multiplos de 5 :  "))

	promedio_1 = 0
	promedio_2 = 0
	
	for i in range(1, x+1): #recorremos el ciclo dando los parametros 

		promedio_1 += i * 2
		
	promedio_1 //= x

	print(f"El promedio de los {x} multiplos de 2 es {promedio_1}")


	for i in range(1, y+1): #recorremos el ciclo dando los parametros 

		promedio_2 += i * 5
		
	promedio_2 //= y
	
	print(f"El promedio de los {y} multiplos de 5 es {promedio_2}")

	if promedio_1 > promedio_2:
		print(f"El promedio {promedio_1} es mayor al promedio {promedio_2}")

	elif promedio_2 > promedio_1:
		print(f"El promedio {promedio_2} es mayor al promedio {promedio_1}")

	else:
		print("Los promedios son iguales")
			

except ValueError:
	print("El dato ingresado debe ser numerico")