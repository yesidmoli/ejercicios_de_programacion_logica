"""Leer un número entero y determinar si es un número terminado en 4."""



try:
	number = int(input("Ingresa un numero entero"))

	if number % 10 == 4:
		print("El numero es terminado en 4")

	else:
		print("El numero no es terminado en 4")

except ValueError:
	print("el dato ingresa debe ser numerico")