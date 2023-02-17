""". Leer dos números enteros de dos dígitos y determinar si tienen dígitos comunes."""

try:
	number1 = int(input("Ingrese el primer numero entero de dos digitos")) 
	number2 = int(input("Ingrese el primer numero entero de dos digitos"))

	if number1 and number2 >= 10 and number2 and number1 <= 99:

		if (number1 // 10 == number2 // 10) or (number1 // 10 == number2 % 10) or (number1 % 10 == number2 // 10) or (number1 % 10 == number2 % 10):

			print("Los numeros tienen digitos comunes")
		else:
			print("Los numeros no tienen digitos comunes")

	else:
		print("Al menos uno de los dos numeros esta fuera del rango ")

except ValueError:
	print("El dato ingresado debe ser numerico")