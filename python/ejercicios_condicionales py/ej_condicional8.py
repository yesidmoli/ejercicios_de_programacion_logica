"""Leer un número entero de dos dígitos y determinar si sus dos dígitos son primos."""

try:
	number = int(input("Ingrese un numero entero de dos digitos"))

	if number >= 10 and number <= 99:

		d1 = number // 10
		d2 = number % 10

		if d1 % 2 != 0 and d2 % 2 != 0:
			print("es primo")
		else:
			print("al menos uno de los dos digitos no es primo")

	else:
		print("numero no valido")
except ValueError:
	print("el valor ingresado debe ser numerico")