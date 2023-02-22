""" Leer un número entero de tres dígitos y determinar si al menos dos de sus tres dígitos
son Iguales."""

try:
	#obtenemos el numero entero
	num1 = int(input("Ingrese un numero entero de tres dígitos: "))

	if num1 < 100 or num1 > 999: #verificamos si es un numero de 3 digitos
		print("el número debe tener tres dígitos")

	else: #si lo anterior no se cumple, obtenemos los digitos del numero

		d1 = num1 // 100
		d2 = (num1 // 10) % 10 
		d3 = num1 % 10

		if d1 == d2 or d1 == d3 or d2 == d1 or d3 == d1 or d2 == 3:  #verificamos que dijitos son iguales
			print("Al menos dos de sus tres dígitos son iguales")

		else:
			print("Ninguno de los 3 digitos son iguales")


except ValueError:
	print("El dato ingresado debe ser numerico")