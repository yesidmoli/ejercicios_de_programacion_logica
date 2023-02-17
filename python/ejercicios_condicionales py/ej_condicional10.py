"""Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales."""

try:
	number = int(input("Ingrese un numero entero de dos digitos"))

	if number >= 10 and number <= 99:

		d1 = number // 10
		d2 = number % 10

		if d1 == d2:
			print("Los dos digitos son iguales")
		else:
			print("Los dos digitos no son iguales")

	else:
		print("numero no valido")
except ValueError:
	print("el dato ingresado debe ser numerico")