"""Mostrar en pantalla todos los enteros comprendidos entre 1 y 100."""
try:
	#recorremos por medio de un ciclo 
	for i in range(1,100+1):

		print (i) #imprimimos el resultado

except ValueError:
	print("El dato ingresado debe ser numerico")