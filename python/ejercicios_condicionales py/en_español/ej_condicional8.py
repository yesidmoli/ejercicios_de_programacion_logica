"""Leer un número entero de dos dígitos y determinar si sus dos dígitos son primos."""

try: #capturamos el numero entero
	number = int(input("Ingrese un numero entero de dos digitos"))

	if number >= 10 and number <= 99: #verificamos si es de dos digitos

		#Obtenemos los digitos
		d1 = number // 10
		d2 = number % 10

		if d1 % 2 != 0 and d2 % 2 != 0: #verificamos los digitos, para saber si son numeros primos
			print("es primo")
		else:
			print("al menos uno de los dos digitos no es primo")

	else:
		print("numero no valido") #Si las condiciones anteriores no se cumplen

except ValueError:
	print("el valor ingresado debe ser numerico")