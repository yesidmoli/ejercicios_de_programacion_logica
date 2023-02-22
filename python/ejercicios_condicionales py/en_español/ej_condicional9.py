"""Leer un número entero de dos dígitos y determinar si un dígito es múltiplo del otro."""

try: #capturamos el numero entero
	number = int(input("Ingrese un numero de dos digitos"))

	if number >= 10 and number <= 99: #verificamos si es un numero de dos digitos

		#obtenemos los digitos
		d1 = number // 10
		d2 = number % 10

		if d1 % d2 == 0: #validamos si es d1 es multiplo del d2
			print("el primer digito es multiplo del segundo ")

		elif d2 % d1 == 0:#validamos si es d2 es multiplo del d1
			print("el segundo digito es multiplo del primero")

		else:
			print(" ningun digito es multiplo del otro") #de lo contrario imprimimos

	else:
		print("numero no valido")

except ValueError:
	print("el numero ingresado debe ser numerico")