"""Leer dos números enteros y determinar cuál es el mayor."""

try:
	#capturamos los dos numeros
	number1, number2 = int(input("Ingrese el primer numero")), int(input("Ingrese el segundo numero"))

	if number1 > number2: #verficamos cual es el mayor

		print(f" el {number1} es mayor que {number2} ")
	else:
		print(f" el {number2} es mayor que {number1} ")

except ValueError:
	
	print("Error el dato ingresado debe ser numerico")