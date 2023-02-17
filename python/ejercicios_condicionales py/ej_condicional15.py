""" . Leer un número entero de tres dígitos y determinar a cuánto es igual la suma de sus
dígitos."""

try:
	
	num1 = int(input("Ingrese un numero entero de tres dígitos: "))

	if num1 < 100 or num1 > 999:
		print("Los números deben tener tres dígitos")
	else:
		suma = (num1 // 100) + ((num1 // 10) % 10) + (num1 % 10)

		print(f"La suma de todos los dígitos es {suma}")

except ValueError:
	print("El dato ingresado debe ser numerico")