"""Leer un numero entero y mostar todos los pares comprendidos entre 1 y el numero leido"""

try: 
	num = int(input("Ingrese un numero entero  ")) #capturamos el numero 

	for i in range(2,num+1,2): #recorremos el numero ingresado

		print( i) #imprimimos
	

except ValueError:
	print("El dato ingresado debe ser numerico")