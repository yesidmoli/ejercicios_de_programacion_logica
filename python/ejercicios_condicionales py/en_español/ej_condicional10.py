"""Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales."""

try: #capturamos el numero entero
	number = int(input("Ingrese un numero entero de dos digitos"))

	if number >= 10 and number <= 99:  #verificamos si es de dos digitos

		#obtenemos lo digitos del numero

		d1 = number // 10
		d2 = number % 10

		if d1 == d2: #verificamos si son iguales los digitos
			print("Los dos digitos son iguales")
		else:
			print("Los dos digitos no son iguales") #de lo contrario

	else:
		print("numero no valido")

except ValueError:
	print("el dato ingresado debe ser numerico")