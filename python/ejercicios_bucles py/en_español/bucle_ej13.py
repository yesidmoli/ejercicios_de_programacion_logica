"""Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número
leído."""

try:
	#capturamos el numero
	num = int(input("Ingrese el numero entero "))
	
	for i in range(1,num+1): #recorremos el ciclo dando los parametros 

		if i % 5 == 0: #condicionamos para obtener los multiplos de 5
			
			print(i) #imprimimos resultado

except ValueError:
	print("El dato ingresado debe ser numerico")