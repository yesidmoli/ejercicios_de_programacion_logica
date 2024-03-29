""" Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito."""

try: #capturamos el numero entero
	num1 = int(input("Ingrese un numero entero de tres dígitos: "))

	if num1 < 100 or num1 > 999: #verificamos si el numero tiene 3 digitos
		print(" el número debe tener tres dígitos")

	else: #al no cumplirse la condicion anterior, obtenemos la posicion de los digitos

		po1 = num1 // 100
		po2 = (num1 // 10) % 10 
		po3 = num1 % 10

		if po1 > (po2 and po3): #verificamos en que posicion esta el digito mayor
			print("el digito mayor esta en la posicion 1")

		elif po2 > (po1 and po3):
			print("El digito mayor, esta en la posicion 2")

		elif po3 > (po1 and po2):
			print("El digito mayor, esta en la posicion 3")

		else:
			print("Todos los digitos son iguales")

except ValueError:
	print("El dato ingresado debe ser numerico")