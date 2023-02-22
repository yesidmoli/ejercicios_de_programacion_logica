""" . Leer un número entero de tres dígitos y determinar a cuánto es igual la suma de sus
dígitos."""

try:
	#capturamos el numero entero
	num1 = int(input("Ingrese un numero entero de tres dígitos: "))

	if num1 < 100 or num1 > 999: #verificamos si el numero tiene 3 digitos
		print(" el  número debe tener tres dígitos")

	else: #si lo anterior no se cumple, obtenemos los digitos y los sumanos
		suma = (num1 // 100) + ((num1 // 10) % 10) + (num1 % 10)

		print(f"La suma de todos los dígitos es {suma}")

except ValueError:
	print("El dato ingresado debe ser numerico")