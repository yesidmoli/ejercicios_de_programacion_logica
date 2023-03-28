"""Mostrar en pantalla el promedio entero de los n primeros múltiplos de 3 para un número
n leído."""
try:
	n = int(input("Ingrese el valor de n:  "))
	promedio = 0
	
	for i in range(1, n+1): #recorremos el ciclo dando los parametros 

		promedio += i * 3 
		
	promedio //= n

	print(f"El promedio  de los primero {n} multiplos de 3 es: {promedio} ")

			

except ValueError:
	print("El dato ingresado debe ser numerico")