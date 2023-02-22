"""Leer un número entero y determinar si es negativo.
"""

try:
	number= int(input("Ingresa un numero entero")) #capturamos el numero entero

	if number < 0: ##verificamos si el numero ingresado es positivo o negativo
		print("Es un numero negativo")
	else:								
		print("Es un numero positivo")


except ValueError:
	print("el dato ingresado debe ser numerico") #en caso de que el usuario ingreso un dato que no es numerico, mostramos un mensaje