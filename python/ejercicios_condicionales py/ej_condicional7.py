
"""Leer un número entero de dos dígitos y determinar si es primo y además si es negativo."""

try:
	number = int(input("Ingrese un numero de dos digitos"))

	if number < 0:
		print("El numero es negativo")
	else:

		if number >= 10 and number <= 99:

			if  number % 2 == 0:
				print("No es primo")
			else:
				print("Es primo")

		else:
			print("el numero no es valido")

except ValueError:
	print("ValueError")