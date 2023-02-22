
"""Leer un número entero de dos dígitos y determinar si es primo y además si es negativo."""

try: #capturamos el numero entero
	number = int(input("Ingrese un numero de dos digitos"))

	if number < 0: # verificamos si el numero es negativo
		print("El numero es negativo")

	else: #si no es negativo, verificamos por medio de la condicion si es un numero de dos digitos 

		if number >= 10 and number <= 99:

			if  number % 2 != 0: #modulamos para saber si es un numero primo o no
				print("Es primo")
			else:
				print(" No es primo")

		else:
			print("el numero no es valido") #si no se cumplen las condiciones anteriores

except ValueError:
	print("ValueError")