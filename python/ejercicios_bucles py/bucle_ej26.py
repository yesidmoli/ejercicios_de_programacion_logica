"""Leer un número entero y determinar cuál es el mayor de sus dígitos."""
try:
	num = int(input("Ingrese el numero entero"))
	mayor = 0


	for i in range(1, num):
		digito = num % 10
		num //= 10

		if digito > mayor:
			mayor = digito
	
	print("el mayor digito es", mayor)
			

except ValueError:
	print("El dato ingresado debe ser numerico")