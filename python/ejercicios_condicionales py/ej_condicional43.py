"""Leer dos números enteros y determinar si la diferencia entre los dos es un número
divisor exacto de alguno de los dos números."""

try:
	num1, num2 = int(input("Ingrese el primer numero")), int(input("Ingrese el segundo numero"))

	diferencia = num1 - num2 

	if diferencia % num1 == 0 :

		print("Es un divisor exacto ")

	elif diferencia % num2 == 0:
		print("Es un divisor exacto")
	else:
		print(" ninguno de los dos da una division exacta")

except ValueError:
	print("error")