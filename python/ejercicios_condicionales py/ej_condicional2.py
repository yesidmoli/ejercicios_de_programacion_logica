"""Leer un número entero y determinar si tiene 3 dígitos."""

try:
	number = int(input("Ingrese un numero entero")) #capturamos el numero entero

	if number > 99 and number < 999: # verificamos si el numero tiene 3 digitos, si si, imprimimos
		print("Es un numero de 3 digitos")
	else:
		print("No es un numero de 3 digitos") #de lo contrario imprimos no es un numero de 3 digitos

except ValueError:
	print("+++error+++")