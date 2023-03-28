"""Mostrar en pantalla todos los pares comprendidos entre 20 y 200."""


try:
	
	for i in range(20,200+1): #recorremos el ciclo dando los parametros que nos piden 

		print (i) #imprimimos resultado

except ValueError:
	print("El dato ingresado debe ser numerico")