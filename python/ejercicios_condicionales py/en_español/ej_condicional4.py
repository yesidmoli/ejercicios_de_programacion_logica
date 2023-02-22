"""Leer un número entero de dos dígitos y determinar a cuánto es igual la suma de sus
dígitos."""

try:
	number = int(input("Ingrese un numero entero de dos digitos"))

	if number >= 10 and number <= 99: #creamos la condicion para determinar si el numero ingresado es de dos digitos

		#obtenemos los digitos
		d1 = number // 10
		d2 = number % 10

		#realizamos la suma de los digitos obtenidos
		suma = d1 + d2 

		#imprimimos el resultado de la suma 
		print(f"la suma de los digitos es: {suma}")

	else:# si la condicion no se cumple imprimimos
		print("El numero no es de dos digitos")

except ValueError:
	print("error")