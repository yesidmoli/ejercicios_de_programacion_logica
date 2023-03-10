"""Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205"""

try:
	
	for i in range(25,205+1): #recorremos el ciclo dando los parametros que nos piden 

		if i % 10 == 6: #comdicionamos modulando para determinar cuales numeros terminan en 6

			print(i) #imprimimos resultado

except ValueError:
	print("El dato ingresado debe ser numerico")