"""Leer dos números enteros y determinar si la diferencia entre los dos es un número
divisor exacto de alguno de los dos números."""

try: #capturamos los numeros enteros
	num1, num2 = int(input("Ingrese el primer numero")), int(input("Ingrese el segundo numero"))

	diferencia = num1 - num2 # creamos una variable para guardar la diferencia

	if diferencia % num1 == 0 : #verificamos si la diferencia modulada por num1 el residuo da 0

		print("Es un divisor exacto ")

	elif diferencia % num2 == 0: #verificamos si la diferencia modulada por num2 el residuo da 0
		print("Es un divisor exacto")

	else:
		print(" ninguno de los dos da una division exacta") #si lo anterior no se cumple imprimimos

except ValueError:
	print("error")