"""Leer un número entero menor que 50 y positivo y determinar si es un número primo.."""

try: #capturamos el numero entero
	number = int(input("Ingrese un numero entero menor que 50 y positivo "))

	if number <= 0 or number >= 50: #verificamos si es un numero positivo y menor que 50
		print("El numero debe ser menor a 50 o positivo")

	else: #si lo anterior no se cumple, validamos si el numero es primo
		if number % 2 != 0:
			print(f" {number} Es un numero primo")
		else:
			print(f" {number} no es un numero primo")

except ValueError:
	print("el dato ingresado debe ser numerico")