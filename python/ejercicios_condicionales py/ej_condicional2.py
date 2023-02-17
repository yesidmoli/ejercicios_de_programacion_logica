"""Leer un número entero y determinar si tiene 3 dígitos."""

try:
	number = int(input("Ingrese un numero entero"))

	if number > 99 and number < 999:
		print("Es un numero de 3 digitos")
	else:
		print("No es un numero de 3 digitos")

except ValueError:
	print("+++error+++")