"""Leer un número entero de dos dígitos y determinar si ambos dígitos son pares."""	


try:
	#pedimos al usuario ingresar el numero, definimos variable

	number = int(input("Ingrese un numero entero de dos digitos"))

	#obtenemos los digitos del numero

	d1 = number // 10
	d2 = number % 10

	#creamos la condicion para saber si los dos digitos son par
	if d1 % 2 == 0 and d2 % 2 == 0:

		print("Los dos digitos son par ")
	else:
		print("Al menos uno de los dos digitos no es par")

except ValueError:
	print("Error")