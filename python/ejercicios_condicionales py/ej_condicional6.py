"""Leer un número entero de dos dígitos menor que 20 y determinar si es primo."""


try:
	#capturamos el numero

	number = int(input("Ingrese un numero entero de dos digitos "))

	#comprobamos si el numero es de dos digitos y menor que 20

	if number >= 10 and number < 20:
		if number % 2 == 0: 
			print(f"{number} No es un numero primo")
		else:
			print(f"{number} es un numero primo")

	else:
		print("El numero no es valido")


except ValueError:
	print("el valor ingresado debe ser numerico")