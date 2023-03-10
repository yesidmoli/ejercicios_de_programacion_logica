"""Leer un número entero y determinar a cuánto es igual la suma de todos los enteros
comprendidos entre 1 y el número leído."""

try:

	num = int(input("Ingrese un numero entero ")) #capturamos el numero 
	suma = 0 #definimos una variable para almacenar la suma, inicializada en 0
	
	for i in range(1,num+1): #recorremos el ciclo dando los parametros que nos piden 

		suma += i #realizamos la suma

		

	print(f"La sumatoria de los numeros enteros es:{suma}") #imprimimos resultado

except ValueError:
	print("El dato ingresado debe ser numerico")