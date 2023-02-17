"""Leer un número entero y determinar si es negativo.
try:
	
except ValueError:
	print("ValueError")"""

try:
	number= int(input("Ingresa un numero entero"))

	if number < 0:
		print("Es un numero negativo")
	else:
		print("Es un numero positivo")

except ValueError:
	print("el dato ingresado debe ser numerico")