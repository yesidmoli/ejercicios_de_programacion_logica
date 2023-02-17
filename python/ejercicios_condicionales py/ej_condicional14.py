""" Leer dos números enteros de dos dígitos y determinar a cuánto es igual la suma de todos
los dígitos"""

try:
	
	num1 = int(input("Ingrese el primer número entero de dos dígitos: "))
	num2 = int(input("Ingrese el segundo número entero de dos dígitos: "))

	if (num1 < 10 or num1 > 99) or (num2 < 10 or num2 > 99):
		print("Los números deben tener dos dígitos")
	else:
		suma = (num1 % 10 )+ (num1 // 10) + (num2 % 10) + (num2 // 10)

		print(f"La suma de todos los dígitos es {suma}")

except ValueError:
	print("El dato ingresado debe ser numerico")